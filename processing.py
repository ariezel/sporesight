import cv2
import numpy as np
import onnxruntime as ort
import os
import sys
from pathlib import Path

from resources import COLORS

''' Load class names from file '''
def load_class_names():
    default_class_names = ["unknown"]
    try:
        class_names_file = "classes.txt"
        with open(class_names_file, 'r') as f:
            class_names = [line.strip() for line in f.readlines()]
        
        if not class_names:
            print(f"Warning: Class names file is empty. Using default class names.")
            return default_class_names
            
        return class_names
        
    except FileNotFoundError:
        print(f"Warning: Class names file not found. Using default class names.")
        return default_class_names
    except Exception as e:
        print(f"Error loading class names: {str(e)}. Using default class names.")
        return default_class_names

''' Class to handle YOLO object detection using ONNX Runtime '''
class YoloDetector:
    def __init__(self, model_path):
        '''
        Initialize detector with ONNX model path
        
        Parameters:
        - model_path: Path to the ONNX model file. If None, will look in default locations.
        '''
        self.class_names = load_class_names()
        self.colors = COLORS
        self.onnx_session = None
        self.expected_image_shape = None


        # Save model path and initialize ONNX Runtime session
        self.model_path = model_path

        if not model_path or not os.path.exists(model_path):
            raise FileNotFoundError(f"ONNX model not found. Please provide a valid model path.")
        
        self.load_onnx_model()
    
    ''' Load the ONNX model '''
    def load_onnx_model(self):
        try:
            print(f"Loading ONNX model from {self.model_path}")
            # Create ONNX Runtime session with optimizations
            self.onnx_session = ort.InferenceSession(
                self.model_path, 
                providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
            )
            
            # Get model input shape from model metadata
            model_inputs = self.onnx_session.get_inputs()
            if model_inputs and len(model_inputs) > 0:
                # Assuming first input is the image
                input_shape = model_inputs[0].shape
                # YOLO models typically use format [batch, channels, height, width]
                if len(input_shape) == 4:
                    self.expected_image_shape = (input_shape[2], input_shape[3])
                    print(f"Model expects input shape: {self.expected_image_shape}")
                else:
                    # Default to 640x640 if shape cannot be determined
                    self.expected_image_shape = (640, 640)
                    print(f"Could not determine model input shape, using default: {self.expected_image_shape}")
            
            print("✅ ONNX model loaded successfully!")
            
        except Exception as e:
            print(f"Error loading ONNX model: {str(e)}")
            raise
    
    ''' Process Image '''
    def process_image(self, image_path):
        '''
        Process an image for object detection
        
        Parameters:
        - image_path: Path to the image file
        
        Returns:
        - result_image: Image with bounding boxes drawn
        - detections: List of detection tuples (class_name, confidence, box)
        '''
        # Check if ONNX session is loaded
        if not self.onnx_session or not self.expected_image_shape:
            raise RuntimeError("ONNX model not initialized properly")
        
        # Read and preprocess image
        original_image = cv2.imread(image_path)
        if original_image is None:
            raise ValueError(f"Could not read image from {image_path}")
            
        # Get image dimensions
        height, width, _ = original_image.shape
        
        # Calculate scaling factors
        expected_width = self.expected_image_shape[1]
        expected_height = self.expected_image_shape[0]
        self.scale = (width / expected_width, height / expected_height)
        
        # Preprocess image
        input_image = self.preprocess_image(original_image, expected_width, expected_height)
        
        # Get model predictions
        detections = self.infer_with_onnx(input_image)
        
        # Process predictions
        boxes, scores, class_ids = self.process_yolo_output(detections, self.scale)
        
        # Create result image with bounding boxes
        result_image = original_image.copy()
        
        # Format detection results
        detection_results = []
        for i in range(len(boxes)):
            x1, y1, x2, y2 = boxes[i].astype(int)
            class_id = class_ids[i]
            score = scores[i]
            
            # Get class name
            if 0 <= class_id < len(self.class_names):
                class_name = self.class_names[class_id]
            else:
                class_name = f"unknown_{class_id}"
            
            # Draw bounding box on image
            self.draw_bounding_box(result_image, class_id, score, x1, y1, x2, y2)
            
            # Add to results
            detection_results.append((class_name, score, [x1, y1, x2, y2]))
        
        return result_image, detection_results
    
    ''' Preprocess image '''
    def preprocess_image(self, image, target_width, target_height):
        '''
        Preprocess image for the YOLO model
        
        Parameters:
        - image: numpy array of the original image
        - target_width, target_height: dimensions required by the model
        
        Returns:
        - preprocessed image ready for inference
        '''

        # Resize image to target dimensions
        resized = cv2.resize(image, (target_width, target_height))
        # Normalize pixel values to [0,1]
        normalized = resized.astype(np.float32) / 255.0
        # Convert to channel-first format (for PyTorch/ONNX models)
        chw = normalized.transpose(2, 0, 1)
        # Add batch dimension
        batched = np.expand_dims(chw, axis=0)
        
        return batched
    
    ''' Inference with ONNX Runtime '''
    def infer_with_onnx(self, input_image):
        '''
        Run inference using ONNX Runtime
        
        Parameters:
        - input_image: preprocessed image tensor
        
        Returns:
        - detection results from the model
        '''
        try:
            # Get input name from model
            input_name = self.onnx_session.get_inputs()[0].name
            
            # Create input dictionary
            input_dict = {input_name: input_image}
            
            # Run inference
            outputs = self.onnx_session.run(None, input_dict)
            
            # Return first output (assuming that's the detection tensor)
            return outputs[0]
            
        except Exception as e:
            print(f"ONNX inference error: {str(e)}")
            raise
    
    ''' Process output retrieved from model '''
    def process_yolo_output(self, detections, scale, conf_threshold=0.25, iou_threshold=0.45):
        '''
        Process YOLO output tensor into bounding boxes, scores, and class IDs
        
        Parameters:
        - detections: output tensor from the model
        - scale: scaling factors (width_scale, height_scale)
        - conf_threshold: confidence threshold for filtering detections
        - iou_threshold: IoU threshold for non-maximum suppression
        
        Returns:
        - boxes: list of bounding boxes [x1, y1, x2, y2]
        - scores: list of confidence scores
        - class_ids: list of class IDs
        '''
        width_scale, height_scale = scale
        
        if len(detections.shape) == 3:
            detections = detections[0]  # Take first batch
        num_classes = detections.shape[1] - 5  # Subtract 5 for x,y,w,h,conf
        confidence_scores = detections[:, 4]
        
        mask = confidence_scores >= conf_threshold
        if not np.any(mask):
            return [], [], []
        
        filtered_detections = detections[mask]
        
        # Extract boxes, scores, and class IDs
        boxes = []
        scores = []
        class_ids = []
        
        for detection in filtered_detections:
            # Get box coordinates
            x, y, w, h = detection[0:4]
            
            # Convert to corner format and scale to original image dimensions
            x1 = (x - w/2) * width_scale
            y1 = (y - h/2) * height_scale
            x2 = (x + w/2) * width_scale
            y2 = (y + h/2) * height_scale
            
            # Get confidence score
            conf = detection[4]
            
            # Get class scores and ID
            if num_classes == 1:
                # If only one class, the class id is always 0
                class_id = 0
                class_score = 1.0
            else:
                # Get class with highest probability
                class_scores = detection[5:5+num_classes]
                class_id = np.argmax(class_scores)
                class_score = class_scores[class_id]
            
            # Final score is confidence * class probability
            score = float(conf * class_score)
            
            if score >= conf_threshold:
                boxes.append([x1, y1, x2, y2])
                scores.append(score)
                class_ids.append(class_id)
        
        # Convert to numpy arrays
        if not boxes:
            return [], [], []
            
        boxes = np.array(boxes)
        scores = np.array(scores)
        class_ids = np.array(class_ids)
        
        # Apply non-maximum suppression
        indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), conf_threshold, iou_threshold)
        
        if len(indices) > 0:
            # OpenCV returns indices in different formats depending on version
            if isinstance(indices, list):
                selected_indices = indices
            else:
                selected_indices = indices.flatten()
            
            return boxes[selected_indices], scores[selected_indices], class_ids[selected_indices]
        else:
            return [], [], []
    
    ''' Visualize bounding boxes '''
    def draw_bounding_box(self, img, class_id, confidence, x, y, x_plus_w, y_plus_h):
        
        # Safely get class name - if index is out of range, use a default name
        if 0 <= class_id < len(self.class_names):
            class_name = self.class_names[class_id]
        else:
            class_name = f"unknown_{class_id}"
        
        label = f'{class_name}: {confidence:.2f}'

        cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), self.colors[class_id], 4)
        
        # Text specifications
        font = cv2.FONT_HERSHEY_DUPLEX 
        font_scale = 0.75
        thickness = 2
        text_size, baseline = cv2.getTextSize(label, font, font_scale, thickness)
        text_w, text_h = text_size

        # Background rectangle for the text
        cv2.rectangle(img, (x, y - text_h - 10), (x + text_w, y), self.colors[class_id], -1)  # black background

        # Put text on top
        cv2.putText(img, label, (x, y - 5), font, font_scale, (255, 255, 255), thickness)  # white text

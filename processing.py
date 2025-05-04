import cv2
import numpy as np
import tritonclient.grpc as grpcclient

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

''' Class to handle YOLO object detection using Triton Inference Server '''
class YoloDetector:
    def __init__(self, model_name, server_url='localhost:8001'):
        '''
        Initialize detector with model name and server URL
        
        Parameters:
        - model_name: Name of the YOLO model on Triton server
        - server_url: URL of the Triton Inference Server
        '''
        self.model_name = model_name
        self.server_url = server_url
        self.triton_client = None
        self.expected_image_shape = None
        self.class_names = load_class_names()
        self.colors = COLORS
        
        # Initialize Triton client
        self.connect_to_triton()
    
    ''' Connect to the Triton Inference Server '''
    def connect_to_triton(self):
        try:
            keepalive_options = grpcclient.KeepAliveOptions(
                keepalive_time_ms=2**31 - 1,
                keepalive_timeout_ms=20000,
                keepalive_permit_without_calls=False,
                http2_max_pings_without_data=2
            )
            
            self.triton_client = grpcclient.InferenceServerClient(
                url=self.server_url,
                verbose=False,
                keepalive_options=keepalive_options
            )
            
            if self.triton_client.is_server_live():
                print("✅ Triton server is live!")
                # Get model metadata to determine expected shape
                model_metadata = self.triton_client.get_model_metadata(self.model_name)
                self.expected_image_shape = model_metadata.inputs[0].shape[-2:]
            else:
                print("❌ Triton server is not responding.")
                
        except Exception as e:
            print(f"Triton connection failed: {str(e)}")
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
        # Check if Triton client is connected
        if not self.triton_client or not self.expected_image_shape:
            self.connect_to_triton()
        
        # TODO connect to camera
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
        detections = self.infer_with_triton(input_image)
        
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
    
    ''' Inference to Triton Server '''
    def infer_with_triton(self, input_image):
        '''
        Send inference request to Triton server
        
        Parameters:
        - input_image: preprocessed image tensor
        
        Returns:
        - detection results from the model
        '''
        try:
            # Prepare input tensor
            inputs = []
            inputs.append(grpcclient.InferInput("images", input_image.shape, "FP32"))
            inputs[0].set_data_from_numpy(input_image)
            
            # Specify output tensor
            outputs = []
            outputs.append(grpcclient.InferRequestedOutput("output0"))
            
            # Send inference request
            response = self.triton_client.infer(
                model_name=self.model_name,
                inputs=inputs,
                outputs=outputs
            )
            
            # Get output tensor
            return response.as_numpy("output0")
            
        except Exception as e:
            print(f"Inference error: {str(e)}")
            raise
    
    ''' Process output retrieved from server '''
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
    
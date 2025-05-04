import os
import json
import time
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtGui import *

'''Manages detection storage, organization and retrieval'''
class DetectionManager:
    
    def __init__(self, base_dir="./detections"):
        self.base_dir = base_dir
        # Create base directory if it doesn't exist
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
    
    def save_detection(self, image, detection_details, timestamp=None):
        '''
        Save detection image and metadata
        
        Parameters:
        - image: numpy array (cv2 image)
        - detection_details: list of tuples (class_name, confidence, box)
        - timestamp: optional timestamp (uses current time if None)
        
        Returns:
        - tuple (image_path, metadata_path)
        '''
        # Use current timestamp if none provided
        if timestamp is None:
            timestamp = int(time.time())
        
        # Convert timestamp to date string for folder organization
        date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        date_folder = os.path.join(self.base_dir, date_str)
        
        # Create date folder if it doesn't exist
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)
        
        # Create filenames
        base_filename = f"detection_{timestamp}"
        image_path = os.path.join(date_folder, f"{base_filename}.jpg")
        metadata_path = os.path.join(date_folder, f"{base_filename}.txt")
        
        # Save the image
        import cv2
        cv2.imwrite(image_path, image)
        
        # Format metadata for storage
        metadata = {
            "timestamp": timestamp,
            "date": date_str,
            "detections": []
        }
        
        # Add each detection with formatted coordinates
        for class_name, confidence, box in detection_details:
            metadata["detections"].append({
                "class": class_name,
                "confidence": float(confidence),
                "box": [float(coord) for coord in box]
            })
        
        # Save metadata as JSON
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2)
        
        return image_path, metadata_path
    
    def get_detection_dates(self):
        '''
        Get list of all dates that have detections
        
        Returns:
        - List of date strings (YYYY-MM-DD format)
        '''
        dates = []
        # List all subdirectories in base directory
        for item in os.listdir(self.base_dir):
            item_path = os.path.join(self.base_dir, item)
            # Check if it's a directory and follows date format
            if os.path.isdir(item_path) and self._is_date_format(item):
                dates.append(item)
        
        # Sort dates newest first
        dates.sort(reverse=True)
        return dates
    
    def _is_date_format(self, date_str):
        '''Check if string is in YYYY-MM-DD format'''
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def get_detections_by_date(self, date_str):
        '''
        Get all detections for a specific date
        
        Parameters:
        - date_str: Date string in YYYY-MM-DD format
        
        Returns:
        - List of (image_path, metadata) tuples
        '''
        date_folder = os.path.join(self.base_dir, date_str)
        if not os.path.exists(date_folder):
            return []
        
        detections = []
        image_files = {}
        metadata_files = {}
        
        # First pass: collect all files
        for file in os.listdir(date_folder):
            file_path = os.path.join(date_folder, file)
            base_name = os.path.splitext(file)[0]
            ext = os.path.splitext(file)[1].lower()
            
            if ext == '.jpg' or ext == '.png':
                image_files[base_name] = file_path
            elif ext == '.txt':
                metadata_files[base_name] = file_path
        
        # Second pass: match image and metadata files
        for base_name in image_files:
            if base_name in metadata_files:
                # Load metadata
                try:
                    with open(metadata_files[base_name], 'r') as f:
                        metadata = json.load(f)
                    
                    # Check if image exists
                    if os.path.exists(image_files[base_name]):
                        # Convert metadata format back to tuples for consistency
                        detection_tuples = []
                        for det in metadata.get("detections", []):
                            detection_tuples.append((
                                det["class"],
                                det["confidence"],
                                det["box"]
                            ))
                        
                        detections.append((image_files[base_name], detection_tuples))
                except Exception as e:
                    print(f"Error loading detection {base_name}: {str(e)}")
        
        # Sort by timestamp (newest first)
        detections.sort(key=lambda x: os.path.basename(x[0]), reverse=True)
        return detections
    
    def get_all_detections(self, max_per_date=None):
        '''
        Get all detections across all dates
        
        Parameters:
        - max_per_date: Optional limit for detections per date
        
        Returns:
        - List of (image_path, metadata) tuples
        '''
        all_detections = []
        for date in self.get_detection_dates():
            date_detections = self.get_detections_by_date(date)
            if max_per_date:
                date_detections = date_detections[:max_per_date]
            all_detections.extend(date_detections)
        
        return all_detections
    
    def get_date_folder_path(self, date_str):
        """
        Get the folder path for a specific date
        
        Args:
            date_str (str): Date string in format 'YYYY-MM-DD'
            
        Returns:
            str: Path to the folder for this date, or None if invalid
        """
        if not date_str or date_str == "All Dates":
            return None
            
        date_folder = os.path.join(self.base_dir, date_str)
        
        if os.path.exists(date_folder) and os.path.isdir(date_folder):
            return date_folder
        return None
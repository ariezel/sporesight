from PySide6.QtCore import *
from PySide6.QtGui import *
import cv2

class CameraThread(QThread):
    # Signal for updating image
    imageUpdate = Signal(QImage)
    # Signal for connection failure
    connectionFailed = Signal(str)

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.stream_url = url 
        self.CameraThreadActive = None  
        self.frame = None

    def run(self):
        self.CameraThreadActive = True
        try:
            # Convert numeric string to integer for camera indices
            camera_source = self.stream_url
            if self.stream_url.isdigit():
                camera_source = int(self.stream_url)
                
            print(f"Opening camera stream at {camera_source}")
            capture = cv2.VideoCapture(camera_source)
            
            if not capture.isOpened():
                error_msg = f"Error: Could not open video stream at {self.stream_url}"
                
                self.connectionFailed.emit(error_msg)
                return error_msg
                
            while self.CameraThreadActive:
                ret, frame = capture.read()
                self.frame = frame
                
                if not ret:
                    print("Error: Could not read frame.")
                    # If we lose connection, wait a moment and try to reconnect
                    if not self.CameraThreadActive:  # Check before sleeping
                        break
                    QThread.msleep(1000)  # Sleep for 1 second
                    capture.release()
                    
                    # Try to reconnect with the same conversion logic
                    if not self.CameraThreadActive:  # Check before reconnecting
                        break
                    
                    camera_source = self.stream_url
                    if self.stream_url.isdigit():
                        camera_source = int(self.stream_url)
                        
                    capture = cv2.VideoCapture(camera_source)
                    if not capture.isOpened():
                        print("Reconnection failed. Stopping camera thread.")
                        break
                    continue
                    
                # Process frame as before
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQt = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                scaled_img = convertToQt.scaled(1920, 1080, Qt.KeepAspectRatio)
                
                if self.CameraThreadActive:  # Make sure we're still active before emitting
                    self.imageUpdate.emit(scaled_img)
                
                # Add a small delay to prevent high CPU usage
                if not self.CameraThreadActive:  # Check before sleeping
                    break
                QThread.msleep(10)
                
        except Exception as e:
            print(f"Camera thread error: {str(e)}")
            self.connectionFailed.emit(f"Camera error: {str(e)}")
        finally:
            if 'capture' in locals() and capture is not None:
                capture.release()
            print("Camera thread stopped")

    def stop(self):
        self.CameraThreadActive = False
        self.quit()
        
        # Use a timer to avoid blocking
        wait_timer = QTimer()
        wait_timer.setSingleShot(True)
        wait_timer.timeout.connect(self.terminate)
        wait_timer.start(1000)  # Give it 500ms to quit properly\
    
    def get_frame(self):
        return self.frame
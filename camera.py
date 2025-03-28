import cv2

from PySide6.QtCore import *
from PySide6.QtGui import *

# Replace with the camera's stream URL
stream_url = "rtsp://192.168.7.1:554/axis-media/media.amp?streamprofile=Quality"

''' Threading is necessary for multitasking; prevents program window from freezing '''
class CameraThread(QThread):
    imageUpdate = Signal(QImage)

    ''' Check available indices of camera feeds'''
    ''' This is only viable for connection via USB '''
    def test(self):
        for i in range(5):  
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"Camera found at index {i}")             
                cap.release()
        pass

    ''' Run thread, access the camera feed '''
    def run(self):
        self.CameraThreadActive = True
        capture = cv2.VideoCapture(0) # Change VideoCapture value

        if not capture.isOpened():
            print("Error: Could not open video stream.")
            return None  # Return a specific value if capture fails

        while self.CameraThreadActive:
            ret, frame = capture.read()

            if not ret:
                print("Error: Could not read frame.")
                return None

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Flip image for PyQt to understand
            flippedImage = cv2.flip(img, 1)
            convertToQt = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)

            # Change size of QImage
            scaledImg = convertToQt.scaled(640, 480, Qt.KeepAspectRatio) # Can be resized

            # Send signal to Main Window class
            self.imageUpdate.emit(scaledImg)

        capture.release()

    ''' Stop the while loop '''
    def stop(self):
        self.CameraThreadActive = False
        self.quit()

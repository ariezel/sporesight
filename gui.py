from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from feed import CameraThread  # Import CameraThread

'''
    TODO:
    - GUI
        [  ] Resize window to full screen
        [  ] Loading screen for camera feed
    - AI
        [  ] VBOX/Column for statistics
        [  ] Triton server connection
'''

title = "SporeSight" 

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__() 

        self.setWindowTitle(title)

        self.VBL = QVBoxLayout()
        self.feedLabel = QLabel()

        # Cancels the feed, does not stop the program
        self.cancelBTN = QPushButton("Cancel")
        self.cancelBTN.clicked.connect(self.cancelFeed)

        self.VBL.addWidget(self.feedLabel)
        self.VBL.addWidget(self.cancelBTN)

        # Call CameraThread
        self.CameraThread = CameraThread()
        self.CameraThread.start()
        self.CameraThread.imageUpdate.connect(self.imageUpdateSlot)

        self.setLayout(self.VBL)
    
    def imageUpdateSlot(self, img):
        self.feedLabel.setPixmap(QPixmap.fromImage(img))

    def cancelFeed(self):
        self.CameraThread.stop()
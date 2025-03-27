from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from camera import CameraThread  # Import CameraThread

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # # self.ui = Ui_Splash()
        # self.ui.setupUi(self)
    
        # Set the splash screen into frameless window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setCenter()       
        self.setShadow() 

        # Set the timer in the loading bar on the splash screen
        self.timer = QTimer()
        self.timer.timeout.connect(self.setProgress)
        self.timer.start(35)

        # Change the text 
        QTimer.singleShot(1500, lambda: self.ui.splash_caption_lbl.setText("Loading configuration..."))
        QTimer.singleShot(3000, lambda: self.ui.splash_caption_lbl.setText("Loading application..."))

        self.show()

    # Function for setting the splash screen into center of the window screen
    def setCenter(self):
        screen = self.frameGeometry()
        center = QGuiApplication.primaryScreen().availableGeometry().center()
        screen.moveCenter(center)
        self.move(screen.topLeft())

    # Function for setting the drop shadow effect in the splash screen
    def setShadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(125, 204, 204, 250))
        self.ui.splash_frame.setGraphicsEffect(self.shadow)

    # Function for setting the value of the splash progress bar
    def setProgress(self):
        global splash_counter
        self.ui.splash_progress.setValue(splash_counter)

        if splash_counter > 100:
            self.timer.stop()
            self.main = Main()
            self.main.show()
            self.close()

        splash_counter += 1



from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from resources import SS_LOGO_PNG
from ui.splash_ui import Ui_Splash
from app import MainWindow  

splash_counter = 0

class Splash(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        # Set the splash screen into frameless window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Center window and set shadow
        self.setCenter()       
        self.setShadow() 
        
        # Configure loading text and progress
        self.setup_loading()
        
        # Add fade-in animation
        self.setup_animations()
        
        # Show the splash screen
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
        self.shadow.setColor(QColor(102, 51, 153, 1))
        self.ui.splash_frame.setGraphicsEffect(self.shadow)
    
    def setup_loading(self):
        # Set initial text
        self.ui.splash_caption_lbl.setText("Starting up...")
        
        # Initialize progress bar
        self.ui.splash_progress.setValue(0)
        
        # Set progressive loading text
        self.loading_steps = [
            (1500, "Setting up application..."),
            (3000, "Loading modules..."),
            (4500, "Connecting to services..."),
            (6000, "Welcome...")
        ]
        
        # Schedule text changes
        for time, text in self.loading_steps:
            QTimer.singleShot(time, lambda t=text: self.ui.splash_caption_lbl.setText(t))
        
        # Set the timer in the loading bar on the splash screen
        self.timer = QTimer()
        self.timer.timeout.connect(self.setProgress)
        self.timer.start(60)  # Slightly slower for smoother animation
    
    def setup_animations(self):
        # Initial opacity
        self.setWindowOpacity(0.0)
        
        # Fade-in animation
        self.fade_in = QPropertyAnimation(self, b"windowOpacity")
        self.fade_in.setDuration(1000)
        self.fade_in.setStartValue(0.0)
        self.fade_in.setEndValue(1.0)
        self.fade_in.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_in.start()

    # Function for setting the value of the splash progress bar
    def setProgress(self):
        global splash_counter
        # Add a slight pulsing effect
        import math
        pulse = 5 * math.sin(splash_counter / 5)
        progress_value = min(splash_counter + pulse, 100)
        self.ui.splash_progress.setValue(progress_value)

        if splash_counter >= 100:
            self.timer.stop()
            self.close_splash()
            
        splash_counter += 1
    
    def close_splash(self):
        # Fade out animation
        self.fade_out = QPropertyAnimation(self, b"windowOpacity")
        self.fade_out.setDuration(1000)
        self.fade_out.setStartValue(1.0)
        self.fade_out.setEndValue(0.0)
        self.fade_out.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_out.finished.connect(self.on_fade_out_finished)
        self.fade_out.start()
    
    def on_fade_out_finished(self):
        # Start main window and close splash
        self.main = MainWindow()
        self.main.showMaximized()
        self.close()
    
    # Required for QPropertyAnimation to work with windowOpacity
    def getWindowOpacity(self):
        return super().windowOpacity()
        
    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity)
        
    # Using Property from PySide6.QtCore
    windowOpacity = Property(float, getWindowOpacity, setWindowOpacity)
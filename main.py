'''
    References
        [1] QCameraThread  for OpenCV Feed in PyQt (SH) : https://www.youtube.com/watch?v=dTDgbx-XelY


'''

import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.showMaximized()
    sys.exit(App.exec())
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from app import MainWindow
from resources import STYLE_QSS 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load QSS file safely
    style_path = Path(STYLE_QSS)
    if style_path.exists():
        with style_path.open("r") as style_file:
            app.setStyleSheet(style_file.read())

    root = MainWindow()
    root.showNormal()

    sys.exit(app.exec())

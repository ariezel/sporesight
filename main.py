import argparse, sys, os
from pathlib import Path
from PySide6.QtWidgets import QApplication
from app import MainWindow
from resources import STYLE_QSS

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    '''Change model name'''
    parser.add_argument("--model_name", type=str, required=False, default="yolov5", help="Model name")
    parser.add_argument("--url", type=str, required=False, default="localhost:8001", help="Inference server URL. Default is localhost:8001.")
    args = parser.parse_args()

    app = QApplication(sys.argv)

    # Try to read the QSS file content
    try:
        # Determine if running as bundled app or in development
        if getattr(sys, 'frozen', False):
            # If frozen (PyInstaller bundle)
            style_path = os.path.join(sys._MEIPASS, "ui", "style.qss")
        else:
            # In development
            style_path = STYLE_QSS
        
        print(f"Loading style from: {style_path}")  # Debug info
        
        # Read and apply stylesheet
        with open(style_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())
            
    except Exception as e:
        print(f"Error loading style file: {e}")
        # Continue without the stylesheet

    root = MainWindow(args.model_name, args.url)
    root.showMaximized()

    sys.exit(app.exec())
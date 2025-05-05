import argparse, sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from app import MainWindow
from resources import STYLE_QSS 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, required=False, default="./models/YOLOv5.onnx", help="Model name")
    parser.add_argument("--url", type=str, required=False, default="localhost:8001", help="Inference server URL. Default is localhost:8001.")
    args = parser.parse_args()

    app = QApplication(sys.argv)

    # Load QSS file safely
    style_path = Path(STYLE_QSS)
    if style_path.exists():
        with style_path.open("r") as style_file:
            app.setStyleSheet(style_file.read())

    root = MainWindow(args.model_name, args.url)
    root.showMaximized()

    sys.exit(app.exec())

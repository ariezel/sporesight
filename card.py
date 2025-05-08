import os, time
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtCore import *
from processing import load_class_names
from resources import COLORS
from dialog import DetectionDialog

class DetectionCard(QFrame):
    ''' Card widget to display full image with detection results '''
    def __init__(self, image_path, detections, class_names, parent=None):
        '''
        Parameters:
        - image_path: Path to the full image with detections
        - detections: List of tuples (class_name, confidence, box) for all detections in the image
        '''
        super().__init__(parent)
        
        # Store detections data
        self.image_path = image_path
        self.detections = detections
        self.timestamp = ''
        self.class_names = class_names
        self.colors = COLORS
        
        # Set frame style
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet('''
            DetectionCard {
                background-color: white;
                border-radius: 14px;
                padding-top: 15px;
                padding-right: 10px;
                padding-left: 10px;
                padding-bottom: 5px;
            }
            DetectionCard:hover {
                background-color: white;
                border-radius: 14px;
            }
        ''')

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 30))  # semi-transparent black
        self.setGraphicsEffect(shadow)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Header with timestamp and menu button
        header_layout = QHBoxLayout()
        
        # Extract timestamp from filename if available
        timestamp_label = QLabel()
        if image_path:
            filename = os.path.basename(image_path)
            
            # Try to extract timestamp from filename (format: detections_TIMESTAMP.jpg)
            if '_' in filename:
                try:
                    timestamp = int(filename.split('_')[1].split('.')[0])
                    self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                except (ValueError, IndexError):
                    self.timestamp = filename  # Use filename if extraction fails
            else:
                self.timestamp = filename
                
            timestamp_label.setText(self.timestamp)
        else:
            timestamp_label.setText("No timestamp")
            
        timestamp_label.setStyleSheet("color: #666; font-size: 12px;")
        header_layout.addWidget(timestamp_label, 1)
        layout.addLayout(header_layout)
        
        # Image preview with detections drawn
        if image_path and os.path.exists(image_path):
            image_label = QLabel()
            pixmap = QPixmap(image_path)
            image_label.setPixmap(pixmap.scaled(QSize(320, 240), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setStyleSheet("border-radius:14px;")
            layout.addWidget(image_label)
        else:
            # No image available
            no_image = QLabel("No Image Available")
            no_image.setAlignment(Qt.AlignCenter)
            no_image.setStyleSheet("color: #999; padding: 40px;")
            layout.addWidget(no_image)
        
        # Detection summary
        summary_label = QLabel(f"{len(detections)} Detection{'s' if len(detections) != 1 else ''}")
        summary_label.setAlignment(Qt.AlignLeft)
        summary_label.setFont(QFont("Arial", 12, QFont.Bold))
        summary_label.setStyleSheet("color: #4F1C51; padding-top: 10px")
        layout.addWidget(summary_label)
        
        # Detection classes preview (show first 3 classes with counts)
        class_counts = {}
        for class_name, _, _ in detections:
            if class_name in class_counts:
                class_counts[class_name] += 1
            else:
                class_counts[class_name] = 1
        
        # Create compact class summary
        if class_counts:
            classes_text = ", ".join([f"{count}x {name}" for name, count in list(class_counts.items())[:3]])
            if len(class_counts) > 3:
                classes_text += ", ..."
        else:
            classes_text = "No detections found"
            
        classes_label = QLabel(classes_text)
        classes_label.setWordWrap(True)
        classes_label.setAlignment(Qt.AlignLeft)
        classes_label.setStyleSheet("color: #666; padding-left: 2px")
        layout.addWidget(classes_label)
        
        # Add spacer
        layout.addStretch()
        
        # View button
        view_btn = QPushButton("View Details")
        view_btn.setStyleSheet('''
            QPushButton {
                background-color: white;
                border: 1px solid #4F1C51;
                color: #4F1C51;
                padding: 10px 10px;
                border-radius: 14px;
                font-weight: 700;
                margin-top: 10px;
                text-align:center;
            }
            QPushButton:hover {
                background-color: #4F1C51;
                color: white;
            }
        ''')
        view_btn.setFixedWidth(120)
        
        # Connect the button to show details dialog
        if image_path and os.path.exists(image_path):
            view_btn.clicked.connect(self.show_detection_details)
        
        # Button container for centering
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.addWidget(view_btn, 0, Qt.AlignRight)
        btn_layout.setContentsMargins(0, 0, 5, 5)
        
        layout.addWidget(btn_container)

    ''' Show a dialog with the full image and list of all detections '''
    def show_detection_details(self):
        deleted_path = DetectionDialog.show_detection_view(
            parent=self.parent(),
            image_path=self.image_path,
            detections=self.detections,
            title=os.path.basename(self.image_path),
            timestamp=self.timestamp,
            class_names=self.class_names,
            colors=self.colors
        )

        if deleted_path:
            try:
                image_exists = os.path.exists(deleted_path)
                txt_file = os.path.splitext(deleted_path)[0] + '.txt'
                txt_exists = os.path.exists(txt_file)
                
                if not image_exists and not txt_exists:
                    QMessageBox.warning(
                        self,
                        "File Not Found",
                        f"Could not find files to delete: {os.path.basename(deleted_path)}",
                        QMessageBox.Ok
                    )
                    return
                
                # Delete the image file
                if image_exists:
                    os.remove(deleted_path)
                    print(f"Deleted image: {deleted_path}")
                
                # Delete the associated txt file
                if txt_exists:
                    os.remove(txt_file)
                    print(f"Deleted associated text file: {txt_file}")
                
                # Find the main window to update analytics
                main_window = self.find_main_window()
                self.remove_from_layout()
                
                # Update analytics page if main window was found
                if main_window and hasattr(main_window, 'update_analytics_page'):
                    QTimer.singleShot(100, main_window.update_analytics_page)
                    print("Analytics page update scheduled after deletion")
                else:
                    print("Warning: Could not find main window or update_analytics_page method")
                
                # # Show success message
                # QMessageBox.information(
                #     self,
                #     "Deletion Success",
                #     f"Detection has been deleted successfully.",
                #     QMessageBox.Ok
                # )
                
            except Exception as e:
                print(f"Error deleting files: {str(e)}")
                import traceback
                traceback.print_exc()
                QMessageBox.warning(
                    self,
                    "Deletion Error",
                    f"Failed to delete one or more files: {str(e)}",
                    QMessageBox.Ok
                )
    
    ''' Find the main window instance from the widget hierarchy '''
    def find_main_window(self):
        widget = self.parent()
        while widget is not None:
            if isinstance(widget, QMainWindow):
                return widget
            widget = widget.parent()
        return None
    
    ''' Remove this card from its parent layout '''
    def remove_from_layout(self):
        try:
            parent = self.parent()
            if not parent:
                print("Warning: Card has no parent widget")
                return False
                
            # Get the layout containing this card
            parent_layout = parent.layout()
            if not parent_layout:
                print("Warning: Parent has no layout")
                return False
                
            # Find the index of this card in the layout
            found = False
            for i in range(parent_layout.count()):
                item = parent_layout.itemAt(i)
                if item and item.widget() == self:
                    parent_layout.removeItem(item)
                    self.setParent(None)  
                    self.deleteLater()    
                    found = True
                    break
                    
            if not found:
                print("Warning: Card not found in parent layout")
                # Try alternative approach - hide the card
                self.hide()
                self.setParent(None)
                self.deleteLater()

            parent.update()
            
            print(f"Card removed for deleted image: {os.path.basename(self.image_path)}")
            return True
            
        except Exception as e:
            print(f"Error removing card from layout: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

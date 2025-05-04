import os
from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QFrame, 
    QTableWidget, QHeaderView, QTableWidgetItem, QPushButton, 
    QProgressBar, QAbstractItemView, QMessageBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QSize, Signal

'''
Reusable dialog component for displaying detection results
Can be used for both confirming new detections and viewing saved ones
'''
class DetectionDialog(QDialog):

    # Signal for delete operation
    deletionRequested = Signal(str)

    def __init__(
        self, 
        parent=None, 
        image_path="", 
        detections=None, 
        title="Detection Results", 
        timestamp="",
        class_names=None, 
        colors=None,
        mode="view"  # "view" or "confirm"
    ):
        super().__init__(parent)
        
        # Store parameters
        self.image_path = image_path
        self.detections = detections or []
        self.timestamp = timestamp
        self.class_names = class_names or []
        self.colors = colors or [(0, 120, 255)]  # Default blue if no colors provided
        self.mode = mode
        self.result = False  # For confirmation mode: True=save, False=discard
        
        # Set dialog properties
        self.setWindowTitle(title)
        self.setMinimumSize(1100, 600)
        
        # Set dialog styling
        self.setStyleSheet('''
            QDialog {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333;
            }
            QPushButton {
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
        ''')
        
        # Initialize UI
        self.init_ui()
    
    '''Set up the dialog UI'''
    def init_ui(self):
        # Main layout - horizontal to split left/right panels
        layout = QHBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Create and add panels
        left_panel = self.create_image_panel()
        right_panel = self.create_info_panel()
        
        layout.addWidget(left_panel, 60)  # 60% width
        layout.addWidget(right_panel, 40)  # 40% width
    
    '''Create the left panel containing the image'''
    def create_image_panel(self):
        panel = QWidget()
        panel.setStyleSheet('''
            QWidget {
                background-color: white;
                border-radius: 8px;
            }
        ''')
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Add title
        title_text = self.timestamp if self.timestamp and self.mode == "view" else "Preview"
        image_title = QLabel(title_text)
        image_title.setFont(QFont("Arial", 12, QFont.Bold))
        image_title.setStyleSheet("color: #4F1C51;")
        image_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_title)
        
        # Create frame for image
        image_frame = QFrame()
        image_frame.setFrameShape(QFrame.StyledPanel)
        image_frame_layout = QVBoxLayout(image_frame)
        
        # Add image to dialog if available
        image_label = QLabel()
        if self.image_path and os.path.exists(self.image_path):
            pixmap = QPixmap(self.image_path)
            image_label.setPixmap(pixmap.scaled(
                QSize(700, 700), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            ))
        else:
            image_label.setText("Image not available")
            image_label.setStyleSheet("color: #999; font-size: 14px;")
        
        image_label.setAlignment(Qt.AlignCenter)
        image_frame_layout.addWidget(image_label)
        layout.addWidget(image_frame, 1)  # 1 is stretch factor
        
        # Path label
        path_text = f"File: {os.path.basename(self.image_path)}" if self.image_path else "No file"
        path_label = QLabel(path_text)
        path_label.setStyleSheet('''
            color: #666; 
            font-size: 12px;
            background-color: white;
            padding: 5px 20px;
            border-radius: 3px;
            margin-bottom: 10px                    
        ''')
        path_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(path_label)
        
        return panel
    
    '''Create the right panel with detection info and buttons'''
    def create_info_panel(self):
        panel = QWidget()
        panel.setStyleSheet('''
            QWidget {
                background-color: white;
                border-radius: 8px;
            }
        ''')
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Header with detection count
        detected_items = len(self.detections)
        header_label = QLabel(f"Detections ({detected_items})")
        header_label.setFont(QFont("Arial", 14, QFont.Bold))
        header_label.setStyleSheet("color: #4F1C51;")
        layout.addWidget(header_label)
        
        # Add detection table
        table = self.create_detection_table()
        layout.addWidget(table, 1)  # 1 is stretch factor
        
        # Add confirmation section if in confirmation mode
        if self.mode == "confirm":
            self.add_confirmation_buttons(layout)
        else:  # View mode - just a close button
            button_box = QWidget()
            button_layout = QHBoxLayout(button_box)
            button_layout.setContentsMargins(0, 10, 0, 0)
            
            close_btn = QPushButton("Close")
            close_btn.setStyleSheet('''
                QPushButton {
                    border-radius: 14px;
                    padding: 15px 10px;
                    text-align: center;
                    color: white;
                    font-weight: 700;
                    background-color: #210F37;
                }
                QPushButton:hover {
                    background-color: #4F1C51;
                }
            ''')
            close_btn.clicked.connect(self.accept)

            # Discard button
            delete_btn = QPushButton("Delete")
            delete_btn.setStyleSheet('''
                QPushButton {
                    border-radius: 14px;
                    padding: 15px 10px;
                    text-align: center;
                    color: white;
                    font-weight: 700;
                    background-color: #900D09;
                }
                QPushButton:hover {
                    background-color: red;
                }
            ''')
            delete_btn.clicked.connect(self.delete_clicked)
            
            button_layout.addWidget(delete_btn)
            button_layout.addWidget(close_btn)
            layout.addWidget(button_box)
        
        return panel
    
    '''Create the table showing detection details'''
    def create_detection_table(self):
        info_frame = QFrame()
        info_frame.setFrameShape(QFrame.StyledPanel)
        info_frame.setStyleSheet('''
            QFrame {
                background-color: white;
                border-radius: 4px;
                border: none;
            }
        ''')
        info_layout = QVBoxLayout(info_frame)
        
        if self.detections:
            # Create table
            table = QTableWidget()
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(["Class", "Confidence"])
            table.setRowCount(len(self.detections))
            table.setSelectionBehavior(QAbstractItemView.SelectRows)
            table.setAlternatingRowColors(True)
            table.setShowGrid(False)
            table.setFocusPolicy(Qt.NoFocus)
            
            # Configure header
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            
            # Hide row numbers
            table.verticalHeader().setVisible(False)
            
            # Style the table
            table.setStyleSheet('''
                QTableWidget {
                    border-radius: 4px;
                    background-color: white;
                    selection-background-color: #F1E4F3;
                    selection-color: #4F1C51;
                }
                QTableWidget::item {
                    border-bottom: 1px solid #f0f0f0;
                }
                QTableWidget::item:selected {
                    background-color: #F1E4F3;
                    color: #4F1C51;
                }
                QHeaderView::section {
                    background-color: #f8f9fa;
                    padding: 4px 8px;  
                    border: none;
                    border-bottom: 1px solid #ddd;
                    font-weight: bold;
                    color: #666;
                }
            ''')
            
            for i, det in enumerate(self.detections):
                if isinstance(det, tuple) and len(det) >= 2:
                    class_name = det[0]
                    confidence = det[1]  # Assume confidence is between 0-1
                    
                    # Add class name
                    class_item = QTableWidgetItem(class_name)
                    table.setItem(i, 0, class_item)
                    
                    # Add confidence as progress bar
                    conf_widget = QWidget()
                    conf_layout = QHBoxLayout(conf_widget)
                    conf_layout.setContentsMargins(4, 2, 4, 2)
                    
                    # Get color based on class
                    qt_color = self.get_class_color(class_name)
                    
                    # Create progress bar
                    progress = QProgressBar()
                    progress.setRange(0, 100)
                    confidence_value = int(confidence * 100)  # Convert to percentage
                    progress.setValue(confidence_value)
                    progress.setTextVisible(True)
                    progress.setFormat(f"{confidence:.2f}")
                    
                    # Apply the class color to the progress bar
                    progress.setStyleSheet(f'''
                        QProgressBar {{
                            border: none;
                            border-radius: 2px;
                            background-color: #f0f0f0;
                            height: 16px;
                            text-align: center;
                        }}
                        QProgressBar::chunk {{
                            background-color: {qt_color};
                            border-radius: 2px;
                        }}
                    ''')
                    
                    conf_layout.addWidget(progress)
                    table.setCellWidget(i, 1, conf_widget)
                else:
                    # Handle unexpected format
                    table.setItem(i, 0, QTableWidgetItem("Unknown"))
                    table.setItem(i, 1, QTableWidgetItem("N/A"))
            
            info_layout.addWidget(table)
        else:
            # No detections message
            no_detection_label = QLabel("No objects detected.")
            no_detection_label.setAlignment(Qt.AlignCenter)
            no_detection_label.setStyleSheet("font-size: 14px; color: #666; padding: 20px;")
            info_layout.addWidget(no_detection_label)
        
        return info_frame
    
    '''Add save/discard buttons for confirmation mode'''
    def add_confirmation_buttons(self, layout):
        confirm_label = QLabel("Do you want to save this detection?")
        confirm_label.setFont(QFont("Arial", 11))
        confirm_label.setStyleSheet("color: #333; margin-top: 15px; font-weight: 700;")
        confirm_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(confirm_label)
        
        # Add button container
        button_box = QWidget()
        button_layout = QHBoxLayout(button_box)
        button_layout.setContentsMargins(0, 10, 0, 0)
        
        # Save button
        save_btn = QPushButton("Save Detection")
        save_btn.setStyleSheet('''
            QPushButton {
                border-radius: 14px;
                padding: 15px 10px;
                text-align: center;
                color: white;
                font-weight: 700;
                background-color: #210F37;
            }
            QPushButton:hover {
                background-color: #4F1C51;
            }
        ''')
        save_btn.clicked.connect(self.save_clicked)
        
        # Discard button
        discard_btn = QPushButton("Discard")
        discard_btn.setStyleSheet('''
            QPushButton {
                border-radius: 14px;
                padding: 15px 10px;
                text-align: center;
                color: white;
                font-weight: 700;
                background-color: #900D09;
            }
            QPushButton:hover {
                background-color: red;
            }
        ''')
        discard_btn.clicked.connect(self.discard_clicked)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(discard_btn)
        layout.addWidget(button_box)
    
    '''Get color for a specific class'''
    def get_class_color(self, class_name):
        try:
            # Determine the index of the class
            if class_name in self.class_names:
                class_id = self.class_names.index(class_name)
            else:
                class_id = 0
                    
            # Ensure we have colors and index is in range
            if self.colors and len(self.colors) > 0:
                class_id = class_id % len(self.colors)
                cv_color = self.colors[class_id]
                rgb_color = (cv_color[2], cv_color[1], cv_color[0])
                hex_color = f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}"
                return hex_color
            else:
                print("Warning: No colors available, using fallback")
                return "#3498db"  # Default blue
        except Exception as e:
            print(f"Error getting class color: {str(e)}")
            return "#3498db"  # Default blue
    
    '''Handle save button click'''
    def save_clicked(self):
        self.result = True
        self.accept()
        
    '''Handle discard button click'''
    def discard_clicked(self):
        self.result = False
        self.accept()

    '''Handle delete button click (new method)'''
    def delete_clicked(self):
        # Show confirmation dialog
        response = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete this image and its detection data?\n\n{self.image_path}",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No  # Default is No for safety
        )
        
        if response == QMessageBox.Yes:
            # Emit the signal with the image path
            self.deletionRequested.emit(self.image_path)
            self.accept()  # Close the dialog
    
    @staticmethod
    def show_detection_view(parent, image_path, detections, title="Detection Details", timestamp="", class_names=None, colors=None):
        '''
        Static method to show dialog in view mode
        Returns: None (just for viewing)
        '''
        dialog = DetectionDialog(
            parent=parent,
            image_path=image_path,
            detections=detections,
            title=title,
            timestamp=timestamp,
            class_names=class_names,
            colors=colors,
            mode="view"
        )
        # Track whether deletion was requested
        deleted_path = [None]  # Use list to allow modification from inner function
        
        # Connect deletion signal to capture the path
        def on_deletion_requested(path):
            deleted_path[0] = path

        dialog.deletionRequested.connect(on_deletion_requested)
        dialog.exec_()

        return deleted_path[0]
    
    @staticmethod
    def show_detection_confirmation(parent, image_path, detections, title="Detection Results", class_names=None, colors=None):
        '''
        Static method to show dialog in confirmation mode
        Returns: bool (True=save, False=discard)
        '''
        dialog = DetectionDialog(
            parent=parent,
            image_path=image_path,
            detections=detections,
            title=title,
            class_names=class_names,
            colors=colors,
            mode="confirm"
        )
        dialog.exec_()
        return dialog.result
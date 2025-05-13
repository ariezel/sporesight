from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from camera import CameraThread 
from card import *
from detection import DetectionManager
from resources import *
from ui.app_ui import Ui_MainWindow
import cv2
import time

from processing import YoloDetector

output_path = "./test/output/0003.jpg"

class MainWindow(QMainWindow):

    def __init__(self, stream_url="0"):
        super().__init__() 

        # Initialize class attributes
        self.title = "SporeSight"
        self.model_name = None
        self.class_names = None
        self.image_path = ""
        self.stream_url = stream_url
        self.camera_thread = None
        self.detector = None
        self.detection_manager = DetectionManager()
        self.colors = COLORS
        self.conf_threshold = "0.25"
        self.temp_image_path = "./temp_capture.jpg"
        self.result_temp_path = "./temp_result.jpg"

        ''' Initialize UI and its elements '''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window properties
        self.setWindowTitle(self.title)
        self.setWindowIcon(QPixmap(SS_LOGO))
        self.setMinimumSize(1420, 780) 
        
        self.setup_ui_elements()
        self.init_menu(MENU)
        self.init_content_pages(MENU)
        self.init_signal_slots()
    
    ''' Customize UI '''
    def setup_ui_elements(self):
        # App title and icon
        self.ui.app_title.setText("SporeSight")
        self.ui.app_icon.setPixmap(QPixmap(LOGO_ICON))
        self.ui.app_icon.setScaledContents(True)
        
        # Menu settings
        self.ui.maximizedmenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.minimizedmenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.minimizedmenu.hide()
        
        # Menu button
        self.ui.menu_btn.setText("")
        self.ui.menu_btn.setIcon(QPixmap(MENU_CLOSE_ICON))
        self.ui.menu_btn.setIconSize(QSize(20, 20))
        self.ui.menu_btn.setCheckable(True)
        self.ui.menu_btn.setChecked(False)
        self.ui.menu_btn.setCursor(Qt.PointingHandCursor)

    ''' Initialize Signals and Slots '''
    def init_signal_slots(self):
        # Menu toggle connections
        self.ui.menu_btn.toggled["bool"].connect(self.ui.maximizedmenu.setHidden)
        self.ui.menu_btn.toggled["bool"].connect(self.ui.app_title.setHidden)
        self.ui.menu_btn.toggled["bool"].connect(self.ui.app_icon.setHidden)
        self.ui.menu_btn.toggled["bool"].connect(self.ui.minimizedmenu.setVisible)
        self.ui.menu_btn.toggled.connect(self.update_menu_icons)

        # Menu selection connections
        self.ui.maximizedmenu.currentRowChanged["int"].connect(self.ui.pages.setCurrentIndex)
        self.ui.minimizedmenu.currentRowChanged["int"].connect(self.ui.pages.setCurrentIndex)
        self.ui.maximizedmenu.currentRowChanged["int"].connect(self.ui.minimizedmenu.setCurrentRow)
        self.ui.minimizedmenu.currentRowChanged["int"].connect(self.ui.maximizedmenu.setCurrentRow)

        # Update menu icons when selection changes
        self.ui.maximizedmenu.currentRowChanged.connect(self.update_menu_icons)
        self.ui.minimizedmenu.currentRowChanged.connect(self.update_menu_icons)

        # Configuration page connections
        self.ui.config_camera_btn.clicked.connect(self.open_model_file)
        self.ui.config_classes_btn.clicked.connect(self.open_class_file)
        self.ui.config_cfscore_btn_add.clicked.connect(self.increment_confidence)
        self.ui.config_cfscore_btn_sub.clicked.connect(self.decrement_confidence)
        self.ui.config_cfscore_lineedit.textChanged.connect(self.update_confidence_from_text)

        # Feed page connections
        self.ui.feed_detect_btn.clicked.connect(self.on_detect_clicked)
        self.ui.feed_stop_btn.clicked.connect(self.toggle_camera_feed)
    
    ''' Change icon of selected menu item '''
    def update_menu_icons(self, index):
        for i in range(self.ui.maximizedmenu.count()):
            icon = MENU[i]["selected_icon"] if i == index else MENU[i]["default_icon"]
            self.ui.maximizedmenu.item(i).setIcon(QPixmap(icon))
            self.ui.minimizedmenu.item(i).setIcon(QPixmap(icon))

    ''' Change icon buttons according to status '''
    def button_icon_change(self, status):
        if status:
            self.menu_btn.setIcon(QPixmap(MENU_OPEN_ICON))
        else:
            self.menu_btn.setIcon(QPixmap(MENU_CLOSE_ICON))
    
    ''' Initialize side menu '''
    def init_menu(self, menu_list):
        self.ui.maximizedmenu.clear()
        self.ui.minimizedmenu.clear()
        
        for option in menu_list:
            # Add item to minimized menu (icon only)
            min_item = QListWidgetItem()
            min_item.setIcon(QPixmap(option.get("default_icon")))
            self.ui.minimizedmenu.addItem(min_item)
            
            # Add item to maximized menu (icon + text)
            max_item = QListWidgetItem()
            max_item.setIcon(QPixmap(option.get("default_icon")))
            max_item.setText(option.get("name"))
            self.ui.maximizedmenu.addItem(max_item)
        
        # Set initial selection
        self.ui.maximizedmenu.setCurrentRow(0)
        self.ui.minimizedmenu.setCurrentRow(0)

    ''' Initialize stack widget with content page '''
    def init_content_pages(self, menu_list):
        # Clear existing widgets
        self.clear_stacked_widget()

        for option in menu_list:
            page_name = option.get("name").strip()
            
            if page_name == "Camera View":
                self.init_camera_page(option)
            elif page_name == "Analytics":
                self.init_analytics_page(option)
            elif page_name == "About":
                self.init_about_page(option)
            elif page_name == "Configuration":
                self.init_config_page(option)
            else:
                self.add_default_page(option)
    
    ''' Remove all widgets from the stacked widget '''
    def clear_stacked_widget(self):
        widget_list = self.ui.pages.findChildren(QWidget)
        for widget in widget_list:
            self.ui.pages.removeWidget(widget)

    ''' Edit Config UI '''
    def init_config_page(self, option):
        self.ui.config_title.setText(option.get("name"))
        self.ui.config_desc.setText(option.get("description"))
        self.ui.config_desc.setWordWrap(True)
            
        # Set frame style
        self.ui.config_body_desc.setFrameShape(QFrame.StyledPanel)
        self.ui.config_body_desc.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.config_body_desc.setGraphicsEffect(shadow)

        self.ui.config_body_files.setFrameShape(QFrame.StyledPanel)
        self.ui.config_body_files.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.config_body_files.setGraphicsEffect(shadow)

        # Show current configuration
        self.ui.config_curr_classfile.setText("<b>Current Class File: </b>")
        self.ui.config_curr_model.setText("<b>Current Model File: </b>")
        self.ui.class_label.setText("<b>Classes: </b>")
        self.ui.classfile.setText("Select a text file containing class names <i>(e.g. classes.txt)</i>")
        self.ui.model_name.setText("Select an ONNX model file <i>(e.g. yolov5.onnx)</i>")
        self.ui.class_list.setText("<i>None</i>")

        # Model configuration section
        self.ui.config_camera_label.setText('ONNX Model Path')
        self.ui.config_camera_lineedit.setText("Select an ONNX model file (e.g. yolov5.onnx)")
        self.ui.config_camera_lineedit.setReadOnly(True)
        self.ui.config_camera_btn.setText('Browse')
        self.ui.config_camera_btn.setCursor(Qt.PointingHandCursor)

        # Classes configuration
        self.ui.config_classes_label.setText('Classes.txt Path')
        self.ui.config_classes_lineedit.setText("Select a text file containing class names (e.g. classes.txt)")
        self.ui.config_classes_lineedit.setReadOnly(True)
        self.ui.config_classes_btn.setText('Browse')
        self.ui.config_classes_btn.setCursor(Qt.PointingHandCursor)

        # Confidence Score configuration section
        self.ui.config_cfscore_label.setText('Confidence Score')
        self.ui.config_cfscore_lineedit.setText(self.conf_threshold)
        self.ui.config_cfscore_lineedit.setAlignment(Qt.AlignCenter) 
        self.ui.config_cfscore_lineedit.setReadOnly(True)
        self.ui.config_cfscore_btn_add.setText('+')
        self.ui.config_cfscore_btn_add.setCursor(Qt.PointingHandCursor)
        self.ui.config_cfscore_btn_sub.setText('-')
        self.ui.config_cfscore_btn_sub.setCursor(Qt.PointingHandCursor)

        # Add config page to stacked widget
        self.ui.pages.addWidget(self.ui.config_section_frame)   # Initialize the UI class
    
    '''Open file dialog to select ONNX model file'''
    def open_model_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select ONNX Model File", "", "ONNX Files (*.onnx);;All Files (*)", options=options)
        
        if file_name:
            base_name = os.path.basename(file_name)
            self.ui.model_name.setText(base_name)
            self.ui.config_camera_lineedit.setText(file_name)
            self.model_name = file_name

    '''Open file dialog to select class file'''
    def open_class_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select text file containing classes", "", "TXT Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            base_name = os.path.basename(file_name)
            self.ui.classfile.setText(base_name)
            self.ui.config_classes_lineedit.setText(file_name)
            self.class_names = self.load_class_names(file_name)

    '''Open file dialog to select image file'''
    def open_image_file(self):
        try:
            if self.model_name is None or self.class_names is None:
                    raise ValueError("Model and class names must be set before processing an image.")
        except ValueError as e:
            QMessageBox.critical(self, "Configuration Error", str(e))
            return
        
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.jpg *.jpeg *.png);;All Files (*)", options=options)

        if file_name:
            try:
                QApplication.setOverrideCursor(Qt.WaitCursor)
                self.image_path = file_name
                print(f'CLASS NAMES: {self.class_names}')
                self.detector = YoloDetector(self.model_name, self.conf_threshold, self.class_names)
                result_image, detections = self.detector.process_image(self.image_path)
                # Save the result image to temporary file first
                cv2.imwrite(self.result_temp_path, result_image)
                QApplication.restoreOverrideCursor()  # Restore cursor before dialog
                save_confirmed = self.show_detection_confirmation_dialog(self.result_temp_path, detections)

                if save_confirmed:
                    image_path = self.save_detection_results(result_image, detections)
                    self.update_analytics_page()
                    QMessageBox.information(self, "Detection Saved", f"Detection has been saved successfully.")
                    print(f"Detection saved to: {image_path}")
            except Exception as e:
                print(f"Error processing image: {str(e)}")
                QMessageBox.critical(self, "Processing Error", f"An error occurred: {str(e)}")
            finally:
                # Make sure cursor is restored even if there was an error
                if QApplication.overrideCursor():
                    QApplication.restoreOverrideCursor()
            QApplication.restoreOverrideCursor()

    ''' Edit Feed UI '''
    def init_camera_page(self, option):
        # Set page title and description
        self.ui.feed_title.setText(option.get("name"))
            
        # Set frame style
        self.ui.feed_results.setText(CAMERA_DESCRIPTION)
        self.ui.feed_results.setWordWrap(True)  
        self.ui.results_desc_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.results_desc_frame.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.results_desc_frame.setGraphicsEffect(shadow)

        self.ui.feed_classes_content.setText(CAMERA_DESCRIPTION)
        self.ui.feed_classes_content.setWordWrap(True)  
        self.ui.feed_classes_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.feed_classes_frame.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.feed_classes_frame.setGraphicsEffect(shadow)

        # Setup camera controls
        self.ui.feed_detect_btn.setText("Detect")
        self.ui.feed_stop_btn.setText("Start Feed")
        self.ui.feed_detect_btn.setCursor(Qt.PointingHandCursor)
        self.ui.feed_stop_btn.setCursor(Qt.PointingHandCursor)

        self.ui.feed_progressbar.setVisible(False)
        self.ui.feed_progressbar.setStyleSheet(DEFAULT_STYLE)
        
        # Set tooltips
        self.ui.feed_detect_btn.setToolTip("Start the detection process on the live feed")
        self.ui.feed_stop_btn.setToolTip("Toggle the camera feed")
        self.ui.feed_title.setToolTip("This section displays the live camera feed")
        
        # Set initial button styles
        self.feed_stop_active = True  # Track if feed should be stopped
        self.ui.feed_detect_btn.setStyleSheet(DEFAULT_STYLE)
        self.ui.feed_stop_btn.setStyleSheet(COMPLETED_STYLE)
        
        # Initialize camera thread
        self.init_camera_thread()
        
        # Add feed page to stacked widget
        self.ui.pages.addWidget(self.ui.feed_section_frame)

    ''' Initialize the camera thread for video streaming '''
    def init_camera_thread(self):
        if not self.camera_thread:
            self.camera_thread = CameraThread(self.stream_url)
            self.camera_thread.imageUpdate.connect(self.update_camera_image)

    ''' Toggle camera feed on/off '''
    @Slot()
    def toggle_camera_feed(self):
        self.feed_stop_active = not self.feed_stop_active
        if self.feed_stop_active:
            if self.camera_thread and self.camera_thread.isRunning():
                self.camera_thread.stop()
            self.ui.feed_stop_btn.setText("Start Feed")
            self.ui.feed_stop_btn.setStyleSheet(COMPLETED_STYLE)
        else:
            if not self.camera_thread:
                self.init_camera_thread()
            self.camera_thread.start()
            self.ui.feed_stop_btn.setText("Stop Feed")
            self.ui.feed_stop_btn.setStyleSheet(DEFAULT_STYLE)
    
    '''Update the camera feed image'''
    @Slot(object)
    def update_camera_image(self, img):
        scaled_img = img.scaled(
            self.ui.feed_label.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        self.ui.feed_label.setPixmap(QPixmap.fromImage(scaled_img))
    
    ''' Process detection on the current frame '''
    def on_detect_clicked(self):
        try:
            # Check if detector is initialized
            if not self.detector:
                self.detector = YoloDetector(self.model_name, self.conf_threshold, self.class_names)
                # Get class names from detector if available
                if hasattr(self.detector, 'get_class_names'):
                    self.class_names = self.detector.get_class_names()
            
            # Check if camera thread is running
            if not self.camera_thread or not self.camera_thread.isRunning():
                QMessageBox.warning(self, "Camera Error", "Please start the camera feed first before detecting.")
                return
            
            # Show loading indicator - start
            self.ui.feed_detect_btn.setEnabled(False) 
            self.ui.feed_detect_btn.setText("Processing...")
            QApplication.setOverrideCursor(Qt.WaitCursor)  
            self.ui.feed_progressbar.setValue(0)  
            self.ui.feed_progressbar.setVisible(True)
            QApplication.processEvents() 
            
            self.camera_thread.CameraThreadActive = False
            
            # Update UI to reflect paused state
            if not self.feed_stop_active:
                self.feed_stop_active = True
                self.ui.feed_stop_btn.setText("Start Feed")
                self.ui.feed_stop_btn.setStyleSheet(COMPLETED_STYLE)
           
            # Save the captured frame to a temporary file
            cv2.imwrite(self.temp_image_path, self.camera_thread.get_frame())
            
            self.ui.feed_progressbar.setValue(30)
            QApplication.processEvents()
            
            # Verify file was saved
            if not os.path.exists(self.temp_image_path):
                QMessageBox.warning(self, "File Error", "Could not save temporary image.")
                return
            
            # Log for debugging
            print(f"Processing image: {os.path.abspath(self.temp_image_path)}")
            
            # Process the image
            
            result_image, detections = self.detector.process_image(self.temp_image_path)
        
            if not detections:
                print("No detections found.")
            
            # Update progress
            self.ui.feed_progressbar.setValue(80)
            QApplication.processEvents()
            
            # Save result image to temporary file
            cv2.imwrite(self.result_temp_path, result_image)
            
            # Verify result file exists
            if not os.path.exists(self.result_temp_path):
                print("Warning: Could not save result image")

            self.ui.feed_progressbar.setValue(100)
            QApplication.setOverrideCursor(Qt.ArrowCursor)  
            save_confirmed = self.show_detection_confirmation_dialog(self.result_temp_path, detections)
            
            if save_confirmed:
                image_path = self.save_detection_results(result_image, detections)
                self.update_analytics_page()
                QMessageBox.information(self, "Detection Saved", f"Detection has been saved successfully.")
                print(f"Detection saved to: {image_path}")
            
            QApplication.setOverrideCursor(Qt.ArrowCursor)  
            
        except Exception as e:
            print(f"Detection error: {str(e)}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "Detection Error", f"An error occurred: {str(e)}")
        
        finally:
            self.ui.feed_detect_btn.setEnabled(True)
            self.ui.feed_detect_btn.setText("Detect")
            QApplication.restoreOverrideCursor() 
            QTimer.singleShot(1500, lambda: self.ui.feed_progressbar.setVisible(False))
            try:
                for temp_file in [self.temp_image_path, self.result_temp_path]:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
            except Exception as e:
                print(f"Error removing temporary files: {str(e)}")

    ''' Save detection results and update history '''
    def save_detection_results(self, image, detection_details):
        timestamp = int(time.time())
        image_path, _ = self.detection_manager.save_detection(
            image, detection_details, timestamp
        )
        return image_path
    
    ''' Initialize Analytics UI with menu options for managing detection images '''
    def init_analytics_page(self, option):
        self.ui.analytics_title.setText(option.get("name"))
        
        # Make sure analytics section has a layout
        if self.ui.analytics_section_frame.layout() is None:
            layout = QVBoxLayout(self.ui.analytics_section_frame)
            self.ui.analytics_section_frame.setLayout(layout)
        
        # Add to stacked widget
        self.ui.pages.addWidget(self.ui.analytics_section_frame)
        
        # Load detection data
        self.update_analytics_page()

    ''' Update the analytics page with current detection data '''
    def update_analytics_page(self):
        # Clear existing content
        self.clear_analytics_content()
        
        # Get detection dates
        dates = self.detection_manager.get_detection_dates()
        
        # Create toolbar with date filter - pass "All Dates" as current selection
        toolbar = self.create_analytics_toolbar(dates, current_selection="All Dates")
        self.ui.analytics_body_content.layout().addWidget(toolbar)
        
        # Create scrollable area for detection cards
        scroll_area = self.create_detection_cards_area()
        self.ui.analytics_body_content.layout().addWidget(scroll_area)
        
        # Update analytics title with detection count
        all_detections = self.detection_manager.get_all_detections()
        total_detections = sum(len(details) for _, details in all_detections)
        self.ui.analytics_title.setText(
            f"     Analytics - {total_detections} Detection{'s' if total_detections != 1 else ''}"
        )

        # Force layout update
        self.ui.analytics_body_content.layout().update()
        QApplication.processEvents()

    def find_date_filter(self):
        for i in range(self.ui.analytics_body_content.layout().count()):
            item = self.ui.analytics_body_content.layout().itemAt(i)
            if item and item.widget():
                # Check if this is the toolbar widget
                toolbar = item.widget()
                # Look for QComboBox in toolbar children
                combo_boxes = toolbar.findChildren(QComboBox)
                if combo_boxes:
                    return combo_boxes[0]
        return None

    ''' Clear all widgets from analytics content area '''
    def clear_analytics_content(self):
        while self.ui.analytics_body_content.layout().count():
            item = self.ui.analytics_body_content.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    ''' Create toolbar with date filter for analytics page '''
    def create_analytics_toolbar(self, dates, current_selection=None):
        # Create container widget
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar.setStyleSheet("margin-bottom: 10px;")
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add date filter label
        filter_label = QLabel("Filter by date:")
        filter_label.setStyleSheet('''
            color: #2C3E50;
            font-weight: 600;
            font-size: 16px;
            margin-right: 5px;
            margin-left: 5px;
        ''')
        toolbar_layout.addWidget(filter_label)
        
        # Add date filter dropdown
        date_filter = QComboBox()
        date_filter.addItem("All Dates")
        for date in dates:
            date_filter.addItem(date)
            
        # Set the current selection if provided
        if current_selection:
            index = date_filter.findText(current_selection)
            if index >= 0:
                date_filter.setCurrentIndex(index)
                
        date_filter.setStyleSheet('''
            QComboBox {
                background-color: white;
                border: 1px solid #CCC;
                border-radius: 3px;
                padding: 3px 8px;
                min-width: 120px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #CCC;
                font-size: 14px;
            }
        ''')
        toolbar_layout.addWidget(date_filter)
        
        # Add spacer
        toolbar_layout.addStretch()

        # Add delete all button
        detect_img_btn = QPushButton("Detect an image")
        detect_img_btn.setStyleSheet('''
            QPushButton {
                background-color: #210F37;
                text-align: center;
                border-radius: 14px;
                color: white;
                font-weight: 700;
                padding: 11px 20px;
                font-size: 14px;
                width: 110px;
            }
            QPushButton:hover {
                border-color: #4F1C51;
                background-color: #4F1C51;
            }
        ''')
        detect_img_btn.setCursor(Qt.PointingHandCursor)
        detect_img_btn.clicked.connect(self.open_image_file)  # Connect to the method to open image file

        toolbar_layout.addWidget(detect_img_btn)
        
        # Block signals temporarily to prevent recursive filtering
        date_filter.blockSignals(True)
        date_filter.setCurrentText(current_selection if current_selection else "All Dates")
        date_filter.blockSignals(False)
        
        # Connect date filter change event
        date_filter.currentIndexChanged.connect(
            lambda idx: self.filter_detections_by_date(date_filter.currentText())
        )
        
        return toolbar
    
    ''' Filter detection cards by date '''
    def filter_detections_by_date(self, date):

        # Re-create cards area with filtered data
        self.clear_analytics_content()
        
        # Get all available dates
        all_dates = self.detection_manager.get_detection_dates()
        
        # Recreate toolbar with the current date selected
        toolbar = self.create_analytics_toolbar(all_dates, current_selection=date)
        self.ui.analytics_body_content.layout().addWidget(toolbar)
        
        # Create new scroll area with filtered data
        if date == "All Dates":
            scroll_area = self.create_detection_cards_area()
        else:
            # Check if the folder is empty after filtering
            detections = self.detection_manager.get_detections_by_date(date)
            if not detections:
                # If no detections for this date, remove the empty folder
                folder_path = self.detection_manager.get_date_folder_path(date)
                if folder_path and os.path.exists(folder_path) and not os.listdir(folder_path):
                    try:
                        os.rmdir(folder_path)
                        QTimer.singleShot(100, lambda: self.update_analytics_page())
                        return  # Early return as we're going to refresh the page
                    except Exception as e:
                        print(f"Error removing empty folder: {str(e)}")
            
            scroll_area = self.create_detection_cards_area(date)
        
        self.ui.analytics_body_content.layout().addWidget(scroll_area)
    
    ''' Create scrollable area with detection cards '''
    def create_detection_cards_area(self, date=None):
        """
        Create scrollable area with detection cards
        
        Args:
            date (str, optional): If provided, only show detections from this date
        
        Returns:
            QScrollArea: Scrollable area containing detection cards
        """
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background: transparent; border: none;")
        
        # Create container for cards
        cards_container = QWidget()
        cards_container.setStyleSheet("background: transparent;")
        cards_layout = QGridLayout(cards_container)
        cards_layout.setSpacing(15)
        
        # Get detections based on whether a date was provided
        try:
            if date is None:
                detections = self.detection_manager.get_all_detections()
                no_detections_message = "No detections found"
            else:
                detections = self.detection_manager.get_detections_by_date(date)
                no_detections_message = f"No detections found for {date}"
            
            # Add detection cards
            if detections:
                for i, (image_path, detection_details) in enumerate(detections):
                    # Verify that the image file still exists
                    if not os.path.exists(image_path):
                        print(f"Warning: Image file not found: {image_path}")
                        continue
                        
                    # Calculate grid position - 3 cards per row
                    row = i // 3
                    col = i % 3
                    
                    # Create card
                    try:
                        card = DetectionCard(image_path, detection_details, self.class_names, parent=cards_container)
                        
                        # Add to layout
                        cards_layout.addWidget(card, row, col, Qt.AlignLeft | Qt.AlignTop)
                    except Exception as e:
                        print(f"Error creating detection card: {str(e)}")
                        import traceback
                        traceback.print_exc()
                    
                # Add stretch to prevent cards from expanding
                cards_layout.setColumnStretch(3, 1)
            else:
                # Show "no detections" message
                no_detections = QLabel(no_detections_message)
                no_detections.setAlignment(Qt.AlignCenter)
                no_detections.setStyleSheet("font-size: 16px; color: #666; padding: 40px;")
                cards_layout.addWidget(no_detections, 0, 0, 1, 3)
        except Exception as e:
            # Handle any errors gracefully
            error_label = QLabel(f"Error loading detections: {str(e)}")
            error_label.setAlignment(Qt.AlignCenter)
            error_label.setStyleSheet("font-size: 16px; color: #f00; padding: 40px;")
            cards_layout.addWidget(error_label, 0, 0, 1, 3)
            import traceback
            traceback.print_exc()
        
        # Set container as scroll area widget
        scroll_area.setWidget(cards_container)
        
        return scroll_area
    
    ''' Remove a card from the UI after its files have been deleted '''
    def remove_detection_card(self, card):
        """
        Parameters:
        - card: DetectionCard instance to be removed
        """
        parent_container = card.parent()
        if parent_container:
            parent_layout = parent_container.layout()
            if parent_layout:
                for i in range(parent_layout.count()):
                    item = parent_layout.itemAt(i)
                    if item and item.widget() == card:
                        parent_layout.removeItem(item)
                        break
            card.setParent(None)
        else:
            print("Warning: Could not find parent container for card")
        
    ''' About Page '''
    def init_about_page(self, option):
        '''Initialize the about page'''
        self.ui.about_title.setText(option.get("name"))
        
        # Set team information
        self.set_about_team_info()

        # Set frame style
        self.ui.about_ics_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.about_ics_frame.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.about_ics_frame.setGraphicsEffect(shadow)

        self.ui.about_ipb_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.about_ipb_frame.setFrameShadow(QFrame.Raised)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 10))  # semi-transparent black
        self.ui.about_ipb_frame.setGraphicsEffect(shadow)

        self.ui.ics_logo_label.setPixmap(QPixmap(ICS_LOGO))
        self.ui.ics_logo_label.setScaledContents(True)
        self.ui.ipb_logo_label.setPixmap(QPixmap(IPB_LOGO))
        self.ui.ipb_logo_label.setScaledContents(True)

        
        # Add to stacked widget
        self.ui.pages.addWidget(self.ui.about_section_frame)

    ''' Set team information on about page '''
    def set_about_team_info(self):
        # ICS team information
        self.ui.ics_adviser_name.setText(ABOUT[0].get("name"))
        self.ui.ics_adviser_designation.setText(ABOUT[0].get("designation"))
        self.ui.ics_student_name.setText(ABOUT[1].get("name"))
        self.ui.ics_student_designation.setText(ABOUT[1].get("designation"))
        
        # IPB team information
        self.ui.ipb_adviser_name.setText(ABOUT[2].get("name"))
        self.ui.ipb_adviser_designation.setText(ABOUT[2].get("designation"))
        self.ui.ipb_student_name.setText(ABOUT[3].get("name"))
        self.ui.ipb_student_designation.setText(ABOUT[3].get("designation"))

    ''' Default UI '''            
    def add_default_page(self, option):
        '''Add a default page for menu items without special handling'''
        text = option.get("name")
        page = QWidget()
        layout = QGridLayout(page)
        
        label = QLabel(text=text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font = QFont()
        font.setPixelSize(30)
        label.setFont(font)
        
        layout.addWidget(label)
        self.ui.pages.addWidget(page)
    
    ''' Dialog for detection confirmation '''
    def show_detection_confirmation_dialog(self, image_path, detections):
        """
        Show a dialog with the detected image and ask the user if they want to save it.

        Args:
            image_path: Path to the image file
            detections: List of tuples (class_name, confidence, box)
            
        Returns:
            bool: True if user confirms save, False otherwise
        """
        try:
            # Ensure image path exists
            if not os.path.exists(image_path):
                print(f"Warning: Image file {image_path} not found")
                return False
            
            # Use empty list if no class names are available
            class_names = self.class_names
            
            # Make sure colors is available
            colors = self.colors if hasattr(self, 'colors') and self.colors else None
            
            # Import at the top level of the function
            from card import DetectionDialog
            
            if detections is None:
                detections = []
            
            result = DetectionDialog.show_detection_confirmation(
                parent=self,
                image_path=image_path,
                detections=detections,
                title="Detection Results",
                class_names=class_names,
                colors=colors
            )
            return result

        except Exception as e:
            print(f"Error showing confirmation dialog: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

    ''' Helper method to handle dialog button clicks '''
    def handle_dialog_result(self, dialog, result_list, value):
        result_list[0] = value
        dialog.accept()
    
    ''' Handle application closing '''
    def closeEvent(self, event):
        print("Application closing...")
        if self.camera_thread and self.camera_thread.isRunning():
            print("Stopping camera thread...")
            self.camera_thread.stop()
            
            # Don't wait for the thread indefinitely
            if not self.camera_thread.wait(2000):  # Wait up to 1 second
                print("Camera thread did not finish in time, forcing termination")
                self.camera_thread.terminate()
                self.camera_thread.wait()  # Wait for it to finish terminating
        print("Cleanup done, accepting close event")
        event.accept()

    ''' Increment confidence threshold '''
    def increment_confidence(self):
        try:
            current = float(self.conf_threshold)
            # Increment by 0.05, but don't exceed 1.0
            new_value = min(1.0, current + 0.05)
            self.conf_threshold = f"{new_value:.2f}"
            self.ui.config_cfscore_lineedit.setText(self.conf_threshold)
        except ValueError:
            print("Invalid confidence value")
    
    ''' Decrement confidence threshold '''
    def decrement_confidence(self):
        try:
            current = float(self.conf_threshold)
            # Decrement by 0.05, but don't go below 0.05
            new_value = max(0.05, current - 0.05)
            self.conf_threshold = f"{new_value:.2f}"
            self.ui.config_cfscore_lineedit.setText(self.conf_threshold)
        except ValueError:
            print("Invalid confidence value")
    
    ''' Update confidence threshold from text input '''
    def update_confidence_from_text(self, text):
        try:
            # Validate input is a number between 0 and 1
            value = float(text)
            if 0 <= value <= 1:
                self.conf_threshold = f"{value:.2f}"
                print(f"Confidence threshold updated to: {self.conf_threshold}")
            else:
                print(f"Confidence value {value} out of range (0-1)")
        except ValueError:
            # If not a valid float, don't update the threshold
            print(f"Invalid confidence value: {text}")

    ''' Load class names from file '''
    def load_class_names(self, classfile_path):
        default_class_names = ["unknown"]
        try:
            class_names_file = classfile_path
            with open(class_names_file, 'r') as f:
                class_names = [line.strip() for line in f.readlines()]
            if not class_names:
                print(f"Warning: Class names file is empty. Using default class names.")
                return default_class_names
            return class_names
            
        except FileNotFoundError:
            print(f"Warning: Class names file not found. Using default class names.")
            return default_class_names
        except Exception as e:
            print(f"Error loading class names: {str(e)}. Using default class names.")
            return default_class_names



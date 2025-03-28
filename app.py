from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from torch import Size
from camera import CameraThread  # Import CameraThread
from resources import *
from ui.app_ui import Ui_MainWindow

from PySide6.QtCore import *

class MainWindow(QMainWindow):
    
    title = "SporeSight"

    def __init__(self):
        super().__init__() 

        self.setWindowTitle(self.title)
        self.setWindowIcon(QPixmap(LOGO_ICON_SELECTED))

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        ''' Initialize UI and its elements '''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app_title = self.ui.app_title
        self.app_icon = self.ui.app_icon
        self.maximizedmenu = self.ui.maximizedmenu
        self.minimizedmenu = self.ui.minimizedmenu
        self.menu_btn = self.ui.menu_btn
        self.main_content = self.ui.pages # Stacked widget

        ''' Customize UI '''

        # App title and icon
        self.app_title.setText("SporeSight")
        self.app_icon.setPixmap(QPixmap(LOGO_ICON))
        self.app_icon.setScaledContents(True)

        # Menu
        self.maximizedmenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.minimizedmenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.minimizedmenu.hide()

        # Menu button
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QPixmap(MENU_CLOSE_ICON))
        self.menu_btn.setIconSize(QSize(20, 20))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)
        self.menu_btn.setCursor(Qt.PointingHandCursor)

        ''' Name has 5 spaces at the beginning due to UI issues '''
        ''' List is located at the resources.py file '''
        self.menu_list = MENU
        
        ''' Initialize UI slots '''
        self.init_list_widget(self.menu_list)
        self.init_stackedwidget(self.menu_list)
        self.init_signal_slot()

    ''' Function for pressing the mouse within the window '''
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    ''' Function for dragging window '''
    def mouseMoveEvent(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

    ''' Initialize Signals and Slots '''
    def init_signal_slot(self):
        # Connect signal and slots for the menu button and side menu
        self.menu_btn.toggled["bool"].connect(self.maximizedmenu.setHidden)
        self.menu_btn.toggled["bool"].connect(self.app_title.setHidden)
        self.menu_btn.toggled["bool"].connect(self.app_icon.setHidden)
        self.menu_btn.toggled["bool"].connect(self.minimizedmenu.setVisible)
        self.menu_btn.toggled.connect(self.button_icon_change)

        # Connect signal and slots for switching between items
        self.maximizedmenu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.minimizedmenu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.maximizedmenu.currentRowChanged["int"].connect(self.minimizedmenu.setCurrentRow)
        self.minimizedmenu.currentRowChanged["int"].connect(self.maximizedmenu.setCurrentRow)

        # Update menu icons when an item is clicked
        self.maximizedmenu.currentRowChanged.connect(self.update_menu_icons)
        self.minimizedmenu.currentRowChanged.connect(self.update_menu_icons)
    
    ''' Change icon of selected menu item '''
    def update_menu_icons(self, index):
        for i in range(self.maximizedmenu.count()):
            if i == index:
                # Set selected icon
                self.maximizedmenu.item(i).setIcon(QPixmap(self.menu_list[i]["selected_icon"]))
                self.minimizedmenu.item(i).setIcon(QPixmap(self.menu_list[i]["selected_icon"]))
            else:
                # Set default icon
                self.maximizedmenu.item(i).setIcon(QPixmap(self.menu_list[i]["default_icon"]))
                self.minimizedmenu.item(i).setIcon(QPixmap(self.menu_list[i]["default_icon"]))

    ''' Change icon buttons according to status '''
    def button_icon_change(self, status):
        if status:
            self.menu_btn.setIcon(QPixmap(MENU_OPEN_ICON))
        else:
            self.menu_btn.setIcon(QPixmap(MENU_CLOSE_ICON))
    
    ''' Initialize side menu '''
    def init_list_widget(self, menu_list):
        self.maximizedmenu.clear()
        self.minimizedmenu.clear()

        for option in menu_list:
            # Set items for the minimized menu only
            item = QListWidgetItem()
            item.setIcon(QPixmap(option.get("default_icon")))
            self.minimizedmenu.addItem(item)
            self.minimizedmenu.setCurrentRow(0)

            # Set items for maximized menu
            item2 = QListWidgetItem()
            item2.setIcon(QPixmap(option.get("default_icon")))
            item2.setText(option.get("name"))
            self.maximizedmenu.addItem(item2)
            self.maximizedmenu.setCurrentRow

    ''' Initialize stack widget with content page '''
    def init_stackedwidget(self, menu_list):
        widget_list = self.main_content.findChildren(QWidget)
        
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        for option in menu_list:
            text = option.get("name").strip()  # Remove spaces

            if text == "YOLO Configuration": self.init_config_ui(option)
            elif text == "Camera View": self.init_feed_ui(option)

            else:
                text = option.get("name")
                layout = QGridLayout()
                label = QLabel(text=text)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                font = QFont()
                font.setPixelSize(30)

                label.setFont(font)
                layout.addWidget(label)
                new_page = QWidget()
                new_page.setLayout(layout)
                self.main_content.addWidget(new_page)

    ''' Edit Config UI '''
    def init_config_ui(self, option):
        
        self.config_title = self.ui.config_title
        self.config_desc = self.ui.config_desc

        self.config_title.setText(option.get("name"))
        self.config_desc.setText(option.get("description"))
        self.config_desc.setWordWrap(True)

        self.config_ui = self.ui.config_section_frame  # Initialize the UI class
        self.main_content.addWidget(self.config_ui)

    ''' Edit Feed UI '''
    def init_feed_ui(self, option):
            
        self.feed_title = self.ui.feed_title
        self.feed_desc = self.ui.feed_desc
        self.feed_ui = self.ui.feed_section_frame  # Initialize the UI class

        self.feed_title.setText(option.get("name"))
        self.feed_desc.setText(option.get("description"))

        self.feed_label = self.ui.feed_label
        # self.feed_label.setFixedSize(640, 480)  

        ''' Call the Camera Thread '''
        self.CameraThread = CameraThread()
        self.CameraThread.start()  # Start the camera thread
        self.CameraThread.imageUpdate.connect(self.imageUpdateSlot) # Connect the signal for image updates
        
        self.main_content.addWidget(self.feed_ui)

    def imageUpdateSlot(self, img):
        self.feed_label.setPixmap(QPixmap.fromImage(img))

    def cancelFeed(self):
        self.CameraThread.stop()

    
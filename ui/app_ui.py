# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1346, 838)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.config_page = QWidget()
        self.config_page.setObjectName(u"config_page")
        self.config_section_frame = QFrame(self.config_page)
        self.config_section_frame.setObjectName(u"config_section_frame")
        self.config_section_frame.setGeometry(QRect(0, 0, 1021, 841))
        self.config_section_frame.setFrameShape(QFrame.StyledPanel)
        self.config_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.config_section_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.config_title_frame = QFrame(self.config_section_frame)
        self.config_title_frame.setObjectName(u"config_title_frame")
        self.config_title_frame.setMaximumSize(QSize(16777215, 80))
        self.config_title_frame.setFrameShape(QFrame.StyledPanel)
        self.config_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.config_title_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.config_title = QLabel(self.config_title_frame)
        self.config_title.setObjectName(u"config_title")
        self.config_title.setStyleSheet(u"background-color:rgb(44, 20, 74);\n"
"border-radius: 15px;")

        self.horizontalLayout_3.addWidget(self.config_title)


        self.verticalLayout.addWidget(self.config_title_frame)

        self.config_body_frame = QFrame(self.config_section_frame)
        self.config_body_frame.setObjectName(u"config_body_frame")
        self.config_body_frame.setFrameShape(QFrame.StyledPanel)
        self.config_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.config_body_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.config_body_desc = QFrame(self.config_body_frame)
        self.config_body_desc.setObjectName(u"config_body_desc")
        self.config_body_desc.setMaximumSize(QSize(16777215, 60))
        self.config_body_desc.setFrameShape(QFrame.StyledPanel)
        self.config_body_desc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.config_body_desc)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.config_desc = QLabel(self.config_body_desc)
        self.config_desc.setObjectName(u"config_desc")
        self.config_desc.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.config_desc)


        self.verticalLayout_2.addWidget(self.config_body_desc)

        self.config_body_files = QFrame(self.config_body_frame)
        self.config_body_files.setObjectName(u"config_body_files")
        self.config_body_files.setMaximumSize(QSize(16777215, 16777215))
        self.config_body_files.setFrameShape(QFrame.StyledPanel)
        self.config_body_files.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.config_body_files)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cfg_frame = QFrame(self.config_body_files)
        self.cfg_frame.setObjectName(u"cfg_frame")
        self.cfg_frame.setFrameShape(QFrame.NoFrame)
        self.cfg_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.cfg_frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cfg_lbl = QLabel(self.cfg_frame)
        self.cfg_lbl.setObjectName(u"cfg_lbl")
        font = QFont()
        self.cfg_lbl.setFont(font)
        self.cfg_lbl.setStyleSheet(u"font-size: 17px;")

        self.horizontalLayout_10.addWidget(self.cfg_lbl)

        self.cfg_line = QLineEdit(self.cfg_frame)
        self.cfg_line.setObjectName(u"cfg_line")
        self.cfg_line.setFont(font)
        self.cfg_line.setStyleSheet(u"padding: 5px;\n"
"font-size: 15px;\n"
"border: 1px solid rgb(52, 73, 85);\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.cfg_line.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.cfg_line)

        self.cfg_browse_btn = QPushButton(self.cfg_frame)
        self.cfg_browse_btn.setObjectName(u"cfg_browse_btn")
        self.cfg_browse_btn.setFont(font)
        self.cfg_browse_btn.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(52, 73, 85);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 15px;\n"
"	border: none;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	padding: 7px 30px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(74, 101, 114);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(0, 128, 128);\n"
"}\n"
"")
        self.cfg_browse_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout_10.addWidget(self.cfg_browse_btn)


        self.verticalLayout_3.addWidget(self.cfg_frame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.confidence_lbl = QLabel(self.config_body_files)
        self.confidence_lbl.setObjectName(u"confidence_lbl")
        self.confidence_lbl.setFont(font)
        self.confidence_lbl.setStyleSheet(u"font-size: 17px;")
        self.confidence_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.confidence_lbl)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.config_body_files)


        self.verticalLayout.addWidget(self.config_body_frame)

        self.pages.addWidget(self.config_page)
        self.feed_page = QWidget()
        self.feed_page.setObjectName(u"feed_page")
        self.feed_section_frame = QFrame(self.feed_page)
        self.feed_section_frame.setObjectName(u"feed_section_frame")
        self.feed_section_frame.setGeometry(QRect(0, 0, 1021, 841))
        self.feed_section_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.feed_section_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.feed_title_frame = QFrame(self.feed_section_frame)
        self.feed_title_frame.setObjectName(u"feed_title_frame")
        self.feed_title_frame.setMaximumSize(QSize(16777215, 80))
        self.feed_title_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.feed_title_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.feed_title = QLabel(self.feed_title_frame)
        self.feed_title.setObjectName(u"feed_title")
        self.feed_title.setStyleSheet(u"background-color:rgb(44, 20, 74);\n"
"border-radius: 15px;")

        self.horizontalLayout_6.addWidget(self.feed_title)


        self.verticalLayout_8.addWidget(self.feed_title_frame)

        self.feed_body_frame = QFrame(self.feed_section_frame)
        self.feed_body_frame.setObjectName(u"feed_body_frame")
        self.feed_body_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.feed_body_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.feed_camera = QFrame(self.feed_body_frame)
        self.feed_camera.setObjectName(u"feed_camera")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_camera.sizePolicy().hasHeightForWidth())
        self.feed_camera.setSizePolicy(sizePolicy)
        self.feed_camera.setMaximumSize(QSize(16777215, 16777215))
        self.feed_camera.setFrameShape(QFrame.StyledPanel)
        self.feed_camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.feed_camera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.feed_label = QLabel(self.feed_camera)
        self.feed_label.setObjectName(u"feed_label")

        self.verticalLayout_7.addWidget(self.feed_label)


        self.horizontalLayout_2.addWidget(self.feed_camera)

        self.feed_body_desc = QFrame(self.feed_body_frame)
        self.feed_body_desc.setObjectName(u"feed_body_desc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.feed_body_desc.sizePolicy().hasHeightForWidth())
        self.feed_body_desc.setSizePolicy(sizePolicy1)
        self.feed_body_desc.setMaximumSize(QSize(16777215, 16777215))
        self.feed_body_desc.setFrameShape(QFrame.StyledPanel)
        self.feed_body_desc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.feed_body_desc)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.feed_desc_frame = QFrame(self.feed_body_desc)
        self.feed_desc_frame.setObjectName(u"feed_desc_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.feed_desc_frame.sizePolicy().hasHeightForWidth())
        self.feed_desc_frame.setSizePolicy(sizePolicy2)
        self.feed_desc_frame.setMaximumSize(QSize(16777215, 60))
        self.feed_desc_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_desc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.feed_desc_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.feed_desc = QLabel(self.feed_desc_frame)
        self.feed_desc.setObjectName(u"feed_desc")
        self.feed_desc.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_5.addWidget(self.feed_desc)


        self.verticalLayout_5.addWidget(self.feed_desc_frame)

        self.results_desc_frame = QFrame(self.feed_body_desc)
        self.results_desc_frame.setObjectName(u"results_desc_frame")
        self.results_desc_frame.setFrameShape(QFrame.StyledPanel)
        self.results_desc_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.results_desc_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.feed_results = QLabel(self.results_desc_frame)
        self.feed_results.setObjectName(u"feed_results")

        self.verticalLayout_6.addWidget(self.feed_results, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.results_desc_frame)


        self.horizontalLayout_2.addWidget(self.feed_body_desc)


        self.verticalLayout_8.addWidget(self.feed_body_frame)

        self.pages.addWidget(self.feed_page)

        self.gridLayout.addWidget(self.pages, 0, 3, 2, 1)

        self.maximizedmenu = QListWidget(self.centralwidget)
        self.maximizedmenu.setObjectName(u"maximizedmenu")
        self.maximizedmenu.setMinimumSize(QSize(0, 0))
        self.maximizedmenu.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.maximizedmenu, 1, 2, 1, 1)

        self.minimizedmenu = QListWidget(self.centralwidget)
        self.minimizedmenu.setObjectName(u"minimizedmenu")
        self.minimizedmenu.setMinimumSize(QSize(0, 0))
        self.minimizedmenu.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.minimizedmenu, 1, 1, 1, 1)

        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_btn = QPushButton(self.title_frame)
        self.menu_btn.setObjectName(u"menu_btn")

        self.horizontalLayout.addWidget(self.menu_btn)

        self.app_icon = QLabel(self.title_frame)
        self.app_icon.setObjectName(u"app_icon")

        self.horizontalLayout.addWidget(self.app_icon)

        self.app_title = QLabel(self.title_frame)
        self.app_title.setObjectName(u"app_title")

        self.horizontalLayout.addWidget(self.app_title)

        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.title_frame, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.config_title.setText("")
        self.config_desc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cfg_lbl.setText(QCoreApplication.translate("MainWindow", u"Configuration File : ", None))
        self.cfg_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add configuration file (.cfg)", None))
        self.cfg_browse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.confidence_lbl.setText(QCoreApplication.translate("MainWindow", u"Confidence Score :", None))
        self.feed_title.setText("")
        self.feed_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_desc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_results.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.app_icon.setText("")
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText("")
    # retranslateUi


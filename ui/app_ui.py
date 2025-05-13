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
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1340, 844)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.maximizedmenu = QListWidget(self.centralwidget)
        self.maximizedmenu.setObjectName(u"maximizedmenu")
        self.maximizedmenu.setMinimumSize(QSize(250, 0))
        self.maximizedmenu.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.maximizedmenu, 1, 2, 1, 1)

        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.minimizedmenu = QListWidget(self.centralwidget)
        self.minimizedmenu.setObjectName(u"minimizedmenu")
        self.minimizedmenu.setMinimumSize(QSize(75, 0))
        self.minimizedmenu.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.minimizedmenu, 1, 1, 1, 1)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.config_page = QWidget()
        self.config_page.setObjectName(u"config_page")
        self.config_section_frame = QFrame(self.config_page)
        self.config_section_frame.setObjectName(u"config_section_frame")
        self.config_section_frame.setGeometry(QRect(0, 0, 791, 631))
        self.config_section_frame.setFrameShape(QFrame.StyledPanel)
        self.config_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.config_section_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.config_title_frame = QFrame(self.config_section_frame)
        self.config_title_frame.setObjectName(u"config_title_frame")
        self.config_title_frame.setMaximumSize(QSize(16777215, 80))
        self.config_title_frame.setStyleSheet(u"border: none;")
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
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.config_body_desc = QFrame(self.config_body_frame)
        self.config_body_desc.setObjectName(u"config_body_desc")
        self.config_body_desc.setMinimumSize(QSize(0, 0))
        self.config_body_desc.setMaximumSize(QSize(16777215, 200))
        self.config_body_desc.setFrameShape(QFrame.StyledPanel)
        self.config_body_desc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.config_body_desc)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.config_desc = QLabel(self.config_body_desc)
        self.config_desc.setObjectName(u"config_desc")
        self.config_desc.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.config_desc)

        self.config_model = QHBoxLayout()
        self.config_model.setSpacing(0)
        self.config_model.setObjectName(u"config_model")
        self.config_curr_model = QLabel(self.config_body_desc)
        self.config_curr_model.setObjectName(u"config_curr_model")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_curr_model.sizePolicy().hasHeightForWidth())
        self.config_curr_model.setSizePolicy(sizePolicy)
        self.config_curr_model.setMaximumSize(QSize(16777215, 16777215))

        self.config_model.addWidget(self.config_curr_model)

        self.model_name = QLabel(self.config_body_desc)
        self.model_name.setObjectName(u"model_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.model_name.sizePolicy().hasHeightForWidth())
        self.model_name.setSizePolicy(sizePolicy1)
        self.model_name.setMaximumSize(QSize(16777215, 16777215))

        self.config_model.addWidget(self.model_name)


        self.verticalLayout_4.addLayout(self.config_model)

        self.config_classes = QHBoxLayout()
        self.config_classes.setSpacing(0)
        self.config_classes.setObjectName(u"config_classes")
        self.config_curr_classfile = QLabel(self.config_body_desc)
        self.config_curr_classfile.setObjectName(u"config_curr_classfile")
        sizePolicy.setHeightForWidth(self.config_curr_classfile.sizePolicy().hasHeightForWidth())
        self.config_curr_classfile.setSizePolicy(sizePolicy)
        self.config_curr_classfile.setMaximumSize(QSize(16777215, 16777215))

        self.config_classes.addWidget(self.config_curr_classfile)

        self.classfile = QLabel(self.config_body_desc)
        self.classfile.setObjectName(u"classfile")
        sizePolicy1.setHeightForWidth(self.classfile.sizePolicy().hasHeightForWidth())
        self.classfile.setSizePolicy(sizePolicy1)
        self.classfile.setMaximumSize(QSize(16777215, 16777215))

        self.config_classes.addWidget(self.classfile)


        self.verticalLayout_4.addLayout(self.config_classes)

        self.classes_content = QHBoxLayout()
        self.classes_content.setSpacing(0)
        self.classes_content.setObjectName(u"classes_content")
        self.class_label = QLabel(self.config_body_desc)
        self.class_label.setObjectName(u"class_label")
        sizePolicy.setHeightForWidth(self.class_label.sizePolicy().hasHeightForWidth())
        self.class_label.setSizePolicy(sizePolicy)
        self.class_label.setMaximumSize(QSize(16777215, 16777215))

        self.classes_content.addWidget(self.class_label)

        self.class_list = QLabel(self.config_body_desc)
        self.class_list.setObjectName(u"class_list")
        sizePolicy1.setHeightForWidth(self.class_list.sizePolicy().hasHeightForWidth())
        self.class_list.setSizePolicy(sizePolicy1)
        self.class_list.setMaximumSize(QSize(16777215, 16777215))

        self.classes_content.addWidget(self.class_list)


        self.verticalLayout_4.addLayout(self.classes_content)


        self.verticalLayout_2.addWidget(self.config_body_desc)

        self.config_body_files = QFrame(self.config_body_frame)
        self.config_body_files.setObjectName(u"config_body_files")
        self.config_body_files.setMaximumSize(QSize(16777215, 16777215))
        self.config_body_files.setFrameShape(QFrame.StyledPanel)
        self.config_body_files.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.config_body_files)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.config_camera_frame = QFrame(self.config_body_files)
        self.config_camera_frame.setObjectName(u"config_camera_frame")
        self.config_camera_frame.setFrameShape(QFrame.StyledPanel)
        self.config_camera_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.config_camera_frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.config_camera_label = QLabel(self.config_camera_frame)
        self.config_camera_label.setObjectName(u"config_camera_label")
        sizePolicy.setHeightForWidth(self.config_camera_label.sizePolicy().hasHeightForWidth())
        self.config_camera_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.config_camera_label, 0, Qt.AlignRight)

        self.config_camerabtn_frame = QFrame(self.config_camera_frame)
        self.config_camerabtn_frame.setObjectName(u"config_camerabtn_frame")
        sizePolicy1.setHeightForWidth(self.config_camerabtn_frame.sizePolicy().hasHeightForWidth())
        self.config_camerabtn_frame.setSizePolicy(sizePolicy1)
        self.config_camerabtn_frame.setFrameShape(QFrame.StyledPanel)
        self.config_camerabtn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.config_camerabtn_frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.config_camera_lineedit = QLineEdit(self.config_camerabtn_frame)
        self.config_camera_lineedit.setObjectName(u"config_camera_lineedit")

        self.horizontalLayout_17.addWidget(self.config_camera_lineedit)

        self.config_camera_btn = QPushButton(self.config_camerabtn_frame)
        self.config_camera_btn.setObjectName(u"config_camera_btn")

        self.horizontalLayout_17.addWidget(self.config_camera_btn)


        self.horizontalLayout_16.addWidget(self.config_camerabtn_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.config_camera_frame)

        self.config_classes_frame = QFrame(self.config_body_files)
        self.config_classes_frame.setObjectName(u"config_classes_frame")
        self.config_classes_frame.setFrameShape(QFrame.StyledPanel)
        self.config_classes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.config_classes_frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.config_classes_label = QLabel(self.config_classes_frame)
        self.config_classes_label.setObjectName(u"config_classes_label")
        sizePolicy.setHeightForWidth(self.config_classes_label.sizePolicy().hasHeightForWidth())
        self.config_classes_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.config_classes_label, 0, Qt.AlignRight)

        self.config_classesbtn_frame = QFrame(self.config_classes_frame)
        self.config_classesbtn_frame.setObjectName(u"config_classesbtn_frame")
        sizePolicy1.setHeightForWidth(self.config_classesbtn_frame.sizePolicy().hasHeightForWidth())
        self.config_classesbtn_frame.setSizePolicy(sizePolicy1)
        self.config_classesbtn_frame.setFrameShape(QFrame.StyledPanel)
        self.config_classesbtn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.config_classesbtn_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.config_classes_lineedit = QLineEdit(self.config_classesbtn_frame)
        self.config_classes_lineedit.setObjectName(u"config_classes_lineedit")

        self.horizontalLayout_22.addWidget(self.config_classes_lineedit)

        self.config_classes_btn = QPushButton(self.config_classesbtn_frame)
        self.config_classes_btn.setObjectName(u"config_classes_btn")

        self.horizontalLayout_22.addWidget(self.config_classes_btn)


        self.horizontalLayout_21.addWidget(self.config_classesbtn_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.config_classes_frame)

        self.config_cfscore_frame = QFrame(self.config_body_files)
        self.config_cfscore_frame.setObjectName(u"config_cfscore_frame")
        self.config_cfscore_frame.setFrameShape(QFrame.StyledPanel)
        self.config_cfscore_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.config_cfscore_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.config_cfscore_label = QLabel(self.config_cfscore_frame)
        self.config_cfscore_label.setObjectName(u"config_cfscore_label")
        sizePolicy.setHeightForWidth(self.config_cfscore_label.sizePolicy().hasHeightForWidth())
        self.config_cfscore_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.config_cfscore_label, 0, Qt.AlignRight)

        self.config_cfscorebtn_frame = QFrame(self.config_cfscore_frame)
        self.config_cfscorebtn_frame.setObjectName(u"config_cfscorebtn_frame")
        sizePolicy1.setHeightForWidth(self.config_cfscorebtn_frame.sizePolicy().hasHeightForWidth())
        self.config_cfscorebtn_frame.setSizePolicy(sizePolicy1)
        self.config_cfscorebtn_frame.setFrameShape(QFrame.StyledPanel)
        self.config_cfscorebtn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.config_cfscorebtn_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.config_cfscore_btn_sub = QPushButton(self.config_cfscorebtn_frame)
        self.config_cfscore_btn_sub.setObjectName(u"config_cfscore_btn_sub")

        self.horizontalLayout_9.addWidget(self.config_cfscore_btn_sub)

        self.config_cfscore_lineedit = QLineEdit(self.config_cfscorebtn_frame)
        self.config_cfscore_lineedit.setObjectName(u"config_cfscore_lineedit")

        self.horizontalLayout_9.addWidget(self.config_cfscore_lineedit)

        self.config_cfscore_btn_add = QPushButton(self.config_cfscorebtn_frame)
        self.config_cfscore_btn_add.setObjectName(u"config_cfscore_btn_add")

        self.horizontalLayout_9.addWidget(self.config_cfscore_btn_add)


        self.horizontalLayout_18.addWidget(self.config_cfscorebtn_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.config_cfscore_frame)


        self.verticalLayout_2.addWidget(self.config_body_files, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.config_body_frame)

        self.pages.addWidget(self.config_page)
        self.feed_page = QWidget()
        self.feed_page.setObjectName(u"feed_page")
        self.feed_section_frame = QFrame(self.feed_page)
        self.feed_section_frame.setObjectName(u"feed_section_frame")
        self.feed_section_frame.setGeometry(QRect(0, 0, 461, 601))
        self.feed_section_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.feed_section_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.feed_title_frame = QFrame(self.feed_section_frame)
        self.feed_title_frame.setObjectName(u"feed_title_frame")
        self.feed_title_frame.setMinimumSize(QSize(0, 80))
        self.feed_title_frame.setMaximumSize(QSize(16777215, 80))
        self.feed_title_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.feed_title_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.feed_title = QLabel(self.feed_title_frame)
        self.feed_title.setObjectName(u"feed_title")
        self.feed_title.setMaximumSize(QSize(16777215, 16777215))
        self.feed_title.setStyleSheet(u"background-color:rgb(44, 20, 74);\n"
"border-radius: 15px;")

        self.horizontalLayout_6.addWidget(self.feed_title)


        self.verticalLayout_8.addWidget(self.feed_title_frame)

        self.feed_body_frame = QFrame(self.feed_section_frame)
        self.feed_body_frame.setObjectName(u"feed_body_frame")
        self.feed_body_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.feed_body_frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.feed_camera = QFrame(self.feed_body_frame)
        self.feed_camera.setObjectName(u"feed_camera")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.feed_camera.sizePolicy().hasHeightForWidth())
        self.feed_camera.setSizePolicy(sizePolicy2)
        self.feed_camera.setMinimumSize(QSize(0, 0))
        self.feed_camera.setMaximumSize(QSize(16777215, 16777215))
        self.feed_camera.setFrameShape(QFrame.StyledPanel)
        self.feed_camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.feed_camera)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.feed_label = QLabel(self.feed_camera)
        self.feed_label.setObjectName(u"feed_label")
        self.feed_label.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.feed_label)


        self.horizontalLayout_2.addWidget(self.feed_camera)

        self.feed_body_desc = QFrame(self.feed_body_frame)
        self.feed_body_desc.setObjectName(u"feed_body_desc")
        sizePolicy.setHeightForWidth(self.feed_body_desc.sizePolicy().hasHeightForWidth())
        self.feed_body_desc.setSizePolicy(sizePolicy)
        self.feed_body_desc.setMinimumSize(QSize(250, 0))
        self.feed_body_desc.setMaximumSize(QSize(16777215, 16777215))
        self.feed_body_desc.setFrameShape(QFrame.StyledPanel)
        self.feed_body_desc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.feed_body_desc)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.feed_model_frame = QFrame(self.feed_body_desc)
        self.feed_model_frame.setObjectName(u"feed_model_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.feed_model_frame.sizePolicy().hasHeightForWidth())
        self.feed_model_frame.setSizePolicy(sizePolicy3)
        self.feed_model_frame.setMinimumSize(QSize(0, 75))
        self.feed_model_frame.setMaximumSize(QSize(16777215, 75))
        self.feed_model_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_model_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.feed_model_frame)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.feed_model_title = QLabel(self.feed_model_frame)
        self.feed_model_title.setObjectName(u"feed_model_title")

        self.horizontalLayout_5.addWidget(self.feed_model_title)

        self.feed_model_content = QLabel(self.feed_model_frame)
        self.feed_model_content.setObjectName(u"feed_model_content")

        self.horizontalLayout_5.addWidget(self.feed_model_content)


        self.verticalLayout_21.addWidget(self.feed_model_frame)

        self.feed_classes_frame = QFrame(self.feed_body_desc)
        self.feed_classes_frame.setObjectName(u"feed_classes_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.feed_classes_frame.sizePolicy().hasHeightForWidth())
        self.feed_classes_frame.setSizePolicy(sizePolicy4)
        self.feed_classes_frame.setMaximumSize(QSize(16777215, 16777215))
        self.feed_classes_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_classes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.feed_classes_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.feed_classes_title = QLabel(self.feed_classes_frame)
        self.feed_classes_title.setObjectName(u"feed_classes_title")
        self.feed_classes_title.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.feed_classes_title)

        self.feed_classes_content = QLabel(self.feed_classes_frame)
        self.feed_classes_content.setObjectName(u"feed_classes_content")
        self.feed_classes_content.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.feed_classes_content)


        self.verticalLayout_21.addWidget(self.feed_classes_frame, 0, Qt.AlignTop)

        self.feed_bottom_frame = QFrame(self.feed_body_desc)
        self.feed_bottom_frame.setObjectName(u"feed_bottom_frame")
        sizePolicy3.setHeightForWidth(self.feed_bottom_frame.sizePolicy().hasHeightForWidth())
        self.feed_bottom_frame.setSizePolicy(sizePolicy3)
        self.feed_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.feed_bottom_frame)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.feed_progressbar_frame = QFrame(self.feed_bottom_frame)
        self.feed_progressbar_frame.setObjectName(u"feed_progressbar_frame")
        self.feed_progressbar_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_progressbar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.feed_progressbar_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.feed_progressbar = QProgressBar(self.feed_progressbar_frame)
        self.feed_progressbar.setObjectName(u"feed_progressbar")
        self.feed_progressbar.setValue(24)

        self.verticalLayout_5.addWidget(self.feed_progressbar)


        self.verticalLayout_19.addWidget(self.feed_progressbar_frame)

        self.feed_control_frame = QFrame(self.feed_bottom_frame)
        self.feed_control_frame.setObjectName(u"feed_control_frame")
        self.feed_control_frame.setMaximumSize(QSize(16777215, 16777215))
        self.feed_control_frame.setFrameShape(QFrame.StyledPanel)
        self.feed_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.feed_control_frame)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.feed_detect_btn = QPushButton(self.feed_control_frame)
        self.feed_detect_btn.setObjectName(u"feed_detect_btn")

        self.horizontalLayout_8.addWidget(self.feed_detect_btn)

        self.feed_stop_btn = QPushButton(self.feed_control_frame)
        self.feed_stop_btn.setObjectName(u"feed_stop_btn")
        self.feed_stop_btn.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.feed_stop_btn)


        self.verticalLayout_19.addWidget(self.feed_control_frame)


        self.verticalLayout_21.addWidget(self.feed_bottom_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.feed_body_desc)


        self.verticalLayout_8.addWidget(self.feed_body_frame)

        self.pages.addWidget(self.feed_page)
        self.analytics_page = QWidget()
        self.analytics_page.setObjectName(u"analytics_page")
        self.analytics_section_frame = QFrame(self.analytics_page)
        self.analytics_section_frame.setObjectName(u"analytics_section_frame")
        self.analytics_section_frame.setGeometry(QRect(0, 0, 1111, 831))
        self.analytics_section_frame.setFrameShape(QFrame.StyledPanel)
        self.analytics_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.analytics_section_frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(20, 20, 20, 20)
        self.analytics_title_frame = QFrame(self.analytics_section_frame)
        self.analytics_title_frame.setObjectName(u"analytics_title_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.analytics_title_frame.sizePolicy().hasHeightForWidth())
        self.analytics_title_frame.setSizePolicy(sizePolicy5)
        self.analytics_title_frame.setMinimumSize(QSize(0, 80))
        self.analytics_title_frame.setMaximumSize(QSize(16777215, 80))
        self.analytics_title_frame.setFrameShape(QFrame.StyledPanel)
        self.analytics_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.analytics_title_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.analytics_title = QLabel(self.analytics_title_frame)
        self.analytics_title.setObjectName(u"analytics_title")
        self.analytics_title.setStyleSheet(u"background-color:rgb(44, 20, 74);\n"
"border-radius: 15px;")

        self.horizontalLayout_4.addWidget(self.analytics_title)


        self.verticalLayout_17.addWidget(self.analytics_title_frame)

        self.analytics_body_frame = QFrame(self.analytics_section_frame)
        self.analytics_body_frame.setObjectName(u"analytics_body_frame")
        self.analytics_body_frame.setFrameShape(QFrame.StyledPanel)
        self.analytics_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.analytics_body_frame)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 20, 0, 0)
        self.analytics_body_content = QFrame(self.analytics_body_frame)
        self.analytics_body_content.setObjectName(u"analytics_body_content")
        self.analytics_body_content.setMaximumSize(QSize(16777215, 16777215))
        self.analytics_body_content.setFrameShape(QFrame.StyledPanel)
        self.analytics_body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.analytics_body_content)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.analytics_body_content)


        self.verticalLayout_17.addWidget(self.analytics_body_frame)

        self.pages.addWidget(self.analytics_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_section_frame = QFrame(self.about_page)
        self.about_section_frame.setObjectName(u"about_section_frame")
        self.about_section_frame.setGeometry(QRect(0, 0, 1001, 821))
        self.about_section_frame.setFrameShape(QFrame.StyledPanel)
        self.about_section_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.about_section_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.about_title_frame = QFrame(self.about_section_frame)
        self.about_title_frame.setObjectName(u"about_title_frame")
        self.about_title_frame.setMaximumSize(QSize(16777215, 80))
        self.about_title_frame.setFrameShape(QFrame.StyledPanel)
        self.about_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.about_title_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.about_title = QLabel(self.about_title_frame)
        self.about_title.setObjectName(u"about_title")
        self.about_title.setStyleSheet(u"background-color:rgb(44, 20, 74);\n"
"border-radius: 15px;")

        self.horizontalLayout_7.addWidget(self.about_title)


        self.verticalLayout_9.addWidget(self.about_title_frame)

        self.about_body_frame = QFrame(self.about_section_frame)
        self.about_body_frame.setObjectName(u"about_body_frame")
        self.about_body_frame.setFrameShape(QFrame.StyledPanel)
        self.about_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.about_body_frame)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 20, 0, 0)
        self.about_ics_frame = QFrame(self.about_body_frame)
        self.about_ics_frame.setObjectName(u"about_ics_frame")
        self.about_ics_frame.setFrameShape(QFrame.StyledPanel)
        self.about_ics_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.about_ics_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ics_logo = QFrame(self.about_ics_frame)
        self.ics_logo.setObjectName(u"ics_logo")
        sizePolicy.setHeightForWidth(self.ics_logo.sizePolicy().hasHeightForWidth())
        self.ics_logo.setSizePolicy(sizePolicy)
        self.ics_logo.setFrameShape(QFrame.StyledPanel)
        self.ics_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.ics_logo)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ics_logo_label = QLabel(self.ics_logo)
        self.ics_logo_label.setObjectName(u"ics_logo_label")

        self.horizontalLayout_12.addWidget(self.ics_logo_label)


        self.horizontalLayout_11.addWidget(self.ics_logo, 0, Qt.AlignVCenter)

        self.about_ics_people = QFrame(self.about_ics_frame)
        self.about_ics_people.setObjectName(u"about_ics_people")
        sizePolicy2.setHeightForWidth(self.about_ics_people.sizePolicy().hasHeightForWidth())
        self.about_ics_people.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.about_ics_people)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ics_1 = QFrame(self.about_ics_people)
        self.ics_1.setObjectName(u"ics_1")
        self.ics_1.setFrameShape(QFrame.StyledPanel)
        self.ics_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.ics_1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ics_adviser_name = QLabel(self.ics_1)
        self.ics_adviser_name.setObjectName(u"ics_adviser_name")

        self.verticalLayout_13.addWidget(self.ics_adviser_name)

        self.ics_adviser_designation = QLabel(self.ics_1)
        self.ics_adviser_designation.setObjectName(u"ics_adviser_designation")

        self.verticalLayout_13.addWidget(self.ics_adviser_designation)


        self.verticalLayout_10.addWidget(self.ics_1, 0, Qt.AlignBottom)

        self.ics_2 = QFrame(self.about_ics_people)
        self.ics_2.setObjectName(u"ics_2")
        self.ics_2.setFrameShape(QFrame.StyledPanel)
        self.ics_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.ics_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.ics_student_name = QLabel(self.ics_2)
        self.ics_student_name.setObjectName(u"ics_student_name")

        self.verticalLayout_14.addWidget(self.ics_student_name)

        self.ics_student_designation = QLabel(self.ics_2)
        self.ics_student_designation.setObjectName(u"ics_student_designation")

        self.verticalLayout_14.addWidget(self.ics_student_designation)


        self.verticalLayout_10.addWidget(self.ics_2, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.about_ics_people)


        self.verticalLayout_12.addWidget(self.about_ics_frame)

        self.about_ipb_frame = QFrame(self.about_body_frame)
        self.about_ipb_frame.setObjectName(u"about_ipb_frame")
        self.about_ipb_frame.setFrameShape(QFrame.StyledPanel)
        self.about_ipb_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.about_ipb_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ipb_logo = QFrame(self.about_ipb_frame)
        self.ipb_logo.setObjectName(u"ipb_logo")
        sizePolicy.setHeightForWidth(self.ipb_logo.sizePolicy().hasHeightForWidth())
        self.ipb_logo.setSizePolicy(sizePolicy)
        self.ipb_logo.setFrameShape(QFrame.StyledPanel)
        self.ipb_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.ipb_logo)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.ipb_logo_label = QLabel(self.ipb_logo)
        self.ipb_logo_label.setObjectName(u"ipb_logo_label")
        self.ipb_logo_label.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_14.addWidget(self.ipb_logo_label)


        self.horizontalLayout_13.addWidget(self.ipb_logo, 0, Qt.AlignVCenter)

        self.about_ipb_people = QFrame(self.about_ipb_frame)
        self.about_ipb_people.setObjectName(u"about_ipb_people")
        sizePolicy2.setHeightForWidth(self.about_ipb_people.sizePolicy().hasHeightForWidth())
        self.about_ipb_people.setSizePolicy(sizePolicy2)
        self.verticalLayout_11 = QVBoxLayout(self.about_ipb_people)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ipb_1 = QFrame(self.about_ipb_people)
        self.ipb_1.setObjectName(u"ipb_1")
        self.ipb_1.setFrameShape(QFrame.StyledPanel)
        self.ipb_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.ipb_1)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ipb_adviser_name = QLabel(self.ipb_1)
        self.ipb_adviser_name.setObjectName(u"ipb_adviser_name")

        self.verticalLayout_15.addWidget(self.ipb_adviser_name)

        self.ipb_adviser_designation = QLabel(self.ipb_1)
        self.ipb_adviser_designation.setObjectName(u"ipb_adviser_designation")

        self.verticalLayout_15.addWidget(self.ipb_adviser_designation)


        self.verticalLayout_11.addWidget(self.ipb_1, 0, Qt.AlignBottom)

        self.ipb_2 = QFrame(self.about_ipb_people)
        self.ipb_2.setObjectName(u"ipb_2")
        self.ipb_2.setFrameShape(QFrame.StyledPanel)
        self.ipb_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.ipb_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ipb_student_name = QLabel(self.ipb_2)
        self.ipb_student_name.setObjectName(u"ipb_student_name")

        self.verticalLayout_16.addWidget(self.ipb_student_name)

        self.ipb_student_designation = QLabel(self.ipb_2)
        self.ipb_student_designation.setObjectName(u"ipb_student_designation")

        self.verticalLayout_16.addWidget(self.ipb_student_designation)


        self.verticalLayout_11.addWidget(self.ipb_2, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.about_ipb_people)


        self.verticalLayout_12.addWidget(self.about_ipb_frame)


        self.verticalLayout_9.addWidget(self.about_body_frame)

        self.pages.addWidget(self.about_page)

        self.gridLayout.addWidget(self.pages, 0, 3, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.app_icon.setText("")
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText("")
        self.config_title.setText("")
        self.config_desc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_curr_model.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.model_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_curr_classfile.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.classfile.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.class_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.class_list.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_camera_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_camera_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.config_classes_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_classes_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.config_cfscore_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.config_cfscore_btn_sub.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.config_cfscore_btn_add.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.feed_title.setText("")
        self.feed_label.setText("")
        self.feed_model_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_model_content.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_classes_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_classes_content.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.feed_detect_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.feed_stop_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.analytics_title.setText("")
        self.about_title.setText("")
        self.ics_logo_label.setText(QCoreApplication.translate("MainWindow", u"ics logo", None))
        self.ics_adviser_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ics_adviser_designation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ics_student_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ics_student_designation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipb_logo_label.setText(QCoreApplication.translate("MainWindow", u"ipb logo", None))
        self.ipb_adviser_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipb_adviser_designation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipb_student_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipb_student_designation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi


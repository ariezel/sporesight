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
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizedmenu = QListWidget(self.centralwidget)
        self.minimizedmenu.setObjectName(u"minimizedmenu")
        self.minimizedmenu.setMinimumSize(QSize(0, 0))
        self.minimizedmenu.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.minimizedmenu, 1, 1, 1, 1)

        self.maximizedmenu = QListWidget(self.centralwidget)
        self.maximizedmenu.setObjectName(u"maximizedmenu")
        self.maximizedmenu.setMinimumSize(QSize(0, 0))
        self.maximizedmenu.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.maximizedmenu, 1, 2, 1, 1)

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

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 671, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.config_title_frame = QFrame(self.frame)
        self.config_title_frame.setObjectName(u"config_title_frame")
        self.config_title_frame.setStyleSheet(u"background-color: rgb(52, 73, 85);\n"
"border-radius: 14px;")
        self.config_title_frame.setFrameShape(QFrame.NoFrame)
        self.config_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.config_title_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 4, -1, 4)
        self.step2_lbl = QPushButton(self.config_title_frame)
        self.step2_lbl.setObjectName(u"step2_lbl")
        self.step2_lbl.setStyleSheet(u"background-color: rgb(52, 73, 85);\n"
"color: rgb(192, 192, 192);\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"text-align: right;\n"
"border: none;")

        self.horizontalLayout_9.addWidget(self.step2_lbl)


        self.verticalLayout.addWidget(self.config_title_frame)

        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pages.addWidget(self.page_2)

        self.gridLayout.addWidget(self.pages, 0, 3, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.app_icon.setText("")
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText("")
        self.step2_lbl.setText(QCoreApplication.translate("MainWindow", u"Step 2 of 5", None))
    # retranslateUi


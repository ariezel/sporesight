# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(567, 346)
        icon = QIcon()
        icon.addFile(u":/icons/icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Splash.setWindowIcon(icon)
        self.splash_frame = QWidget(Splash)
        self.splash_frame.setObjectName(u"splash_frame")
        self.horizontalLayout = QHBoxLayout(self.splash_frame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.splash_outer_frame = QFrame(self.splash_frame)
        self.splash_outer_frame.setObjectName(u"splash_outer_frame")
        self.splash_outer_frame.setStyleSheet(u"QFrame #splash_outer_frame {\n"
"	background-color: #210F37;\n"
"	border-radius: 40px;\n"
"}")
        self.splash_outer_frame.setFrameShape(QFrame.NoFrame)
        self.splash_outer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.splash_outer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.splash_inner_frame = QFrame(self.splash_outer_frame)
        self.splash_inner_frame.setObjectName(u"splash_inner_frame")
        self.splash_inner_frame.setStyleSheet(u"QFrame #splash_inner_frame {\n"
"	background-color: #f7f7f7;\n"
"	border-radius: 35px;\n"
"}")
        self.splash_inner_frame.setFrameShape(QFrame.NoFrame)
        self.splash_inner_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.splash_inner_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splash_title_frame = QFrame(self.splash_inner_frame)
        self.splash_title_frame.setObjectName(u"splash_title_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splash_title_frame.sizePolicy().hasHeightForWidth())
        self.splash_title_frame.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.splash_title_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 30, 0, 0)
        self.splash_title_lbl = QPushButton(self.splash_title_frame)
        self.splash_title_lbl.setObjectName(u"splash_title_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splash_title_lbl.sizePolicy().hasHeightForWidth())
        self.splash_title_lbl.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        self.splash_title_lbl.setFont(font)
        self.splash_title_lbl.setStyleSheet(u"QPushButton { \n"
"	color: #210F37;\n"
"	border: none;\n"
"	text-align:center;\n"
"	border-radius: 10px;\n"
"	padding-left: 40px;\n"
"	padding-right: 40px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	font-size:70px;\n"
"}")
        self.splash_title_lbl.setIconSize(QSize(100, 100))
        self.splash_title_lbl.setCheckable(True)
        self.splash_title_lbl.setChecked(True)

        self.horizontalLayout_3.addWidget(self.splash_title_lbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.splash_title_frame, 0, Qt.AlignVCenter)

        self.splash_caption_frame = QFrame(self.splash_inner_frame)
        self.splash_caption_frame.setObjectName(u"splash_caption_frame")
        self.splash_caption_frame.setFrameShape(QFrame.NoFrame)
        self.splash_caption_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.splash_caption_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(90, -1, 90, 30)
        self.splash_progress = QProgressBar(self.splash_caption_frame)
        self.splash_progress.setObjectName(u"splash_progress")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.splash_progress.setFont(font1)
        self.splash_progress.setStyleSheet(u"QProgressBar {\n"
"	background-color: #210F37;\n"
"	color: rgb(255,255,255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(33, 15, 55, 1), stop:1 rgba(79,28,81,1));\n"
"}")

        self.verticalLayout_2.addWidget(self.splash_progress)

        self.splash_caption_lbl = QLabel(self.splash_caption_frame)
        self.splash_caption_lbl.setObjectName(u"splash_caption_lbl")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.splash_caption_lbl.setFont(font2)
        self.splash_caption_lbl.setStyleSheet(u"color: #210F37;")
        self.splash_caption_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.splash_caption_lbl)


        self.verticalLayout.addWidget(self.splash_caption_frame, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.splash_inner_frame)


        self.horizontalLayout.addWidget(self.splash_outer_frame)

        Splash.setCentralWidget(self.splash_frame)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"MainWindow", None))
        self.splash_title_lbl.setText(QCoreApplication.translate("Splash", u"SporeSight", None))
        self.splash_caption_lbl.setText("")
    # retranslateUi


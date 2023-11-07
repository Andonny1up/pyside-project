# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceproMyYRks.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#leftMenu{\n"
"	background-color: #2596be;\n"
"}\n"
"#mainBody{\n"
"	background-color: #eff9fe;\n"
"}\n"
"QLineEdit{\n"
"	background: transparent;\n"
"	color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"#appHeader{\n"
"	color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4{\n"
"	background-color: #fefeff;\n"
"	border-radius: 10px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"	background-color: #2596be;\n"
"	color: #fff;\n"
"	border-radius:10px;\n"
"}\n"
"#widget_4, #widget_5,#profileCont{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"	background-color: #fefeff;\n"
"}\n"
"#pushButton_7{\n"
"	background-color: #fefeff;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 0, 0, 0)
        self.frame_11 = QFrame(self.leftMenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_43 = QLabel(self.frame_12)
        self.label_43.setObjectName(u"label_43")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_43.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_43, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon = QIcon()
        icon.addFile(u":/blueIcons/assets/icon_blue/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/whiteIcons/assets/icon_white/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_14)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon2 = QIcon()
        icon2.addFile(u":/whiteIcons/assets/icon_white/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_14)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon3 = QIcon()
        icon3.addFile(u":/whiteIcons/assets/icon_white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.pushButton_10)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_13)


        self.verticalLayout_8.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon4 = QIcon()
        icon4.addFile(u":/blueIcons/assets/icon_blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.appHeader = QLabel(self.widget)
        self.appHeader.setObjectName(u"appHeader")
        self.appHeader.setFont(font)

        self.horizontalLayout_4.addWidget(self.appHeader, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(160, 0))
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/search.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_3.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountBtn = QPushButton(self.widget_3)
        self.accountBtn.setObjectName(u"accountBtn")
        icon5 = QIcon()
        icon5.addFile(u":/blueIcons/assets/icon_blue/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.accountBtn)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardsFrame = QWidget(self.mainBody)
        self.cardsFrame.setObjectName(u"cardsFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.card1 = QFrame(self.cardsFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.card1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setFont(font1)
        self.label_3.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/shopping-cart.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.card1)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.cardsFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.card2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setFont(font1)
        self.label_6.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/credit-card.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.label_7 = QLabel(self.card2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_7, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.cardsFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.card3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setFont(font1)
        self.label_9.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/align-right.svg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.label_10 = QLabel(self.card3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_10, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.cardsFrame)
        self.card4.setObjectName(u"card4")
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.card4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(40, 40))
        self.label_12.setFont(font1)
        self.label_12.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/shopping-cart.svg"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.label_13 = QLabel(self.card4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_13, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout.addWidget(self.cardsFrame)

        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.widget_4 = QWidget(self.mainFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_14.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/whiteIcons/assets/icon_white/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_15.setFont(font4)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)

        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 1, 1, 1)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 2, 1, 1, 1)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 3, 2, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 2, 1, 1)

        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 3, 1, 1, 1)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.mainFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.widget_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.widget_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(50, 50))
        self.label_33.setMaximumSize(QSize(50, 50))
        self.label_33.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/globe.svg"))
        self.label_33.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_9)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(25, 25))
        self.label_35.setMaximumSize(QSize(25, 25))
        self.label_35.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/facebook.svg"))
        self.label_35.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_9)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(25, 25))
        self.label_36.setMaximumSize(QSize(25, 25))
        self.label_36.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/message-circle.svg"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_9)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(25, 25))
        self.label_37.setMaximumSize(QSize(25, 25))
        self.label_37.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/phone-call.svg"))
        self.label_37.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_37)


        self.verticalLayout_7.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.widget_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_38 = QLabel(self.frame_10)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(50, 50))
        self.label_38.setMaximumSize(QSize(50, 50))
        self.label_38.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/globe.svg"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_10)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_17.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_10)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(25, 25))
        self.label_40.setMaximumSize(QSize(25, 25))
        self.label_40.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/facebook.svg"))
        self.label_40.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_10)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(25, 25))
        self.label_41.setMaximumSize(QSize(25, 25))
        self.label_41.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/message-circle.svg"))
        self.label_41.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_10)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(25, 25))
        self.label_42.setMaximumSize(QSize(25, 25))
        self.label_42.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/phone-call.svg"))
        self.label_42.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_42)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 50))
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/globe.svg"))
        self.label_28.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_15.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(25, 25))
        self.label_30.setMaximumSize(QSize(25, 25))
        self.label_30.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/facebook.svg"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(25, 25))
        self.label_31.setMaximumSize(QSize(25, 25))
        self.label_31.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/message-circle.svg"))
        self.label_31.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(25, 25))
        self.label_32.setMaximumSize(QSize(25, 25))
        self.label_32.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/phone-call.svg"))
        self.label_32.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_32)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignTop)


        self.horizontalLayout_12.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.mainFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        self.profileCont = QWidget(self.centralwidget)
        self.profileCont.setObjectName(u"profileCont")
        self.verticalLayout_13 = QVBoxLayout(self.profileCont)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.profileCont)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(100, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_44 = QLabel(self.frame_15)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_44, 0, Qt.AlignTop)

        self.label_45 = QLabel(self.frame_15)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_14.addWidget(self.label_45, 0, Qt.AlignTop)

        self.label_46 = QLabel(self.frame_15)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(50, 50))
        self.label_46.setMaximumSize(QSize(50, 50))
        self.label_46.setPixmap(QPixmap(u":/blueIcons/assets/icon_blue/alert-circle.svg"))

        self.verticalLayout_14.addWidget(self.label_46, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_11 = QPushButton(self.frame_15)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon5)

        self.verticalLayout_14.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_15)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon7 = QIcon()
        icon7.addFile(u":/blueIcons/assets/icon_blue/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon7)

        self.verticalLayout_14.addWidget(self.pushButton_12)


        self.verticalLayout_13.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profileCont, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"DESIGNER PUSHMAN", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Algo", None))
        self.accountBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"2.000.000", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"+30", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Something", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"20k", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Community", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ver m\u00e1s", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"cafe", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Almacen", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"$10", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"$20", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Nairobi", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"New jersey", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"$30", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Leche", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Te", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hong kong", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ver m\u00e1s", None))
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Spinn</span></p><p>TV</p></body></html>", None))
        self.label_35.setText("")
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Spinn</span></p><p>TV</p></body></html>", None))
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_42.setText("")
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Spinn</span></p><p>TV</p></body></html>", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"SpinnTV", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_46.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Mi Perfil", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
    # retranslateUi


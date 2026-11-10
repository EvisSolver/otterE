# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 606)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 230, 272, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.serverPanel = QFrame(self.verticalLayoutWidget)
        self.serverPanel.setObjectName(u"serverPanel")
        self.serverPanel.setMinimumSize(QSize(270, 0))
        self.serverPanel.setMaximumSize(QSize(270, 16777215))
        self.serverPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.serverPanel.setFrameShadow(QFrame.Shadow.Raised)

        self.selected_server_label = QLabel(self.serverPanel)
        self.selected_server_label.setObjectName(u"selected_server_label")
        self.selected_server_label.setGeometry(QRect(55, 8, 160, 45))
        self.selected_server_label.setMinimumSize(QSize(0, 45))
        self.selected_server_label.setTextFormat(Qt.TextFormat.AutoText)
        self.selected_server_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.server_list = QListWidget(self.serverPanel)
        QListWidgetItem(self.server_list)

        self.server_list.setObjectName(u"server_list")
        self.server_list.setGeometry(QRect(40, 40, 191, 130))
        self.server_list.setMinimumSize(QSize(0, 130))

        self.verticalLayout.addWidget(self.serverPanel)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(180, 180, 271, 50))
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)

        self.gearButton = QToolButton(self.header)
        self.gearButton.setObjectName(u"gearButton")
        self.gearButton.setGeometry(QRect(0, 0, 51, 51))

        self.titleLabel = QLabel(self.header)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(90, 10, 101, 31))

        self.closeButton = QPushButton(self.header)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(220, 0, 51, 51))

        self.toggleFrame = QFrame(self.centralwidget)
        self.toggleFrame.setObjectName(u"toggleFrame")
        self.toggleFrame.setGeometry(QRect(180, 420, 270, 81))

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleFrame.sizePolicy().hasHeightForWidth())

        self.toggleFrame.setSizePolicy(sizePolicy)
        self.toggleFrame.setMinimumSize(QSize(270, 70))
        self.toggleFrame.setMaximumSize(QSize(270, 16777215))
        self.toggleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.toggleFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayoutWidget = QWidget(self.toggleFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 189, 81))

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.onButton = QPushButton(self.horizontalLayoutWidget)
        self.onButton.setObjectName(u"onButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.onButton.sizePolicy().hasHeightForWidth())
        self.onButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.onButton)

        self.offButton = QPushButton(self.horizontalLayoutWidget)
        self.offButton.setObjectName(u"offButton")
        sizePolicy1.setHeightForWidth(self.offButton.sizePolicy().hasHeightForWidth())
        self.offButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.offButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 22))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selected_server_label.setText(QCoreApplication.translate("MainWindow", u"$SERVER", None))

        __sortingEnabled = self.server_list.isSortingEnabled()
        self.server_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.server_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"server ???", None))
        self.server_list.setSortingEnabled(__sortingEnabled)

        self.gearButton.setText(QCoreApplication.translate("MainWindow", u"\u2699", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"IS NOT WORKING", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
        self.onButton.setText(QCoreApplication.translate("MainWindow", u"PROXY", None))
        self.offButton.setText(QCoreApplication.translate("MainWindow", u"TUN", None))
    # retranslateUi


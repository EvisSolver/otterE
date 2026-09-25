# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QListWidget, QListWidgetItem, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(740, 611)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 70, 381, 461))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.infoPanel = QFrame(self.horizontalLayoutWidget)
        self.infoPanel.setObjectName(u"infoPanel")
        self.infoPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.infoPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.infoLabel = QLabel(self.infoPanel)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(10, 10, 201, 441))
        self.settingsList = QListWidget(self.infoPanel)
        QListWidgetItem(self.settingsList)
        QListWidgetItem(self.settingsList)
        QListWidgetItem(self.settingsList)
        self.settingsList.setObjectName(u"settingsList")
        self.settingsList.setGeometry(QRect(220, 0, 161, 461))

        self.horizontalLayout.addWidget(self.infoPanel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.infoLabel.setText(QCoreApplication.translate("Form", u"$INFO", None))

        __sortingEnabled = self.settingsList.isSortingEnabled()
        self.settingsList.setSortingEnabled(False)
        ___qlistwidgetitem = self.settingsList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Theme", None))
        ___qlistwidgetitem1 = self.settingsList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Language", None))
        ___qlistwidgetitem2 = self.settingsList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"connect_proxy", None))
        self.settingsList.setSortingEnabled(__sortingEnabled)

    # retranslateUi


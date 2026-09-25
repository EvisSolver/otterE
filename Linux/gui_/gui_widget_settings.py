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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

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
        self.infoLabel.setGeometry(QRect(10, 10, 221, 441))
        self.settingsList = QTreeWidget(self.infoPanel)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.settingsList.setHeaderItem(__qtreewidgetitem)
        self.settingsList.setObjectName(u"settingsList")
        self.settingsList.setGeometry(QRect(240, 1, 141, 461))
        self.settingsList.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.infoPanel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.infoLabel.setText(QCoreApplication.translate("Form", u"$INFO", None))
    # retranslateUi


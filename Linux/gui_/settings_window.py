from PySide6.QtWidgets import QWidget 
from PySide6.QtCore import Qt 
from .gui_widget_settings import Ui_Form


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("SettingsForm")
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.horizontalLayoutWidget.setGeometry(0, 0, 381, 461)

        # Размер самой менюшки
        self.setFixedSize(381, 461)

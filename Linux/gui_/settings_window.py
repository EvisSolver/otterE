from PySide6.QtWidgets import QWidget
from .gui_widget_settings import Ui_Form


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.resize(480, 600)


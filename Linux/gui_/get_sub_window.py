from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from .get_sub import Ui_Form
from core import settings


class GetSubWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("GetSubWindow")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if not settings.LINK:
            self.ui.button_get_sub.setText("Get")
            self.ui.input_SubLink.setPlaceholderText("Paste subscription link...")
        self.ui.input_SubLink.setText(settings.LINK)

        self.setWindowTitle("SubLink")

        self.setFixedSize(260, 80)
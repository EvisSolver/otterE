from PySide6.QtWidgets import QWidget

from .get_sub import Ui_Form


class GetSubWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("SubLink")
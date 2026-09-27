import random

from .ui_for_gui import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow


class UI(QMainWindow):
    def __init__(self, server_links: list[all[dict]], total_servers: int):
        '''assign the class and inherit all the classes'''
        super().__init__()

        self.server_links = server_links
        self.total_servers = total_servers

        
        self.ui = Ui_MainWindow()
        self.settings_window = None
        self.get_sub_window = None

        self.ui.setupUi(self)
        self.ui.server_list.clear()

        self.ui_config()

    def ui_config(self):
        '''MAIN-GUI CONFIG'''
        ui = self.ui

        ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        ui.horizontalLayout.setSpacing(0)

        ui.horizontalLayout.setStretch(0, 1)
        ui.horizontalLayout.setStretch(1, 1)

# in layouts saving place under his border
        ui.horizontalLayoutWidget.setGeometry(
            3, 3, 264, 64
        )

# cleaning all standart window-elements
        ui.menubar.hide()
        ui.statusbar.hide()

        self.setFixedSize(310, 380)
        ui.centralwidget.setGeometry(0, 0, 310, 380)

# uppest panel on all weight
        ui.header.setGeometry(0, 0, 310, 50)

        ui.gearButton.setGeometry(0, 0, 51, 50)
        ui.titleLabel.setGeometry(55, 8, 200, 34)
        ui.closeButton.setGeometry(259, 0, 51, 50)

#server panel
        ui.verticalLayoutWidget.setGeometry(20, 60, 270, 200)
        ui.serverPanel.setFixedSize(270, 200)

        ui.selected_server_label.setGeometry(55, 8, 160, 42)
        ui.server_list.setGeometry(35, 60, 200, 125)

# ON/OFF on 1 vertically with server panel
        ui.toggleFrame.setGeometry(20, 280, 270, 70)
        ui.horizontalLayoutWidget.setGeometry(0, 0, 270, 70)


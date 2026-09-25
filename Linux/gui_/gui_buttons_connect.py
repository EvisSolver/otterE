from .settings import server_status
from .gui_main_window_config import UI


class Buttons_Connect(UI):
    '''connect the buttons'''
    def __init__(self, server_links, total_servers):
        super().__init__(server_links, total_servers)
        self.connect_signals()

    def connect_signals(self):
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.gearButton.clicked.connect(self.on_gearButton)

        self.ui.onButton.clicked.connect(self.on_click)
        self.ui.offButton.clicked.connect(self.off_click)

from .settings import server_status
from .gui_main_window_config import UI


class Buttons_Connect(UI):
    '''connect the buttons'''
    def __init__(self, server_links, total_servers):
        super().__init__(server_links, total_servers)

        self._settings_signals_bound = False
        self._sublink_signals_bound = False

        self.connect_signals()

#GUI
    def connect_signals(self):
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.gearButton.clicked.connect(self.open_settings)

        self.ui.onButton.clicked.connect(self.on_click)
        self.ui.offButton.clicked.connect(self.off_click)
#SETTINGS
    def bind_settings_signals(self):
        if self._settings_signals_bound: return
        if self.settings_window is None: return

        self.settings_window.ui.settingsList.itemClicked.connect(self.setting_clicked)

        self._settings_signals_bound = True
#SUBLINK
    def bind_sublink_signals(self):
        if self._sublink_signals_bound: return
        if self.get_sub_window is None: return

        button = self.get_sub_window.ui.button_get_sub
        input_field = self.get_sub_window.ui.input_SubLink

        button.clicked.connect(self.get_sub_link)
        input_field.returnPressed.connect(button.click)

        self._sublink_signals_bound = True
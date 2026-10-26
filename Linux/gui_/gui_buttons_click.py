import subprocess, os, sys, asyncio

from PySide6.QtCore import Qt, QSize, QTranslator #TODO
from PySide6.QtWidgets import QTreeWidgetItem, QApplication
from PySide6.QtGui import QIcon

from qasync import asyncSlot
from pathlib import Path

from core import settings, subscription, xray, storage

from .settings_window import SettingsWindow
from .gui_buttons_connect import Buttons_Connect
from .get_sub_window import GetSubWindow
from .show_errors import show_error

from pystyle import Colors, Write

_HERE = Path(__file__).resolve().parent
sys.path.append(str(_HERE))
sys.path.append(str(_HERE.parent))
from core import settings

class Buttons_Click(Buttons_Connect):
    '''Button-click logic + design params(49:98)'''
    
    def __init__(self, server_links: list[all[dict]], total_servers: int):
        super().__init__(server_links, total_servers)
        self.process = None

        self.set_theme("main_theme_.qss")
        self.set_close_button()
        self.load_local_servers()

    def load_local_servers(self):
        servers = []    
        try:
            files = [f for f in os.listdir(settings.path_to_jsons) if os.path.isfile(os.path.join(settings.path_to_jsons, f)) and f.endswith(".json")]
            if len(files):
                Write.Print(f"{len(files)} local servers found", Colors.green, interval = 0)
                for file in files:
                    print(file)
                    # subprocess.Popen(f"xray run -c {file}", shell = True)
                    servers.append(file)
                    self.ui.server_list.addItem(f"{file[:-5]}")
            else: Write.Print("local servers not found", Colors.yellow, interval = 0)
        except Exception as error:
            Write.Print(error, Colors.red, interval = 0)
        return servers
    
#GET_SUB_LINK_BUTTON
    @asyncSlot()
    @show_error
    async def get_sub_link(self):
        settings.LINK = (
            self.get_sub_window.ui.input_SubLink.text()
        )
        with open(
            settings.path_to_create_memory_file,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(settings.LINK)

        server_links, total_servers = await subscription.get_links()
        clean_list = await subscription.get_clean_link(server_links)

        dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)

        clean_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers)
        full_clean_jsons = await xray.get_clean_json()

        self.server_links = clean_list
        self.total_servers = total_servers
        
        self.ui.server_list.clear()

        for self.server in self.server_links:
             self.flag = self.server["server_flag"]
             self.name = self.server["server_name"]

             print(self.flag, self.name)
             self.ui.server_list.addItem(f"{self.flag} | {self.name}")


#MAIN MENU
    def on_click(self):
        '''func to "ON" button'''

        try:
            current_server = self.ui.server_list.currentItem()
            self.name_with_no_flag = current_server.text().split("|")[-1].strip()

            self.ui.selected_server_label.setText(current_server.text())
            self.ui.titleLabel.setText("IS WORKING...")

            if current_server is not None:
                print("server picked ", current_server.text(), self.name_with_no_flag)
                self.process = subprocess.Popen(f"xray run -c '{settings.path_to_jsons}{self.name_with_no_flag}.json'", shell = True)
                self.set_border_state("on")
            else: 
                self.set_border_state("off")
                Write.Print("server_not_picked", Colors.red, interval = 0)

        except Exception as error: Write.Print(f"Unknown Error in |ON| : {error}", Colors.red, interval = 0)


    def off_click(self):
        '''func to "ON" button'''
        try:
            self.process.terminate()
            subprocess.run("pkill -f xray", shell = True)
            Write.Print(f"\n\nSERVER |{self.name_with_no_flag}| IS OFF\n", Colors.green, interval = 0)

            self.ui.titleLabel.setText("IS NOT WORKING")
            self.ui.selected_server_label.setText("$SERVER")

            self.set_border_state("off")

        except Exception as error: Write.Print(f"Unknown Error in |OFF| : {error}", Colors.red, interval = 0)


#SETTINGS
    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()

            self.rebuild_settings_tree()
            self.bind_settings_signals()

        self.settings_window.show()
        self.settings_window.raise_()
        self.settings_window.activateWindow()


#SubLink
    def open_sublink(self):
        if self.get_sub_window is None:
            self.get_sub_window = GetSubWindow()
            self.bind_sublink_signals()
            
        self.get_sub_window.show()
        self.get_sub_window.raise_()
        self.get_sub_window.activateWindow()

#ADDING the tree-lists-buttons in settings
    def rebuild_settings_tree(self):
        "translator"
        self.tree = self.settings_window.ui.settingsList
        self.tree.clear()
        self.tree.setHeaderHidden(True)
        self.tree.setIndentation(0)

        theme = QTreeWidgetItem([self.tr("Theme")])
        theme.setData(0, Qt.ItemDataRole.UserRole, "theme")

        themes = {
            "Galaxy": "galaxy_theme_.qss",
            "Cute": "cute_theme_.qss",
            "Black": "black_theme_.qss"
        }

        for text_theme, file_name in themes.items():
            item_theme = QTreeWidgetItem([self.tr(text_theme)])
            item_theme.setData(0, Qt.ItemDataRole.UserRole, f"Theme:{file_name}")

            theme.addChild(item_theme)
        

        language = QTreeWidgetItem([self.tr("Language")])
        language.setData(0, Qt.ItemDataRole.UserRole, "Language")

        languages = {
            "English": "en",
            "Русский": "ru",
            "Ukraine": "ua"
        }

        for text, code in languages.items():
            item = QTreeWidgetItem([self.tr(text)])
            item.setData(0, Qt.ItemDataRole.UserRole, f"language: {code}")
            language.addChild(item)

        sublink = QTreeWidgetItem([self.tr("SubLink")])
        sublink.setData(0, Qt.ItemDataRole.UserRole, "sublink")

        self.tree.addTopLevelItem(theme)
        self.tree.addTopLevelItem(language)
        self.tree.addTopLevelItem(sublink)

#SETTINGS(IN)-BUTTONS
    def setting_clicked(self, item: str):
        """setting-menu opening"""
        text = item.text(0)
        label = self.settings_window.ui.infoLabel

        label.setWordWrap(True)
        label.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop
        )
            
        if text == "Theme" and item.parent() is None:
            self.settings_window.ui.infoLabel.setText('changing the "Theme" for your comfortable')

        if text == "SubLink":
            self.open_sublink()

        theme_action = item.data(0, Qt.ItemDataRole.UserRole)
        if isinstance(theme_action, str):
            if theme_action.startswith("Theme:"):
                file_name = theme_action.split(":", 1)[1]
                self.set_theme(file_name)
                return
            
#CLOSE-BUTTON
    def set_close_button(self):
        self.ui.closeButton.setText("")
        self.ui.closeButton.setIcon(
            QIcon("Themes_/images_/close_button_ico.png")
        )
        self.ui.closeButton.setIconSize(QSize(36, 36))



#SET-THEMES
    def set_theme(self, theme_file):
        with open(
            f"Themes_/{theme_file}",
            "r",
            encoding = "utf-8"
        ) as file:
            QApplication.instance().setStyleSheet(file.read())


    def set_border_state(self, state):
        self.ui.centralwidget.setProperty(
            "state",
            state
        )

        widgets = [
            self.ui.centralwidget,
            self.ui.header,
            self.ui.serverPanel,
            self.ui.selected_server_label,
            self.ui.titleLabel,
            self.ui.server_list,
        ]

        for widget in widgets:
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
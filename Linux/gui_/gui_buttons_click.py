import subprocess, os, sys, asyncio

from PySide6.QtCore import Qt, QSize, QTranslator #TODO
from PySide6.QtWidgets import QTreeWidgetItem, QApplication
from PySide6.QtGui import QIcon

from qasync import asyncSlot
from pathlib import Path

from languages_.change_lang import load_language

from core import settings, subscription, xray, storage

from sing_box_path import path_to_sing_jsons
from .settings_window import SettingsWindow
from .gui_buttons_connect import Buttons_Connect
from .get_sub_window import GetSubWindow
from .show_errors import show_error

from sing_box_core.sing_box import start_sing_box, kill_sing_box

from pystyle import Colors, Write

_HERE = Path(__file__).resolve().parent
sys.path.append(str(_HERE))
sys.path.append(str(_HERE.parent))
from core import settings


# === Buttons ===
class Buttons_Click(Buttons_Connect):
    '''Button-click logic + design params(49:98)'''
    
    def __init__(self, server_links: list[all[dict]], total_servers: int):
        print("window-obj added")
        super().__init__(server_links, total_servers)
        self.sing_box_process = None
        self.process = None

        self.set_theme("main_theme_.qss")
        self.set_close_button()
        self.load_local_servers()

    def load_local_servers(self): # -- Check on Local Servers | No have - Skip | Have - Adding
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
    
# -- GET_SUB_LINK_BUTTON --
    @asyncSlot()
    @show_error
    async def get_sub_link(self):
        '''Gets Link and adding servers'''
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

# --- TUN Button's ---
    def TUN_button_pressed(self): # -- Starting Sing-box
        '''TUN ON'''
        try:
            current_server = self.ui.server_list.currentItem()
            if current_server is not None:
                self.name_with_no_flag = current_server.text().split("|")[-1].strip()
                print("server picked ", self.name_with_no_flag)
                print(path_to_sing_jsons)
                start_sing_box(f"{path_to_sing_jsons}{self.name_with_no_flag}.json")
        except subprocess.CalledProcessError as error:
            with open("errors.log", "w", encoding="utf-8") as log_file:
                log_file.write(
                    f"{'--' * 10}\nError: {error}\n"
                    f"STDERR:\n{error.stderr}\n"
                    f"STDOUT:\n{error.stdout}\n"
                    f"{'--' * 10}\n"
                )
    def TUN_button_released(self): # -- Kills sing-box when TUN OFF
        kill_sing_box()
        self.set_border_state("TUN_OFF")
        
    def TUN_button_toggler(self, checked): # -- Toggling TUN button's ON/OFF
        print("TUN BUTTON:", checked,
          "process:", getattr(self, "sing_box_process", None))
        if checked: 
            self.TUN_button_pressed()
            self.set_border_state("TUN_ON")
        elif not checked: self.TUN_button_released()

# --- PROXY Button's ---
    def PROXY_button_pressed(self): # -- Starting Xray
        '''ON PROXY'''
        try:
            self.current_server = self.ui.server_list.currentItem()
            self.name_with_no_flag = self.current_server.text().split("|")[-1].strip()  
            self.ui.selected_server_label.setText(self.current_server.text())
            self.ui.titleLabel.setText("IS WORKING...")
            
            if self.current_server is not None:
                print("server picked ", self.current_server.text(), self.name_with_no_flag)
                self.process = subprocess.Popen(f"xray run -c '{settings.path_to_jsons}{self.name_with_no_flag}.json' &", shell = True)
                self.set_border_state("PROXY_ON")
        except Exception as error: Write.Print(f"Unknown Error in |ON| : {error}", Colors.red, interval = 0)
                
    def PROXY_button_released(self): # -- Killing Xray
        '''OFF PROXY'''
        xray.kill_xray_core()
        self.set_border_state("PROXY_OFF")
    def PROXY_button_toggler(self, checked): # -- Toggling Xray button's ON/OFF
        if checked: self.PROXY_button_pressed()
        if not checked: self.PROXY_button_released()

# --- SETTINGS ---
    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()

            self.rebuild_settings_tree()
            self.bind_settings_signals()

        self.settings_window.show()
        self.settings_window.raise_()
        self.settings_window.activateWindow()


# --- SubLink ---
    def open_sublink(self):
        if self.get_sub_window is None:
            self.get_sub_window = GetSubWindow()
            self.bind_sublink_signals()
            
        self.get_sub_window.show()
        self.get_sub_window.raise_()
        self.get_sub_window.activateWindow()

# -- Tree-Lists-Buttons in Settings --
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
            item_theme.setData(0, Qt.ItemDataRole.UserRole, f"theme:{file_name}")

            theme.addChild(item_theme)
        

        language = QTreeWidgetItem([self.tr("Language")])
        language.setData(0, Qt.ItemDataRole.UserRole, "language")

        languages = {
            "English": "en",
            "Русский": "ru",
            "Ukraine": "ua"
        }

        for text, code in languages.items():
            item = QTreeWidgetItem([self.tr(text)])
            item.setData(0, Qt.ItemDataRole.UserRole, f"language:{code}")
            language.addChild(item)

        sublink = QTreeWidgetItem([self.tr("SubLink")])
        sublink.setData(0, Qt.ItemDataRole.UserRole, "sublink")

        self.tree.addTopLevelItem(theme)
        self.tree.addTopLevelItem(language)
        self.tree.addTopLevelItem(sublink)

# -- SETTINGS(IN)-BUTTONS --
    def setting_clicked(self, item, column=0):
        action = item.data(0,Qt.ItemDataRole.UserRole)

        if action == "theme":
            self.settings_window.ui.infoLabel.setText(self.tr('Changing the "Theme"'))
            return

        if action.startswith("theme:"):
            file_name = action.split(
                ":", 1)[1]
            self.set_theme(file_name)
            return

        if action == "language":
            item.setExpanded(not item.isExpanded())
            return

        if action.startswith("language:"):
            code = action.split(":", 1)[1]

            self.set_language(code)
            return

        if action == "sublink":
            self.open_sublink()

# --- SET LANG ---
    def set_language(self, code):
        if not load_language(code): return
        self.ui.retranslateUi(self)
        if self.settings_window is not None:
            self.settings_window.ui.retranslateUi(self.settings_window)
            self.rebuild_settings_tree()
        if self.get_sub_window is not None: self.get_sub_window.ui.retranslateUi(self.get_sub_window)
            
# --- CLOSE-BUTTON ---
    def set_close_button(self):
        self.ui.closeButton.setText("")
        self.ui.closeButton.setIcon(
            QIcon("Themes_/images_/close_button_ico.png")
        )
        self.ui.closeButton.setIconSize(QSize(36, 36))
        kill_sing_box()
        xray.kill_xray_core()


# --- SET-THEMES ---
    def set_theme(self, theme_file):
        with open(
            f"Themes_/{theme_file}",
            "r",
            encoding = "utf-8"
        ) as file:
            QApplication.instance().setStyleSheet(file.read())


# --- SET-BORDER-STATE ---
    def set_border_state(self, state):
        if state.startswith("PROXY_"):
            self.ui.centralwidget.setProperty(
                "PROXY_state",
                state
            )

        elif state.startswith("TUN_"):
            self.ui.centralwidget.setProperty(
                "TUN_state",
                state
            )

        print(
            state,
            self.ui.centralwidget.property("PROXY_state"),
            self.ui.centralwidget.property("TUN_state")
        )

        widgets = [
            self.ui.centralwidget,
            self.ui.header,
            self.ui.serverPanel,
            self.ui.selected_server_label,
            self.ui.titleLabel,
            self.ui.server_list,
            self.ui.onButton,
            self.ui.offButton,
        ]

        for widget in widgets:
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()
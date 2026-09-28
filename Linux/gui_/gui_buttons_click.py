import subprocess, sys, asyncio

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem

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

#MAIN MENU
    def on_click(self):
        '''func to "ON" button'''

        current_server = self.ui.server_list.currentItem()
        self.name_with_no_flag = current_server.text().split("|")[-1].strip()

        self.ui.selected_server_label.setText(current_server.text())
        self.ui.titleLabel.setText("IS WORKING...")

        self.set_border_state("#238B06")
        if current_server is not None:
            print("server picked ", current_server.text(), self.name_with_no_flag)
            self.process = subprocess.Popen(f"xray run -c '{settings.path_to_jsons}{self.name_with_no_flag}.json'", shell = True)
        else: Write.Print("server_not_picked", Colors.red, interval = 0)

    def off_click(self):
        '''func to "ON" button'''

        self.process.terminate()
        subprocess.run("pkill -f xray", shell = True)
        Write.Print(f"\n\nSERVER |{self.name_with_no_flag}| IS OFF\n", Colors.green, interval = 0)

        self.ui.titleLabel.setText("IS NOT WORKING")
        self.ui.selected_server_label.setText("$SERVER")

        self.set_border_state("#C10404")


#GET_SUB_LINK_BUTTON
    @show_error
    def get_sub_link(self):
        settings.LINK = (
            self.get_sub_window.ui.input_SubLink.text()
        )

        with open(
            settings.path_to_create_memory_file,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(settings.LINK)

        server_links, total_servers = asyncio.run(subscription.get_links())
        clean_list = asyncio.run(subscription.get_clean_link(server_links))

        dirty_jsons = asyncio.run(xray.get_dirty_json(clean_list, total_servers))

        clean_list, total_servers = asyncio.run(storage.create_file(clean_list, dirty_jsons, total_servers))
        full_clean_jsons = asyncio.run(xray.get_clean_json())

        self.server_links = clean_list
        self.total_servers = total_servers
        
        self.ui.server_list.clear()

        for self.server in self.server_links:
             self.flag = self.server["server_flag"]
             self.name = self.server["server_name"]

             print(self.flag, self.name)
             self.ui.server_list.addItem(f"{self.flag} | {self.name}")


#SETTINGS
    def open_settings(self):
        '''func to "open_settings(left-up button in main-gui)" button'''
        
        if self.settings_window is None:
            self.settings_window = SettingsWindow()

            tree = self.settings_window.ui.settingsList
            tree.setIndentation(0)
            
            tree.clear()
            tree.setHeaderHidden(True)


            language = QTreeWidgetItem(["Language"])
            language.addChild(QTreeWidgetItem(["English"]))
            language.addChild(QTreeWidgetItem(["Русский"]))
            language.addChild(QTreeWidgetItem(["Ukraine"]))

            theme = QTreeWidgetItem(["Theme"])
            proxy = QTreeWidgetItem(["SubLink"])

            tree.addTopLevelItem(theme)
            tree.addTopLevelItem(language)
            tree.addTopLevelItem(proxy)

            tree.itemClicked.connect(self.setting_clicked)

        self.settings_window.show()
        self.settings_window.move(
            self.x() + self.width() + 10,
            self.y()
        )

    def setting_clicked(self, item: str):
        text = item.text(0)
        label = self.settings_window.ui.infoLabel

        self.settings_window.ui.infoLabel.setStyleSheet("""
            QLabel {
                color: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                    stop:0 #00FF00, stop:1 #00FFFF);
                font-weight: bold;
            }
        """)

        label.setWordWrap(True)
        label.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop
        )

        if text == "Language" and item.parent() is None:
            item.setExpanded(not item.isExpanded())
            label.setText("changing your language")
        elif item.parent() is not None:
            print("Выбран язык:", text)
            
        if text == "Theme" and item.parent() is None:
            self.settings_window.ui.infoLabel.setText('changing the "Theme" for your comfortable')

        if text == "SubLink":
            if self.get_sub_window is None:
                self.get_sub_window = GetSubWindow()
            self.get_sub_window.show()
            self.get_sub_window.raise_()
            self.get_sub_window.activateWindow()

            button = self.get_sub_window.ui.button_get_sub
            input_field = self.get_sub_window.ui.input_SubLink

            button.clicked.connect(self.get_sub_link)
            input_field.returnPressed.connect(button.click)


#MAIN-COLORS
    def set_border_state(self, color: Colors):

        self.ui.centralwidget.setStyleSheet(f"""
            QFrame#header {{
                background-color: #0d011d;
                border: 3px solid {color};
            }}

            QFrame#serverPanel {{
                background-color: #0d011d;
                border: 3px solid {color};
            }}


            QLabel#selected_server_label {{
                border: 3px solid {color};
            }}

            QLabel#titleLabel {{
                border: 3px solid {color};
            }}

            QListWidget#server_list {{
                border: 3px solid {color};
            }}

            QToolButton#gearButton, QPushButton#closeButton {{
                border: 3px solid {color};  
            }}
        """)            

        self.ui.server_list.setStyleSheet(f"""

            QListWidget#server_list::item {{
            border-bottom: 3px solid #2E0054;
            }}

        """)


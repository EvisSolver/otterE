import subprocess, sys, random

from PySide6.QtWidgets import QWidget
from pathlib import Path

from .gui_buttons_connect import Buttons_Connect
from pystyle import Colors, Write

_HERE = Path(__file__).resolve().parent
sys.path.append(str(_HERE))
sys.path.append(str(_HERE.parent))
from core import settings


class Buttons_Click(Buttons_Connect):
    '''Button-click logic + design params(49:98)'''
    def __init__(self, server_links, total_servers):
        super().__init__(server_links, total_servers)

    def on_click(self):

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
        self.process.terminate()
        subprocess.run("pkill -f xray", shell = True)
        Write.Print(f"\n\nSERVER |{self.name_with_no_flag}| IS OFF\n", Colors.green, interval = 0)

        self.ui.titleLabel.setText("IS NOT WORKING")
        self.ui.selected_server_label.setText("$SERVER")

        self.set_border_state("#C10404")

    def on_gearButton(self):
        print("settings")

    def set_border_state(self, color):

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


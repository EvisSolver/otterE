from pathlib import Path
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from .gui_buttons_click import Buttons_Click


def main(server_links: list[all[dict]], total_servers: int):
    '''main gui-app'''
    window = Buttons_Click(server_links, total_servers)
    window.show()

    return window
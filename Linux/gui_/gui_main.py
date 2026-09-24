import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from .gui_buttons_click import Buttons_Click


def main(server_links, total_servers):
    app = QApplication.instance() or QApplication(sys.argv)

    style_path = Path(__file__).with_name("style.qss")
    if style_path.exists():
        app.setStyleSheet(
            style_path.read_text(encoding = "utf-8")
        )

    window = Buttons_Click(server_links, total_servers)
    window.show()

    return app.exec()
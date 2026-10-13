import asyncio
import os
import sys

import load_saved_servers_

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from gui_.gui_buttons_click import Buttons_Click

from pathlib import Path
from core import settings, subscription, xray, storage
from ui import console, picker

from gui_.gui_main import main as gui_main


async def app_main(app):

    os.makedirs(settings.path_to_jsons, exist_ok=True)

    server_links, total_servers = await load_saved_servers_.load_saved_servers()

    window = Buttons_Click(server_links, total_servers)
    window.show()

    quit_event = asyncio.Event()
    
    app.aboutToQuit.connect(quit_event.set)
    await quit_event.wait()

    # GUI нельзя await'ить: это обычная функция, внутри неё блокирующий app.exec().
    # Возвращает код выхода, поэтому отдаём его наружу.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    with loop:
        loop.run_until_complete(app_main(app))
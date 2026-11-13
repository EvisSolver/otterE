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
from installer import installer

from gui_.gui_main import main as gui_main


async def app_main(app):
    installer()

    server_links, total_servers = (
        await load_saved_servers_.load_saved_servers()
    )
    window = gui_main(
        server_links,
        total_servers
    )

    return window

    # -- GUI нельзя await'ить: это обычная функция, внутри неё блокирующий app.exec().
    # -- Возвращает код выхода, поэтому отдаём его наружу.


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    app.aboutToQuit.connect(
        loop.stop
    )

    with loop:
        window = loop.run_until_complete(
            app_main(app)
        )

        loop.run_forever()
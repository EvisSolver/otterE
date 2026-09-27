import asyncio
import os
import sys
from pathlib import Path

from core import settings, subscription, xray, storage
from ui import console, picker

from gui_.gui_main import main as gui_main


def app_main():

    os.makedirs(settings.path_to_jsons, exist_ok=True)
    return gui_main([], 0)

    # GUI нельзя await'ить: это обычная функция, внутри неё блокирующий app.exec().
    # Возвращает код выхода, поэтому отдаём его наружу.


if __name__ == "__main__":
    sys.exit(app_main())
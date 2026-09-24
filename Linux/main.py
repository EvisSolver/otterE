import asyncio
import os
import sys
from pathlib import Path

from core import settings, subscription, xray, storage
from ui import console, picker

from gui_.gui_main import main as gui_main


async def app_main():

    os.makedirs(settings.path_to_jsons, exist_ok=True)
    server_links, total_servers = await subscription.get_links()
    clean_list = await subscription.get_clean_link(server_links)
    print(clean_list)
    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)
    clean_link_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers)
    full_clean_json = await xray.get_clean_json()
   
    return gui_main(clean_list, total_servers)

    # GUI нельзя await'ить: это обычная функция, внутри неё блокирующий app.exec().
    # Возвращает код выхода, поэтому отдаём его наружу.


if __name__ == "__main__":
    sys.exit(asyncio.run(app_main()))

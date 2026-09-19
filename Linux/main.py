import asyncio, os, sys

from core import settings, subscription, xray, storage
from ui import console, picker


async def main():

    os.makedirs(settings.path_to_jsons, exist_ok=True)
    server_links, total_servers = await subscription.get_links()
    clean_list = await subscription.get_clean_link(server_links)
    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)

    await storage.create_file(clean_list, dirty_jsons, total_servers)
    await console.loading(clean_list)
    await picker.pick(clean_list, total_servers)


if __name__ == "__main__":
    asyncio.run(main())
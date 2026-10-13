from core import settings, subscription, xray, storage


async def load_saved_servers():
    try:
        with open(
            settings.path_to_create_memory_file,
            "r", encoding = "utf-8"
        ) as file: settings.LINK = file.read().strip()

    except FileNotFoundError: settings.LINK = ""

    if not settings.LINK: return [], 0


    server_links, total_servers = await subscription.get_links()
    clean_list = await subscription.get_clean_link(server_links)
    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)
    clean_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers)

    await xray.get_clean_json()

    return clean_list, total_servers
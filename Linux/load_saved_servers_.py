import base64
from core import settings, subscription, xray, storage
from load_local_servers_ import load_local_servers


async def load_saved_servers():
    local_servers, total_servers = load_local_servers()
    if total_servers > 0: return local_servers, total_servers
    
    try:
        with open(
            settings.path_to_create_memory_file,
            "r", encoding = "utf-8"
        ) as file_text:
            encoded_bytes = base64.b64encode(file_text.read().encode("utf-8"))
            settings.LINK = file_text.read().strip()
        decoded_bytes = base64.b64decode(encoded_bytes.decode())


    except FileNotFoundError: settings.LINK = ""

    if not settings.LINK: return [], 0


    server_links, total_servers = await subscription.get_links()
    clean_list = await subscription.get_clean_link(server_links)
    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)
    clean_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers)

    await xray.get_clean_json()

    return clean_list, total_servers
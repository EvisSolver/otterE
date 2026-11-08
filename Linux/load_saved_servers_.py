from core import settings, subscription, xray, storage
from load_local_servers_ import load_local_servers

from sing_box_core.get_sing_box_json import vless_link_to_sing_box_dirty_json
from sing_box_core.converter import dirty_json_to_clean_json_sing_box
from sing_box_core.create_files_jsons import create_jsons

from pystyle import Colors, Write

async def load_saved_servers():
    try:
        with open(
            settings.path_to_create_memory_file,
            "r", encoding = "utf-8"
        ) as file_text: 
            print(file_text)
            settings.LINK = file_text.read().strip()
            
            # encoded_bytes = base64.b64encode(file_text.read().encode("utf-8"))
        # decoded_bytes = base64.b64decode(encoded_bytes.decode())
    
    except Exception as e: print(e)
    # FileNotFoundError: settings.LINK = ""

    total_servers = load_local_servers()
    
    if not settings.LINK: return [], 0


    server_links, total_servers = await subscription.get_links()
    clean_list = await subscription.get_clean_link(server_links)
    # print(clean_list)
    print("-" * 100)
    dirty_jsons = [
        await vless_link_to_sing_box_dirty_json(item["server_link"])   # без await
        for item in clean_list
    ]
    print("=" * 100, "\n", clean_list)
    clean_json = await dirty_json_to_clean_json_sing_box(dirty_jsons)
    for server in clean_list:
        print(server["server_name"])
        json_in_file = await create_jsons(f"{server["server_name"]}.json", [dirty_json for dirty_json in dirty_jsons])
        
        

    print("-" * 100)
    print(dirty_jsons)
    # print(singbox_outbounds)

    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers)
    clean_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers)

    await xray.get_clean_json()

    return clean_list, total_servers
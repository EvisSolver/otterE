from core import settings, subscription, xray, storage
from load_local_servers_ import load_local_servers

from sing_box_path import path_to_sing_jsons

from sing_box_core.get_sing_box_json import vless_link_to_sing_box_dirty_json
from sing_box_core.converter import dirty_json_to_clean_json_sing_box
from sing_box_core.create_files_jsons import create_jsons

from pystyle import Colors, Write


# --- Load Local Servers ---
async def load_saved_servers():
    '''Checking local-servers on PC and responsible for sing-box
       If Local servers not founded - skip
       If Local server founded - Already Add in the list    
    '''
    try:
        with open(
            settings.path_to_create_memory_file,
            "r", encoding = "utf-8"
        ) as file_text: 
            # print(file_text)
            settings.LINK = file_text.read().strip() # -- Reading the file and Using link for Auto-Load server's
    
    except Exception as e: print(e)
    # FileNotFoundError: settings.LINK = ""
    total_servers = load_local_servers() # -- Loading Local Servers

    if not settings.LINK: return [], 0
    server_links, total_servers = await subscription.get_links() # -- Getting dirty-Links
    clean_list = await subscription.get_clean_link(server_links) # -- Getting clean-Links
    # print(clean_list)
    dirty_jsons = [
        await vless_link_to_sing_box_dirty_json(item["server_link"]) # -- Gets dirty-Jsons
        for item in clean_list
    ]
    # print("\n", "-" * 100)
    # print([dirty_json for dirty_json in dirty_jsons])
    # print("-" * 100", "\n")

# -- Sing-box --
    for server, dirty_json in zip(clean_list, dirty_jsons): # -- Gets Server-name's + Fixing invalid-name's
        # print(server["server_name"].replace("/", "_"))
        server_name = server["server_name"].replace("/", "_")
        dirty_json["tag"] = "vless-reality" # -- Changing tag on 'vless-reality' for stability work
        # Write.Print("-" * 100, Colors.purple, interval = 0)
        # print(dirty_json)
        # Write.Print("-" * 100, Colors.purple, interval = 0)
        
        clean_json = await dirty_json_to_clean_json_sing_box(dirty_json) # -- Gets clean-Jsons for start sing-box
        json_in_file = await create_jsons(f"{server_name}", clean_json, path_to_sing_jsons) # -- Creating files with clean .json f for picking servers and starting
        # Write.Print("-" * 100, Colors.blue, interval = 0)
        # print(json_in_file)
        # Write.Print("-" * 100, Colors.blue, interval = 0)
        
        Write.Print("\n=" * 5, Colors.orange, interval = 0)
        Write.Print("=\n" * 5, Colors.orange, interval = 0)

    # print("-" * 100)
    # print(dirty_jsons)
    # print(singbox_outbounds)
    
# -- Xray --
    dirty_jsons = await xray.get_dirty_json(clean_list, total_servers) # -- Gets dirty-Jsons
    clean_list, total_servers = await storage.create_file(clean_list, dirty_jsons, total_servers) # -- Gets Clean List with Server-names&Clean-server-link's&...

    await xray.get_clean_json() # -- Gets clean-Jsons to start xray

    return clean_list, total_servers
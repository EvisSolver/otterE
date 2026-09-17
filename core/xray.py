import subprocess, json
from pystyle import Colors, Write

from .settings import path_to_xray_link


async def get_dirty_json(clean_link_list: list, total_servers: int) -> list:
    '''
        getting dirty_json to make clean_json(for xray run -c)
    '''

    dirty_jsons = []

    for clean_link in clean_link_list[0:total_servers + 1]:
        Write.Print(f"\n{'=' * 150}\n", Colors.blue, interval = 0)
        Write.Print(f"""
        
        server  | {clean_link['server_id']}
        region  | {clean_link['server_flag']}
        name    | {clean_link['server_name']}
\n""", Colors.yellow, interval = 0)

        command_for_dirty_json = f"cd {path_to_xray_link} && ./Xray-Link-Json '{clean_link['server_link']}'"
        result_for_dirty_json = subprocess.run(
            command_for_dirty_json,
            shell = True, capture_output = True, text = True
        )
        full_output_for_dirty_json = result_for_dirty_json.stdout
        dirty_jsons.append(full_output_for_dirty_json)

    return dirty_jsons


async def get_clean_json(server_name) -> dict:
    '''
        making dirty_json to clean_json with adding work-parameters(config) in .json
    '''
    
    clean_json = f"{server_name}.json"

    with open(
        clean_json,
        encoding = "utf-8"
    ) as file:
        json_config = json.load(file)

    json_config["inbounds"] = [
        {
            "listen": "127.0.0.1", "port": 10808,
            "protocol": "socks",

            "settings": {"udp": True},
            "tag": "socks-in"
        },
        {
        "listen": "127.0.0.1", 
        "port": 10809,
        "protocol": "http",
        "settings": {},
        "tag": "http-in"
        }
    ]

    json_config["outbounds"][0]["sendThrough"] = "0.0.0.0"

    with open(
        clean_json, "w", encoding = "utf-8"
    ) as file:
        json.dump(json_config, file, ensure_ascii = False, indent = 2) 
    return json_config


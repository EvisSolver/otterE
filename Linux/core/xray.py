import subprocess, json

from pathlib import Path
from pystyle import Colors, Write

from .settings import path_to_xray_link, path_to_jsons


async def get_dirty_json(clean_link_list: list[all[dict]], total_servers: int) -> list:
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


async def get_clean_json() -> list[all[dict]]:
    '''
        дописывает inbounds / sendThrough во ВСЕ jsons/*.json
    '''
    inbounds = [
        {"listen": "127.0.0.1", "port": 10808, "protocol": "socks",
         "settings": {"udp": True}, "tag": "socks-in"}
    ]

    configs = []
    for clean_json in Path(path_to_jsons).glob("*.json"):
        try:
            json_config = json.loads(clean_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            Write.Print(f"\n[skip] {clean_json.name}: невалидный json\n", Colors.red, interval=0)
            continue

        json_config["inbounds"] = inbounds
        json_config["outbounds"][0]["sendThrough"] = "0.0.0.0"

        clean_json.write_text(
            json.dumps(json_config, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        configs.append(json_config)

    return configs

def kill_xray_core():
    subprocess.run("pkill -9 xray", shell = True)
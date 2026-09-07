import os
import json, asyncio

from main import get_dirty_json


async def config_main(): #TODO разобраться со структурой
    dirty_json = await get_dirty_json()

    clear_json = "_.json"

    with open(
        clear_json,
        encoding = "utf-8"
    ) as file:
        cfg = json.load(file)


    cfg["inbounds"] = [
        {
            "listen": "127.0.0.1", "port": 10808,
            "protocol": "socks",

            "settings": {"udp": True}, "tag": "socks-in"
        }
    ]

    cfg["outbounds"][0]["sendThrough"] = "0.0.0.0"

    with open(clear_json, "w", encoding = "utf-8") as file:
        json.dump(cfg, file, ensure_ascii = False, indent = 3)

    with open(clear_json, encoding = "utf-8") as file:
        result = json.load(file)

    #TODO if os.system(xray run -c): print("on") else: print("off")"
    os.system(f"xray run -c {clear_json}")
    print(json.dumps(result, ensure_ascii = False))

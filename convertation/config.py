# ROADMAP: получаю чистые ссылки => забрасываю в Xray-Link-Json => обрабатываю полученный json, превращая ее в работающий => xray run -c "...".json
import json, asyncio#TODO
from main import get_dirty_json


async def get_clean_json(server_name):
    clear_json = f"{server_name}.json"#TODO
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

    return result
import json


clear_json = "_.json"

with open(
    "asd.json",
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

print(json.dumps(result, ensure_ascii = False))
from convertation.settings import *


def converter(json_dict):
    protocol = json_dict["protocol"].lower()
    settings = json_dict["settings"]

    if protocol == "vless":
        settings = VlessSettings(
            settings["address"],
            settings["port"],
            settings["id"],

            settings.get("encryption", "none"),
            settings.get("flow")
        )

    elif protocol == "vmess":
        settings = VmessSettings(
            settings["address"],
            settings["port"],
            settings["id"],

            settings.get("alterId", 0),
            settings.get("security", "auto")
        )

    elif protocol == "shadowsocks":
        settings = ShadowsocksSettings(
            settings["address"],
            settings["port"],

            settings["method"],
            settings["password"]
        )

    elif protocol == "trojan":
        settings = TrojanSettings(
            settings["address"],
            settings["port"],

            settings["password"]
        )

    else:
        raise ValueError(f"Unknown protocol: {protocol}")

    return protocol, settings
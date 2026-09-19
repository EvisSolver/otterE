import requests, base64, emoji
from urllib.parse import unquote

from .emoji_founder import get_emoji
from .settings import LINK


async def get_links() -> tuple[dict[str], str]:
    '''
        decoding sub-LINK
        counting servers
        splitting to n lists and returning the dict
    '''

    servers_list = []
    server_ = {}

    response = requests.get(LINK)
    decoded_bytes = base64.b64decode(response.text)
    decoded_text = decoded_bytes.decode("utf-8")
    servers = decoded_text.splitlines()

    total_servers = 0

    for server in servers:
        servers_list.append(server)
        if "://" in server:
            total_servers += 1

            name_flag = unquote(server.split("#")[1]).strip() if "#" in server else "unknown"
            name = emoji.replace_emoji(name_flag, replace = "").strip()
            if " " in name: name = name.replace(" ", "_")

            server_[total_servers] = {
                "name": name,
                "flag": name_flag,
                "link": server,
                "clean_link": server.split("#", 1)[0]
            }
    return server_, total_servers


async def get_clean_link(server_links: dict) -> dict[all[str]]:
    '''
        decoding link(removing emoji-flag)
    '''

    clean_servers_list = []
    server_id = 0

    for _, server in server_links.items():
        emoji_, name, link = await get_emoji(
            server["name"],
            server["link"],
            server["flag"]
        )

        server_id += 1

        clean_servers_dict = {
            "server_id": server_id,
            "server_flag": emoji_,
            "server_name": name,
            "server_link": link
        }
        clean_servers_list.append(clean_servers_dict)
        print(clean_servers_dict["server_link"])
    print("\n\n")
    return clean_servers_list
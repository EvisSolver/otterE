import asyncio
import base64, requests
import emoji, json
import os, subprocess

from link import LINK

from urllib.parse import unquote
from pystyle import Colors, Write


async def emoji_founder(name: str, link: str, text: str) -> tuple[str, str, str]:
    '''
        founding emoji in text: string
        if emoji_list = True(not empty) then we are creating found_emoji which = emoji_list
        we taking first element([0]) and taking ["emoji"] (the first emoji in list)

        Example:
            emoji_list = [
                {
                    "emoji": "🇫🇮"
                }
            ]
        so: found_emoji => emoji_list[0 list-index]["emoji" name of dict]
    '''
    emoji_list = emoji.emoji_list(text)

    if emoji_list:
        found_emoji = emoji_list[0]["emoji"]
        
        return found_emoji, name, link
    return "unknown symbol/emoji"


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
        if "://" in servers_list[0]:
            total_servers += 1

            name_flag = unquote(server.split("#")[1]).strip() if "#" in server else "unknown"#  режем ссылку(берем из нее раскодируемый флаг в закодированной строке(после #))
            name = emoji.replace_emoji(name_flag, replace = "").strip()

            server_[f"Server: {total_servers}"] = {"name": name, "flag": name_flag, "link": server.split("#", 1)[0], "clean_link": server.split("#", 1)[0]}#    убираем с ссылки #%F0%9F...
    Write.Print(f"\ntotal_servers: {total_servers}\n\n", Colors.green, interval = 0)
    return server_, total_servers


async def get_clean_link(server_links: dict) -> dict[all[str]]:
    '''
        decoding link(removing emoji-flag)
    '''
    clean_servers_list = []
    server_id = 0
    
    for _, server in server_links.items():
        emoji_, name, link = await emoji_founder(server["name"], server["link"], server["flag"])


        server_id += 1
        clean_link_dict = {
            "server_id": server_id,
            "flag": emoji_,
            "server_name": name,
            "server_link": link
        }
        clean_servers_list.append(clean_link_dict)
    #Write.Print(json.dumps(clean_servers_list, ensure_ascii=False, indent=2), Colors.purple, interval = 0)
    print("\n\n")
    return clean_servers_list



async def get_dirty_json(clean_link_list: list, total_servers: int) -> list:#DONE
    '''
        getting dirty_json to make clean_json(for xray run -c)
    '''

    dirty_jsons = []

    for clean_link in clean_link_list[0:total_servers + 1]:
        Write.Print(f"\n{'NEXT SERVER':>67}\n", Colors.blue_to_green, interval = 0)
        print(f"\n{'=' * 150}\n")
        Write.Print(f"""\n
        server  | {clean_link["server_id"]}
        region  | {clean_link['flag']}
        name    | {clean_link['server_name']}
        \n""", Colors.yellow, interval = 0)

        command_for_dirty_json = f"cd ~/xra_y_theta/xra_y_link/Xray-Link-Json && ./Xray-Link-Json '{clean_link['server_link']}'"
        result_for_dirty_json = subprocess.run(
            command_for_dirty_json,
            shell = True, capture_output = True, text = True
        )
        full_output_for_dirty_json = result_for_dirty_json.stdout

        dirty_jsons.append(full_output_for_dirty_json)
        #print(f"\n{'=' * 150}")

    #Write.Print(dirty_jsons, Colors.green, interval = 0)
    return dirty_jsons
#ПЕРЕДЕЛАТЬ: 
# ПРАВИЛЬНО: программа не ждет, а переключается на другой сервер
# process = await asyncio.create_subprocess_shell(
#     command,
#     stdout=asyncio.subprocess.PIPE
# )
# stdout, _ = await process.communicate()
# 2. Используйте `aiohttp` вместо `requests`

# Если ваш скрипт скачивает подписки (subscription links) или забирает пулы ссылок (`vless://`, `vmess://`, `ss://`) с сайтов или Telegram-каналов, используйте асинхронный клиент. Обычный `requests` убьет всю скорость `async`.

# 3. Ограничивайте количество одновременных задач (`asyncio.Semaphore`)

# Если в вашем списке `total_servers` будет, например, 500 серверов, и вы запустите их все асинхронно одной пачкой, ваш компьютер или роутер может просто «захлебнуться» от количества одновременно открытых сетевых соединений или запущенных процессов.

# Для Xray-чекеров обязательно нужно ставить ограничение (лимит), например, обрабатывать максимум по 20–30 серверов одновременно:
#также в obsidian написано
#   +доделать get_clear_json(сделать или в config.py подумать посидеть)

async def main():
    server_links, total_servers = await get_links()
    clean_link_list = await get_clean_link(server_links)
    await get_dirty_json(clean_link_list, total_servers)

#requirements.txt in the future btw i still using old venv with the cuda lol
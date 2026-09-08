import asyncio
import base64, requests
import emoji, os

from urllib.parse import unquote

     
LINK = '...'


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
        
        return f"{found_emoji} | {name} | {link}"
    return "unknown symbol/emoji"


async def get_links() -> tuple[dict[str, str], str]:
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

    count_servers = 0

    for server in servers:
        servers_list.append(server)
        if "://" in servers_list[0]:
            count_servers += 1

            # result = [
            #     [server] for _ in range(count_servers)
            # ]
            name_flag = unquote(server.split("#")[1]).strip() if "#" in server else "unknown"#  режем ссылку(берем из нее раскодируемый флаг в закодированной строке(после #))
            name = emoji.replace_emoji(name_flag, replace = "").strip()
            server_[f"Server: {count_servers}"] = {"name": name, "flag": name_flag, "link": server.split("#", 1)[0], "clean_link": server.split("#", 1)[0]}
    return server_, name_flag


async def put_dirty_link(text: str) -> tuple[str, list[str]]:
    '''
        analyzing the text
        writting clean_text(with no flag)
        found_emojis(emoji_flag)
    '''
    found_emoji = [match.chars for match in emoji.analyze(text)]
    clean_link = emoji.replace_emoji(text, replace = '')
    clean_link = clean_link.split('#')[0]

    return clean_link, found_emoji


async def get_clean_link() -> None:
    '''
        decoding link(removing emoji-flag)
    '''

    server_links, name_flag = await get_links()

    for _, server in server_links.items():
        result = await emoji_founder(server["name"], server["link"], server["flag"])
        if result:
            print(result)
    # for link in decoded_link:
    #     clean, found = await put_dirty_link(link)
    #     print(clean)
    #     print(found)


async def get_dirty_json() -> str:#DONE
    '''
        getting dirty_json to make clean_json(for xray run -c)
    '''
    clean_link, flag = await get_clean_link()
    print(f"server picked: {flag}")
    dirty_json = os.system(f"cd ~/xra_y_theta/xra_y_link/Xray-Link-Json && ./Xray-Link-Json '{clean_link}'")

    return dirty_json


async def main(): #TODO
    await get_clean_link()

asyncio.run(main())

# need to fix: link_converter
#(xray_core is doesn't running with a dirty-link/links) | MOGGED
#dirty_link => bad_json => xray is cant run(he's crushing) | NOT MOGGED

#requirements.txt in the future btw i still using old venv with the cuda lol
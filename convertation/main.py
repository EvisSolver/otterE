import asyncio
import base64, requests
import emoji

from urllib.parse import unquote

     
LINK = '...'


async def get_links():
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

            result = [
                [server] for _ in range(count_servers)
            ]

            server_[f"Server: {count_servers}"] = f"{result[0]}"
    return server_

async def put_dirty_link(text):
    '''
        analyzing the text
        writting clean_text(with no flag)
        found_emojis(emoji_flag)
    '''
    found_emoji = [match.chars for match in emoji.analyze(text)]
    clean_link = emoji.replace_emoji(text, replace = '')
    clean_link = clean_link.split('#')[0]

    return clean_link, found_emoji

async def get_clean_link():
    '''
        decoding link(removing emoji-flag)
    '''

    server_links = await get_links()

    decoded_link = [unquote(dec_link.strip("['']")) for dec_link in server_links.values()]#декодирование ссылки на флаг внутри ссылки(например: %F0%9F%87%AA - 🇪🇪)

    for link in decoded_link:
        clean, found = await put_dirty_link(link)
        print(clean)
        print(found)

async def get_dirty_json(): #TODO
    server_ = await get_links()

    

async def main(): #TODO
    print(await get_links())
    await get_clean_link()

asyncio.run(main())

#need to fix: link_converter
#(xray_core is doesn't running with a dirty-link/links)
#dirty_link => bad_json => xray is cant run(he's crushing)

#requirements.txt in the future btw i still using old venv with cuda lol
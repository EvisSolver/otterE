import json, asyncio
from pystyle import Colors, Write
from main import get_dirty_json, get_links, get_clean_link


async def create_file() -> None:
    server_links, total_servers = await get_links()
    clean_link_list = await get_clean_link(server_links)
    servers_parameters = await get_dirty_json(clean_link_list, total_servers)

    for clean_link, server_parameter in zip(clean_link_list[:total_servers], servers_parameters[:total_servers]):

        try:
            data = json.loads(server_parameter)
        except json.JSONDecodeError:
            Write.Print(f"Error | Server:{clean_link['server_name']} gives bad json | skipping...")
            continue

        Write.Print(data, Colors.blue, interval = 0)
        filename = f"{clean_link["server_name"]}.json"

        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, ensure_ascii = False, indent = 2)
        print(clean_link["server_name"])


asyncio.run(create_file())
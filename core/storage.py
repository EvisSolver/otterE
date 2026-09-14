import asyncio, json
from settings import path_to_jsons

from xray import get_clean_json


async def create_file(clean_link_list: list, servers_parameters: dict, total_servers: int):
    for clean_link, server_parameter in zip(clean_link_list[:total_servers], servers_parameters[:total_servers]):
        try:
            data = json.loads(server_parameter)
        except json.JSONDecodeError: continue

        filename = f"{path_to_jsons}{clean_link['server_name']}.json"

        with open(
            filename, "w", encoding = "utf-8"
        ) as file:
            json.dump(data, file, ensure_ascii = False, indent = 2)

        await asyncio.sleep(0.1)
        await get_clean_json(f"{path_to_jsons}{clean_link["server_name"]}")

    return clean_link_list, total_servers
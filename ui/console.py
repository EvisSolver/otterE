import asyncio
from pystyle import Colors, Write


async def loading(clean_link_list: list) -> None:
    try:
        Write.Print("\nlink checking...\n", Colors.yellow, interval = 0)
        return clean_link_list
    except Exception as e:
        Write.Print(e, Colors.red, interval = 0)
        return None


async def start(clean_link_list: list, total_servers: int) -> str:
    picker = {}
    for server in clean_link_list[:total_servers]:
        picker[server["server_id"]] = server["server_name"]
    printer = Write.Print(
        f"""
    Link is succefuly loaded

    Total servers: {total_servers}
    ID|SERVER|: {picker}
        """, Colors.green, interval = 0
    )
    return printer

async def get_user_input(prompt: str, rand_sec: float) -> str:
    loop = asyncio.get_event_loop()
    Write.Print(prompt, Colors.purple, interval = rand_sec)
    return await loop.run_in_executor(None, input)
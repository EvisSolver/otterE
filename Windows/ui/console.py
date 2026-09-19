import asyncio
from pystyle import Colors, Write


async def loading(clean_link_list: list) -> None:
    '''
        checking. if all fine: it started(next func 'start' after 'loading')
        i think it makes none but trynna fix it when can
    '''

    try:
        Write.Print("\nlink checking...\n", Colors.yellow, interval = 0)
        return clean_link_list
    except Exception as e:
        Write.Print(e, Colors.red, interval = 0)
        return None


async def start(clean_link_list: list, total_servers: int) -> str:
    '''
        picker is just a dict which in: 'server_id' and 'server_name'
    '''
    
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
    '''
        creating a new async_def func to async-input to default input wouldn't get in way
        then returning the async-input
    '''

    loop = asyncio.get_event_loop()
    Write.Print(prompt, Colors.purple, interval = rand_sec)
    return await loop.run_in_executor(None, input)
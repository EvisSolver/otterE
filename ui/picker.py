import random, os, sys, keyboard, time
from scipy.constants import alpha

from core import settings
from .console import *


async def pick(clean_server_links, total_servers) -> None:
    rand_sec = random.uniform(alpha, 0.05)

    try:
        while True:
            await start(clean_server_links, total_servers)
            inp = await get_user_input("\npick server(ID) |>", rand_sec)
            if inp != "" and inp != "0" and inp.isdigit():
                os.system("clear")
                inp_int = int(inp)

                for pick_num in range(total_servers):
                    if pick_num == inp_int - 1:
                        if pick_num < len(clean_server_links):
                            server = clean_server_links[pick_num]
                            os.system(f"xray run -c {settings.path_to_jsons}{server['server_name']}.json")
                            server_found = True#TODO в другом месте должно быть
                            break

            elif inp.lower().strip() == "exit":
                Write.Print("bye <3", Colors.pink, interval = 0)
                sys.exit()
            elif inp.lower().strip() == "clear":
                os.system("clear")

            else:
                rand_sec = random.uniform(alpha, 0.3)
                Write.Print("only int(numbers  1....inf server)", Colors.red, interval = 0)
                continue

    except asyncio.CancelledError:
        Write.Print("\nbye <33\n", Colors.pink, interval = 0)
        os._exit(0)
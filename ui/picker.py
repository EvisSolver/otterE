import random, os, sys, keyboard, time
from scipy.constants import alpha

from core import settings
from .console import *


async def pick(clean_server_links, total_servers) -> None:
    '''
        - generating random_number
        - try:
            - while:
                -- writting the text
                -- start is starting with 2 parameters
                -- inp = async user-input

                -- if 'inp' not sumbol or 0 and digit then we clearing the console and creating inp_int(final input)
                -- creating number which we are picking in range total servers(n) + 1 bcs like in range 0:n - 1
                    -- if picking number == inp_int then we are checking list(len(clean_server_links))
                                                                                - for example:
                                                                                            -- clean_server_links = [[], [], [], []] => len = 4 =>  pick_num(like 5) - 1 = 4(ID: 4 server - n server)
                                                                                - then we making 'server' in which we writting the inputting-number
                                                                                                - for example: pick_num(still like 5) == inp_int(like 2) - 1 = inp_int(=1)
                                                                                                            -- clean_server_links has xray run -c jsons/{server_id(1)['server_name'].json}
                                                                                - after the xray run -c ... we ON server_found(if server_found = False ... in future btw i lost the idea from my head)
                - if server_found == True we async-waiting 0.01 sec(to no bugs like 'while' is not stopped and prog got bugged + to know when server is got down in latency in 0.01s) | continue
                - else we writting(str) Server with ID {n id} not found and continue to prog(program(script :#)) still works
            
                - next: just formatting-logic and variants of exits
        
    '''
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
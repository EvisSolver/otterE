import os, sys, json, asyncio, random

from pystyle import Colors, Write
from scipy.constants import alpha

from main import get_dirty_json, get_links, get_clean_link
from config import get_clean_json
from link import server_found


async def create_file(clean_link_list: list, servers_parameters: dict, total_servers: int) -> tuple[list[all[dict], int]]:
    '''
        - creating the cycle which combine list[0:n servers] and dict[0:n servers to] to create files
                                - for example: 
                                    -- my_dict = {'a': 1, 'b': 2}
                                    -- my_list = [10, 20]

                                    # updating values on having keys
                                    - for key, val in zip(my_dict.keys(), my_list):
                                        -- my_dict[key] = val

                                    -- print(my_dict)  # output: {'a': 10, 'b': 20}
        
        - then making 'with as file(like box in irl)': w: writting, encoding to reading with no errors and working is correctly on a lot operating-systems
        creating files in 0.1 sec to not overload the system(maybe in future it got update which can checking 1000 servers in 0.1 secs and pc can lagged if there is no latency(delay))
        retu

        - awaiting get_clean_json - joins in dir jsons/ and creating files which correspond to server_parameter['server_name'].json
        and returning list and int to use it in next-code
    '''
    for clean_link, server_parameter in zip(clean_link_list[:total_servers], servers_parameters[:total_servers]):

        try:
            data = json.loads(server_parameter)
        except json.JSONDecodeError:
            #Write.Print(f"Error | Server:{clean_link['server_name']} gives bad json | skipping...")
            continue

        #Write.Print(data, Colors.blue, interval = 0)
        filename = f"jsons/{clean_link["server_name"]}.json"

        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, ensure_ascii = False, indent = 2)
        #print(clean_link["server_name"])

        await asyncio.sleep(0.1)
        await get_clean_json(f"jsons/{clean_link["server_name"]}")
    #print(clean_jsons)
    return clean_link_list, total_servers


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
    for server in clean_link_list[0:total_servers]:
        picker[server["server_id"]] = server["server_name"]
    printer = Write.Print(f"""
    Link is succefully loaded
    
    Total servers: {total_servers}
    ID|SERVER|: {picker}
    """, Colors.green, interval = 0)
    return printer

async def get_user_input(prompt: str, rand_sec: float) -> str:
    '''
        creating a new async_def func to async-input to default input wouldn't get in way
        then returning the async-input
    '''
    loop = asyncio.get_event_loop()
    Write.Print(prompt, Colors.purple, interval = rand_sec)
    return await loop.run_in_executor(None, input)

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
    rand_sec = random.uniform(alpha, 0.3)
    try:
        while True:
            await start(clean_server_links, total_servers)
            inp = await get_user_input("\npick server(ID) |> ", rand_sec)
            if inp != "" and inp != "0" and inp.isdigit():
                os.system("clear")
                inp_int = int(inp)
                for pick_num in range(total_servers):
                    if pick_num == inp_int - 1:
                        if pick_num < len(clean_server_links):
                            server = clean_server_links[pick_num]
                            os.system(f"xray run -c jsons/{server['server_name']}.json")
                            server_found = True
                            break
                if server_found == True:
                    await asyncio.sleep(0.01)
                    continue
                else:
                    Write.Print(f"Server with ID {inp_int} not found\n", Colors.red, interval = rand_sec)
                    continue
            elif inp.lower().strip() == "exit" or inp == KeyboardInterrupt:
                Write.Print("bye <3", Colors.pink, interval = 0)
                sys.exit()
            else: 
                rand_sec = random.uniform(alpha, 0.3)
                Write.Print("only int(numbers 1....inf server)", Colors.red, interval = 0.05)
                os.system("clear")
                continue
    except asyncio.CancelledError:
        Write.Print("\nbye <33", Colors.pink, interval = 0)
        sys.exit()


async def main():
    '''start'''
    server_links, total_servers = await get_links()
    clean_link_list = await get_clean_link(server_links)
    servers_parameters = await get_dirty_json(clean_link_list, total_servers)

    await create_file(clean_link_list, servers_parameters, total_servers)
    await loading(clean_link_list)
    await start(clean_link_list, total_servers)
    await pick(clean_link_list, total_servers)


asyncio.run(main())
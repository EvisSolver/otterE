import asyncio, json
from .settings import path_to_jsons

from .xray import get_clean_json


async def create_file(clean_link_list: list, servers_parameters: dict, total_servers: int):
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
        except json.JSONDecodeError: continue

        clean_link['server_name'] = clean_link['server_name'].replace(" ", "_")
        filename = f"{path_to_jsons}{clean_link['server_name']}.json"
        with open(
            filename, "w", encoding = "utf-8"
        ) as file:
            json.dump(data, file, ensure_ascii = False, indent = 2)

        await asyncio.sleep(0.1)
        await get_clean_json(f"{path_to_jsons}{clean_link['server_name']}")

    return clean_link_list, total_servers
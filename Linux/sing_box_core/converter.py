import json

async def read_Json_Config() -> dict:
    '''Reading json in config.py and returning'''
    with open(f"sing_box_core/sing_box_config.json", "r", encoding = "utf-8") as file: config = json.load(file)
    return config
async def dirty_json_to_clean_json_sing_box(dirty_json) -> dict:
    '''Adding json_config to generated json'''
    s = {"type": "direct", "tag": "direct", "domain_resolver": "dns-local"}
    global_list = {"outbounds": []}
    global_list["outbounds"].append(dirty_json)
    global_list["outbounds"].append(s)

    json_config = await read_Json_Config()

    global_list.update(json_config)
    print(json.dumps(global_list, indent = 4))
    return global_list
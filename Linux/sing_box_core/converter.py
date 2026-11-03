import json
from get_sing_box_json import vless_link_to_sing_box_dirty_json

link = "vless://3171f8e0-8463-4d72-a277-004e66cbf0c8@lgdf.z9rkv4mqpx.com:443?encryption=none&flow=xtls-rprx-vision&type=tcp&security=reality&sni=lgdf.z9rkv4mqpx.com&fp=qq&pbk=Q6glPwZOhnjHTPtRJUTFgJOBQGgJGTprQfCf_NpOsTc"

def read_Json_Config() -> dict:
    with open("sing_box_config.json", "r", encoding = "utf-8") as file: config = json.load(file)
    return config
def dirty_json_to_clean_json_sing_box() -> dict:

    s = {"type": "direct", "tag": "direct", "domain_resolver": "dns-local"}
    dirty_json = vless_link_to_sing_box_dirty_json(link)
    global_list = {"outbounds": []}
    global_list["outbounds"].append(dirty_json)
    global_list["outbounds"].append(s)

    json_config = read_Json_Config()

    global_list.update(json_config)
    print(json.dumps(global_list, indent = 4))
dirty_json_to_clean_json_sing_box()
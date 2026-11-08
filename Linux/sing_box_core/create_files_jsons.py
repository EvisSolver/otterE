import json

async def create_jsons(file_name, clean_json_for_sign_box):
    '''Create json-files in dir sing_box_jsons/'''

    with open(f"sing_box_core/sing_box_jsons/{file_name}", "w", encoding = "utf-8") as file: json.dump(clean_json_for_sign_box, file, ensure_ascii = False, indent = 2)
    with open(f"sing_box_core/sing_box_jsons/{file_name}", "r", encoding = "utf-8") as file:
        json_in_file = file
    return json_in_file
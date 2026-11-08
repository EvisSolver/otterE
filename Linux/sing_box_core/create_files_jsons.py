import json

async def create_jsons(file_name, clean_json_for_sign_box, json_path):
    '''Create json-files in dir sing_box_jsons/'''

    with open(f"{json_path}{file_name}.json", "w", encoding = "utf-8") as file: json.dump(clean_json_for_sign_box, file, ensure_ascii = False, indent = 2)
    with open(f"{json_path}{file_name}.json", "r", encoding = "utf-8") as file:
        json_in_file = file
    return json_in_file
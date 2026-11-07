import json
from .converter import dirty_json_to_clean_json_sing_box

async def create_jsons(file_name, clean_json_for_sign_box):
    '''Create json-files in dir sing_box_jsons/'''

    with open(f"{file_name}.json", "w", encoding = "utf-8") as file: json.dump(clean_json_for_sign_box, file, ensure_ascii = False, indent = 2)
    with open(file_name, "r", encoding = "utf-8") as file:
        json_in_file = file
    return json_in_file
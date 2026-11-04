import json
from config import path_to_jsons
from converter import dirty_json_to_clean_json_sing_box

def create_jsons(file_name):
    '''Create json-files in dir sing_box_jsons/'''
    clean_json_for_sign_box = dirty_json_to_clean_json_sing_box()
    with open(file_name, "w", encoding = "utf-8") as file: json.dump(clean_json_for_sign_box, file, ensure_ascii = False, indent = 2)
    with open(file_name, "r", encoding = "utf-8") as file:
        json_in_file = file
    return json_in_file
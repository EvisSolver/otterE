import subprocess

from create_files_jsons import create_jsons
from config import path_to_jsons


# --- Checking the status of Json ---
def check_status_of_sing_box(json_file) -> bool:
    status_com = ["sudo", "sing-box", "check", "-c", json_file]
    try:
        subprocess.run(
            status_com, # -- Bash command, with checking the sing-box status
            capture_output = True,
            text = True,
            check = True
        )
        status_sing_box = True
    except: status_sing_box = False
    print(status_sing_box)
    return status_sing_box # -- Checking each json-file

# --- Starting the sing-box ---
file_name = f"{path_to_jsons}dskdfs.json" # -- Test file-name


check_status_of_sing_box(file_name)
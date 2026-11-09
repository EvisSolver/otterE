import subprocess, traceback, os

from .sing_box_no_sudo_installer import perms_ready
from .config import path_to_jsons


# --- Checking the status of Json ---
def check_status_of_sing_box(json_file) -> bool:
    perms_ready()
    status_com = ["sing-box", "check", "-c", json_file]
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
def start_sing_box(json_file):
    
    start_com = ["sing-box", "run", "-c", json_file]
    status = check_status_of_sing_box(json_file)
    print("Переданный путь:", repr(json_file))
    print("Абсолютный путь:", os.path.abspath(json_file))
    print("Файл существует?:", os.path.exists(json_file))

    if status:
        try:
            subprocess.run(
                start_com, # -- Starting sing-box with sudo(SuperUserDO)
                capture_output = True,
                text = True,
                check = True
            )
        except Exception as error:
            with open("errors.log", "w", encoding = "utf-8") as log_file:
                status_log = log_file.write(f"{'--' * 10}\nError\ntype:{type(error).__name__}\n{error}\n{'--' * 10}")
                traceback.print_exc(file = log_file)
            return None
    return True
file_name = f"{path_to_jsons}dskdfs.json" # -- Test file-name



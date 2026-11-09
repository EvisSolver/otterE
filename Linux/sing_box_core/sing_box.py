import subprocess, traceback, os

from .sing_box_no_sudo_installer import perms_ready
from .config import path_to_jsons

from pystyle import Colors, Write

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

    try:
        if status_sing_box:
            Write.Print(f"Server Status: {status_sing_box}\n", Colors.green, interval = 0)
        elif not status_sing_box:
            Write.Print(f"Server Status: {status_sing_box}\n", Colors.red, interval = 0)
    except Exception as error: Write.Print(error,"\n", Colors.red, interval = 0)

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
            global sing_box_process
            sing_box_process = subprocess.Popen(
                start_com, # -- Starting sing-box with sudo(SuperUserDO)
                text = True
            )
            print(f"PID | sing-box | {sing_box_process.pid}")
        except Exception as error:
            with open("errors.log", "w", encoding = "utf-8") as log_file:
                status_log = log_file.write(f"{'--' * 10}\nError\ntype:{type(error).__name__}\n{error}\n{'--' * 10}")
                traceback.print_exc(file = log_file)
            return None

# --- Killing process when button unreleased|OFF| ---
def kill_sing_box():
    subprocess.Popen(["pkill", "-f", "sing-box"])
    print("Kill signal sent to sing-box")

file_name = f"{path_to_jsons}dskdfs.json" # -- Test file-name

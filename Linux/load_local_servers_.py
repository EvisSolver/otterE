import os
from core.settings import *

from pystyle import Colors, Write


def load_local_servers():
    servers = []
    
    try:
        files = [f for f in os.listdir(path_to_jsons) if os.path.isfile(os.path.join(path_to_jsons, f)) and f.endswith(".json")]
        if len(files):
            Write.Print(f"{len(files)} local servers found", Colors.green, interval = 0)
            for file in files:
                print(file)
                # subprocess.Popen(f"xray run -c {file}", shell = True)
                servers.append(file)
        else: Write.Print("local servers not found", Colors.yellow, interval = 0)
    except Exception as error:
        Write.Print(error, Colors.red, interval = 0)

    return servers
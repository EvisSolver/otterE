import os, json
from core import settings

from pystyle import Colors, Write


def load_local_servers():
    servers = []

    try:
        files = os.listdir(settings.path_to_jsons)
    except FileNotFoundError: return [], 0

    for file_name in sorted(files):
        if not file_name.endswith(".json"): continue

        file_path = os.path.join(settings.path_to_jsons, file_name)

        try:
            with open(
                file_path, "r",
                encoding = "utf-8"
            ) as file: json.load(file)
        except Exception as error:
            Write.Print(f"file {file_name} breaked|ERROR:{error} |SKIPPING|", Colors.red, interval = 0)
            continue

        servers.append(
            {
                "server_flag": "",
                "server_name": file_name[:-5]
            }
        )
        return servers, len(servers)
import uuid
from pathlib import Path

from pystyle import Colors, Write

# Постоянный HWID устройства (генерируется один раз и сохраняется в файл)
HWID_FILE = Path(".device_hwid")

def get_hwid():
    try:
        hwid = HWID_FILE.read_text(encoding = "utf-8").strip()
    except FileNotFoundError: hwid = ""

    if not bool(hwid):
        hwid = str(uuid.uuid4())
        HWID_FILE.write_text(hwid, encoding = "utf-8")
    return hwid

# Заголовки с твоей «подписью» для запроса
# HEADERS = {
#     "User-Agent": "ArchEvis/1.0",
#     "x-hwid": DEVICE_HWID,
#     "x-device-os": "Linux",
#     "x-device-model": "PC"
# }
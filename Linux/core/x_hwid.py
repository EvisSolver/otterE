import uuid, getpass, platform
from pathlib import Path

from pystyle import Colors, Write

# Постоянный HWID устройства (генерируется один раз и сохраняется в файл)
HWID_FILE = Path(".device_hwid")

if HWID_FILE.exists():
    DEVICE_HWID = HWID_FILE.read_text(encoding = "utf-8").strip()
else:
    DEVICE_HWID = str(uuid.uuid4())
    Write.Print(DEVICE_HWID, Colors.purple, interval = 0)
    HWID_FILE.write_text(DEVICE_HWID, encoding = "utf-8")
DEVICE_HWID = HWID_FILE.read_text().strip()

# Заголовки с твоей «подписью» для запроса
HEADERS = {
    "User-Agent": "ArchEvis/1.0",
    "x-hwid": DEVICE_HWID,
    "x-device-os": "Linux",
    "x-device-model": "PC"
}

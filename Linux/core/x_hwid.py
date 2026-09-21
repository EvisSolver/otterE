import uuid
from pathlib import Path

# Постоянный HWID устройства (генерируется один раз и сохраняется в файл)
HWID_FILE = Path(".device_hwid")
if not HWID_FILE.exists():
    HWID_FILE.write_text(str(uuid.uuid4()))
DEVICE_HWID = HWID_FILE.read_text().strip()

# Заголовки с твоей «подписью» для запроса
HEADERS = {
    "User-Agent": "ArchEvis/1.0",
    "x-hwid": DEVICE_HWID,
    "x-device-os": "Linux",
    "x-device-model": "PC"
}

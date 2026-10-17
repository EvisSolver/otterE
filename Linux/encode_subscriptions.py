import base64
from core.settings import path_to_create_memory_file

with open(path_to_create_memory_file, "r", encoding = "utf-8") as file: text = file.read()

encoded_bytes = base64.b64encode(text.encode("utf-8"))
decoded_bytes = base64.b64decode(encoded_bytes.decode())
print(decoded_bytes)
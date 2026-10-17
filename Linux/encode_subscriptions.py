# How to make link-encode

import base64
from core.settings import path_to_create_memory_file, path_to_file_with_encoded_LINK


with open(path_to_create_memory_file, "r", encoding = "utf-8") as text:
    text = text.read()
    encoded_text = base64.b64encode(text.encode("utf-8"))
    text = encoded_text
print(text) # encoding encoded
encode_decoded_text = text.decode("utf-8")
print(encode_decoded_text) # decoding encoded
encode_decoded_decoded_text = base64.b64decode(encode_decoded_text)
print(encode_decoded_decoded_text) # encoding decoded
clean_decoded_link = encode_decoded_decoded_text.decode("utf-8")
print(clean_decoded_link) # decoding decoded

with open(path_to_file_with_encoded_LINK, "w") as encode_file:
    encode_file.write(encode_decoded_text)


#
#reading the user input(if he is give the sub)
#creating a new file
#writing text(user-input) in a new file
#encoding text in the main file
#every time decoding the file to link is works
#
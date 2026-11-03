import json
from urllib.parse import urlparse, parse_qs, unquote


link = "vless://3171f8e0-8463-4d72-a277-004e66cbf0c8@lgdf.z9rkv4mqpx.com:443?encryption=none&flow=xtls-rprx-vision&type=tcp&security=reality&sni=lgdf.z9rkv4mqpx.com&fp=qq&pbk=Q6glPwZOhnjHTPtRJUTFgJOBQGgJGTprQfCf_NpOsTc"

def vless_link_to_sing_box(vless_url: str) -> dict[str, any]:
    parsed = urlparse(vless_url)
    print(parsed)

    if parsed.scheme != "vless": raise ValueError(f"Link have unsupported scheme {parsed.scheme}, requires vless://")
    user_info = parsed.username or ""
    server_host = parsed.hostname or ""
    server_port = parsed.port or 443

    
    
vless_link_to_sing_box(link)
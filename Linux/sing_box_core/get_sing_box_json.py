from urllib.parse import urlparse, parse_qs, unquote


link = "vless://3171f8e0-8463-4d72-a277-004e66cbf0c8@lgdf.z9rkv4mqpx.com:443?encryption=none&flow=xtls-rprx-vision&type=tcp&security=reality&sni=lgdf.z9rkv4mqpx.com&fp=qq&pbk=Q6glPwZOhnjHTPtRJUTFgJOBQGgJGTprQfCf_NpOsTc"

async def vless_link_to_sing_box_dirty_json(vless_url: str) -> dict[str, any]:
    '''Put vless-link - gets generated outbounds for sign-box'''
    parsed = urlparse(vless_url)

    if parsed.scheme != "vless": raise ValueError(f"Link has unsupported scheme {parsed.scheme} | requires vless://")
    user_info = parsed.username or ""
    server_host = parsed.hostname or ""
    server_port = parsed.port or 443

    params = parse_qs(parsed.query, keep_blank_values = True)
    def get_param(name: str, default: str = "") -> str:
        '''Extracting values from str(link(query-string))'''
        val = params.get(name, [default])
        return val[0] if val else default

    connection_tag = unquote(parsed.fragment) if parsed.fragment else "vless-reality"

    security_type = get_param("security", "none")
    tls_enabled = security_type in ("tls", "reality")
    reality_enabled = security_type == "reality"

    singbox_outbound = {
        "type": "vless",
        "tag": connection_tag,
        "server": server_host,
        "server_port": server_port,
        "uuid": user_info,
        "flow": get_param("flow", ""),
        "domain_resolver": "dns-local",
        "tls": {
            "enabled": tls_enabled,
            "server_name": get_param("sni", server_host),
            "utls": {},
            "reality": {}
        }
    }

    fingerprint = get_param("fp", "")
    if fingerprint: singbox_outbound["tls"]["utls"] = {
        "enabled": True,
        "fingerprint": fingerprint
    }

    if reality_enabled:
        public_key = get_param("pbk", "")
        short_id = get_param("sid", "")
        singbox_outbound["tls"]["reality"] = {
            "enabled": True,
            "public_key": public_key,
            "short_id": short_id
        }
    singbox_outbound['tag'] = singbox_outbound['tag'].replace(" ", "_").replace("/", "_")

    return singbox_outbound

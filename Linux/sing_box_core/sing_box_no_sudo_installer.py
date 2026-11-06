import shutil, subprocess


def perms_ready() -> bool:
    """True, if sing-box already can up TUN without a root"""
    if not shutil.which("sing-box"): return False

    subprocess.run("sudo setcap 'cap_net_admin,cap_net_bind_service=+ep' /usr/bin/sing-box", shell = True, check = True)
    print("done")

perms_ready()
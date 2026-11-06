import os, shutil, subprocess


def perms_ready() -> bool:
    """True, if sing-box already can up TUN without a root"""
    if not shutil.which("sing-box"): return False

    r = subprocess.run(["getcap", "/usr/bin/sing-box", ])
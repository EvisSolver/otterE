import subprocess, shutil


def set_cap_if_needed(binary):
    path = shutil.which(binary)
    if not path: return

    res = subprocess.run(
        ["getcap", path], capture_output = True, text = True
    )
    caps = "cap_net_admin,cap_net_raw,cap_net_bind_service"
    if not all(c in res.stdout for c in caps.split(",")):
        subprocess.run(
            ["sudo", "setcap", f"{caps}=+ep", path],
            check = True
        )
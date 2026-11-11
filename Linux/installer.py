import subprocess, shutil

def installer():
    try:
        if not shutil.which("sing-box"):
            if shutil.which("yay"): subprocess.run("yay -Sy --noconfrim sing-box", shell = True, check = True)
            if shutil.which("paru"): subprocess.run("paru -Sy --noconfrim sing-box", shell = True, check = True)
            if shutil.which("pacman"): subprocess.run("pacman -Sy --noconfrim sing-box", shell = True, check = True)
        else: print("\nsing-box already installed")

        if not shutil.which("setcap"):
            subprocess.run("sudo pacman -Sy --noconfrim libcap", shell = True)
        else: print("setcap already installed")
        subprocess.run("sudo setcap 'cap_net_admin,cap_net_raw,cap_net_bind_service=+ep' $(which sing-box)", shell = True, check = True)
        subprocess.run("sudo setcap 'cap_net_admin,cap_net_raw,cap_net_bind_service=+ep' $(which xray)", shell = True, check = True)
        print("\ndone")
    except Exception as error: print(error)
import subprocess, shutil

def installer():
    try:
        if not shutil.which("sing-box"):
            if shutil.which("yay"): subprocess.run("yay -S --noconfirm sing-box", shell=True, check=True)
            elif shutil.which("paru"): subprocess.run("paru -S --noconfirm sing-box", shell=True, check=True)
            elif shutil.which("pacman"): subprocess.run("sudo pacman -S --noconfirm sing-box", shell=True, check=True)
        else: print("\nsing-box already installed")

        if not shutil.which("setcap"): subprocess.run("sudo pacman -S --noconfirm libcap", shell=True, check=True)
        else: print("setcap already installed")

        if shutil.which("sing-box"): subprocess.run("sudo setcap 'cap_net_admin,cap_net_raw,cap_net_bind_service=+ep' $(which sing-box)", shell=True, check=True)
        if shutil.which("xray"): subprocess.run("sudo setcap 'cap_net_admin,cap_net_raw,cap_net_bind_service=+ep' $(which xray)", shell=True, check=True)
            
        print("\ndone")
    except Exception as error: print(error)
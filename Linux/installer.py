import subprocess, shutil
from set_cap import set_cap_if_needed

def installer():
    try:
        if not shutil.which("sing-box"):
            if shutil.which("yay"): subprocess.run("yay -S --noconfirm sing-box", shell=True, check=True)
            elif shutil.which("paru"): subprocess.run("paru -S --noconfirm sing-box", shell=True, check=True)
            elif shutil.which("pacman"): subprocess.run("sudo pacman -S --noconfirm sing-box", shell=True, check=True)
        else: print("\nsing-box already installed")

        if not shutil.which("setcap"): subprocess.run("sudo pacman -S --noconfirm libcap", shell=True, check=True)
        else: print("setcap already installed")

        print(f"xray {bool(set_cap_if_needed('xray'))}")
        print(f"sing-box {bool(set_cap_if_needed('sing-box'))}")        

        print("\ndone")
        
    except Exception as error: print(error)
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
            
        print("\ndone")
    except Exception as error: print(error)
import shutil
import subprocess

def perms_ready() -> bool:
    '''Checking/Installing the Rules to open the gui in next times with not "sudo"'''
    singbox_path = shutil.which("sing-box") or "/usr/bin/sing-box"
    
    if not shutil.which("sing-box"):
        return False

    try:
        result = subprocess.run(["getcap", singbox_path], capture_output=True, text=True, check=True) # -- Checking current root

        if "cap_net_admin" in result.stdout and "cap_net_bind_service" in result.stdout: # -- If rules already exist's- nothing
            print("The rules already exists")
            return True
        print("Try again")
        subprocess.Popen(
            f"sudo setcap cap_net_admin,cap_net_bind_service=+ep {singbox_path}", # -- If doesn't exist's - installing the rules
            shell=True, 
            check=True
        )
        print("Rules is succefuly got added")
        return True
        
    except subprocess.CalledProcessError:
        print("Cant check sudo.")
        return False
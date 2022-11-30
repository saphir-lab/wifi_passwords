import re
import subprocess

def get_all_ssids():
    command = "netsh wlan show profile"
    ssids = subprocess.check_output(command, shell=True, text=True)
    ssids_list = re.findall(r"(?:Profile\s*:\s)(.*)", ssids)
    return ssids_list

def get_ssid_pwd(ssid):
    command = f'netsh wlan show profile "{ssid}" key=clear'
    ssid_details = subprocess.check_output(command, shell=True, text=True)
    pwd = re.search(r"(?:Key Content\s*:\s)(.*)", ssid_details)
    return pwd.group(1)

def print_all_ssids(ssids_dict, sort=True):
    if sort:
        for ssid, pwd in sorted(ssids_dict.items()):
            print("- " + ssid + " : " + pwd)
    else:
        for ssid, pwd in ssids_dict.items():
            print("- " + ssid + " : " + pwd)

if __name__ == "__main__":
    ssids_list=get_all_ssids()
    ssids_dict={}
    for ssid in ssids_list:
        ssids_dict[ssid]=get_ssid_pwd(ssid)
    print_all_ssids(ssids_dict)
from Admin import *
import subprocess
import sys
from icecream import *
from pprint import *
options={
    'network divsions':1,
    'IP address class':'D',
    'host req':2,



}

import psutil
interfaces = psutil.net_if_addrs()
for interface, addrs in interfaces.items():
    print(f"Interface: {interface}")

    for addr in addrs:
        if '1' in interface and 'Local' in interface:
            f3_octets=str(addr.address)
#            print(subprocess.run(["powershell", "-Command", '/l %i in (1,1,254) do @ping -n 1 -w 100'+f3_octets], capture_output=True))
        print(f"  Address: {addr.address}")
        print()
        print(f"  Netmask: {addr.netmask}")
from pprint import *
from datetime import datetime
import threading
import subprocess
netBios={}
def ping(ip,netBios):
    command = ["ping",  ip]  # Adjust options for your OS, -n for Windows, -c for Linux
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "Reply" in result.stdout:
        print(f"{ip} is up")
        res='up'
    elif "Reply" not in result.stdout:
        res='dn'
    netBios[ip]=res
    return netBios

def ping_sweep(ip_range):
    threads = []
    for i in range(1, 256):
        ip = f"{ip_range}.{i}"
        thread = threading.Thread(target=ping, args=(ip,netBios))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    with open('network_info','w') as networkMap:
        networkMap.write('netStats='+str(netBios)+'\ntimeStamp="'+str(datetime.now())+'"')
    return netBios

if __name__ == "__main__":
    base_ip = "10.123.1"  # Modify this to match your network
    netBios={'10.123.1.12': 'up', '10.123.1.8': 'up', '10.123.1.15': 'up', '10.123.1.31': 'up', '10.123.1.21': 'up', '10.123.1.17': 'up', '10.123.1.28': 'up', '10.123.1.1': 'up', '10.123.1.23': 'up', '10.123.1.26': 'up', '10.123.1.25': 'up', '10.123.1.4': 'up', '10.123.1.5': 'up', '10.123.1.7': 'up', '10.123.1.3': 'up', '10.123.1.39': 'up', '10.123.1.48': 'up', '10.123.1.2': 'up', '10.123.1.20': 'up', '10.123.1.14': 'up', '10.123.1.11': 'up', '10.123.1.10': 'up', '10.123.1.49': 'up', '10.123.1.47': 'up', '10.123.1.43': 'up', '10.123.1.51': 'up', '10.123.1.44': 'up', '10.123.1.6': 'up', '10.123.1.24': 'up', '10.123.1.27': 'up', '10.123.1.35': 'up', '10.123.1.19': 'up', '10.123.1.9': 'up', '10.123.1.33': 'up', '10.123.1.29': 'up', '10.123.1.22': 'up', '10.123.1.41': 'up', '10.123.1.32': 'up', '10.123.1.30': 'up', '10.123.1.46': 'up', '10.123.1.38': 'up', '10.123.1.18': 'up', '10.123.1.42': 'up', '10.123.1.45': 'up', '10.123.1.34': 'up', '10.123.1.16': 'up', '10.123.1.40': 'up', '10.123.1.50': 'up', '10.123.1.36': 'up', '10.123.1.37': 'up', '10.123.1.13': 'up', '10.123.1.136': 'up', '10.123.1.142': 'up', '10.123.1.144': 'up', '10.123.1.156': 'up', '10.123.1.176': 'up', '10.123.1.146': 'up', '10.123.1.145': 'up', '10.123.1.147': 'up', '10.123.1.198': 'up', '10.123.1.154': 'up', '10.123.1.151': 'up', '10.123.1.141': 'up', '10.123.1.161': 'up', '10.123.1.158': 'up', '10.123.1.149': 'up', '10.123.1.148': 'up', '10.123.1.166': 'up', '10.123.1.168': 'up', '10.123.1.143': 'up', '10.123.1.150': 'up', '10.123.1.171': 'up', '10.123.1.169': 'up', '10.123.1.157': 'up', '10.123.1.153': 'up', '10.123.1.172': 'up', '10.123.1.174': 'up', '10.123.1.155': 'up', '10.123.1.160': 'up', '10.123.1.175': 'up', '10.123.1.188': 'up', '10.123.1.183': 'up', '10.123.1.162': 'up', '10.123.1.163': 'up', '10.123.1.164': 'up', '10.123.1.180': 'up', '10.123.1.152': 'up', '10.123.1.165': 'up', '10.123.1.194': 'up', '10.123.1.206': 'up', '10.123.1.173': 'up', '10.123.1.181': 'up', '10.123.1.167': 'up', '10.123.1.170': 'up', '10.123.1.140': 'up', '10.123.1.159': 'up', '10.123.1.189': 'up', '10.123.1.187': 'up', '10.123.1.185': 'up', '10.123.1.184': 'up', '10.123.1.243': 'up', '10.123.1.182': 'up', '10.123.1.177': 'up', '10.123.1.178': 'up', '10.123.1.204': 'up', '10.123.1.207': 'up', '10.123.1.186': 'up', '10.123.1.203': 'up', '10.123.1.208': 'up', '10.123.1.179': 'up', '10.123.1.210': 'up', '10.123.1.216': 'up', '10.123.1.205': 'up', '10.123.1.193': 'up', '10.123.1.211': 'up', '10.123.1.195': 'up', '10.123.1.197': 'up', '10.123.1.192': 'up', '10.123.1.214': 'up', '10.123.1.220': 'up', '10.123.1.196': 'up', '10.123.1.199': 'up', '10.123.1.200': 'up', '10.123.1.224': 'up', '10.123.1.201': 'up', '10.123.1.191': 'up', '10.123.1.222': 'up', '10.123.1.213': 'up', '10.123.1.212': 'up', '10.123.1.190': 'up', '10.123.1.236': 'up', '10.123.1.230': 'up', '10.123.1.218': 'up', '10.123.1.228': 'up', '10.123.1.215': 'up', '10.123.1.225': 'up', '10.123.1.238': 'up', '10.123.1.237': 'up', '10.123.1.202': 'up', '10.123.1.234': 'up', '10.123.1.226': 'up', '10.123.1.229': 'up', '10.123.1.227': 'up', '10.123.1.219': 'up', '10.123.1.251': 'up', '10.123.1.223': 'up', '10.123.1.245': 'up', '10.123.1.250': 'up', '10.123.1.248': 'up', '10.123.1.217': 'up', '10.123.1.221': 'up', '10.123.1.233': 'up', '10.123.1.252': 'up', '10.123.1.231': 'up', '10.123.1.235': 'up', '10.123.1.255': 'up', '10.123.1.247': 'up', '10.123.1.239': 'up', '10.123.1.232': 'up', '10.123.1.209': 'up', '10.123.1.253': 'up', '10.123.1.242': 'up', '10.123.1.246': 'up', '10.123.1.254': 'up', '10.123.1.244': 'up', '10.123.1.241': 'up', '10.123.1.249': 'up', '10.123.1.240': 'up', '10.123.1.78': 'up', '10.123.1.66': 'up', '10.123.1.119': 'up', '10.123.1.58': 'up', '10.123.1.52': 'up', '10.123.1.76': 'up', '10.123.1.109': 'up', '10.123.1.57': 'up', '10.123.1.53': 'up', '10.123.1.59': 'up', '10.123.1.72': 'up', '10.123.1.55': 'up', '10.123.1.69': 'up', '10.123.1.79': 'up', '10.123.1.90': 'up', '10.123.1.106': 'up', '10.123.1.131': 'up', '10.123.1.87': 'up', '10.123.1.60': 'up', '10.123.1.73': 'up', '10.123.1.62': 'up', '10.123.1.71': 'up', '10.123.1.54': 'up', '10.123.1.68': 'up', '10.123.1.120': 'up', '10.123.1.70': 'up', '10.123.1.135': 'up', '10.123.1.56': 'up', '10.123.1.65': 'up', '10.123.1.67': 'up', '10.123.1.111': 'up', '10.123.1.74': 'up', '10.123.1.118': 'up', '10.123.1.114': 'up', '10.123.1.77': 'up', '10.123.1.99': 'up', '10.123.1.64': 'up', '10.123.1.75': 'up', '10.123.1.102': 'up', '10.123.1.105': 'up', '10.123.1.98': 'up', '10.123.1.63': 'up', '10.123.1.110': 'up', '10.123.1.82': 'up', '10.123.1.103': 'up', '10.123.1.85': 'up', '10.123.1.84': 'up', '10.123.1.86': 'up', '10.123.1.113': 'up', '10.123.1.112': 'up', '10.123.1.104': 'up', '10.123.1.61': 'up', '10.123.1.83': 'up', '10.123.1.91': 'up', '10.123.1.89': 'up', '10.123.1.81': 'up', '10.123.1.92': 'up', '10.123.1.101': 'up', '10.123.1.97': 'up', '10.123.1.96': 'up', '10.123.1.108': 'up', '10.123.1.100': 'up', '10.123.1.95': 'up', '10.123.1.88': 'up', '10.123.1.93': 'up', '10.123.1.94': 'up', '10.123.1.127': 'up', '10.123.1.116': 'up', '10.123.1.117': 'up', '10.123.1.124': 'up', '10.123.1.125': 'up', '10.123.1.115': 'up', '10.123.1.80': 'up', '10.123.1.121': 'up', '10.123.1.132': 'up', '10.123.1.126': 'up', '10.123.1.134': 'up', '10.123.1.107': 'up', '10.123.1.128': 'up', '10.123.1.133': 'up', '10.123.1.137': 'up', '10.123.1.123': 'up', '10.123.1.130': 'up', '10.123.1.129': 'up', '10.123.1.122': 'up', '10.123.1.138': 'up', '10.123.1.139': 'up'}
    netBios=ping_sweep(base_ip)
    #netBios=netBios.sort
    sorted_dict = {key: netBios[key] for key in sorted(netBios)}
    pprint(sorted_dict)
    print()
    ic(sorted_dict)



if __name__ == "__main__":
    base_ip = "192.168.1"  # Modify this to match your network
    #ping_sweep(base_ip)


#if __name__ == "__main__":
#    base_ip = "10.123.1"  # Modify this to match your network
    #ping_sweep(base_ip)








#'/l %i in (1,1,254) do @ping -n 1 -w 100'+f3_octets
if 0:
    for option in options:
        options[option]=input('new value for' +str(option)+':')
    print(options)
    f3_octets='0.0.0'
    
    with open('myfile','w') as writefile:
        test=subprocess.run(["powershell", "-Command", 'ipconfig > test.txt'], capture_output=True)
    with open('test.txt','r') as netBios:
        all=netBios.readlines()
        print(all[20:100])
        print(all)
        lines=1
    #for line in all:
    #    print(lines,line)
    #    lines+=1
    #test=subprocess.check_call(["ipconfig","/all"] )
    
def get_wifi():
    from pprint import pprint
    try:
        from wifi_id import *
        wifi_ids=Sys_wifi
    except ConnectionError:
        #print(errorcode)
        import os
        import socket 
        import subprocess
        import re
        from datetime import datetime
        command_output=subprocess.run(['netsh', 'wlan','show','profiles'],capture_output=True).stdout.decode()
        profile_names=re.findall("All User Profile     :(.*)\r",command_output)
        id_num=0
        wifi_ids={}
        if len(profile_names)!=0:
            wifi_ids[str(socket.gethostname())]={}
            for name in profile_names:
                wifi_profile=dict()
                profile_info=subprocess.run(['netsh','wlan','show','profile',name[1:]],capture_output=True).stdout.decode()
            #print(profile_info)
                if re.search('Security key           : Asbent',profile_info):
                    continue
                else:
                    profile_info_pass= subprocess.run(['netsh','wlan','show','profile',name[1:], 'key=clear'],capture_output=True).stdout.decode()
                    password  = re.search('Key Content            : (.*)\r',profile_info_pass)

                    if password==None:
                        pwrd=None
                    else:
                        pwrd=password[1]
                    wifi_ids[str(socket.gethostname())][str(id_num)]={
                        'ssid':name[1:],
                        'password':pwrd}
                    id_num+=1
        with open(os.getcwd()+'\wifi_id.py','w') as StoreWifi:
            StoreWifi.write('Sys_wifi='+str(wifi_ids)+'\n')
            StoreWifi.write('SaveTime="'+str(datetime.now())+'"')

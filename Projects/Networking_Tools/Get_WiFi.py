from pprint import pprint
try:
    from wifi_id import*
    wifi_ids=Sys_wifi
except :
    import os
    import socket
    import subprocess
    #allows access to system comands
    import re
    #re is short for regular expressions and allows for search for specific text in an output
    from pprint import pprint
    command_output=subprocess.run(['netsh','wlan','show','profiles'], capture_output=True).stdout.decode()
    #runs the command "netsh wlan showprofiles" in the command line and captures the output
    profile_names = re.findall("All User Profile     :(.*)\r",command_output)
    #grabs all profile names and stores them
    #run if list is not empty
    id_num=0
    wifi_ids={}
    if len(profile_names) !=0:
        wifi_ids[str(socket.gethostname())]={}
        for name in profile_names:
            #loop for every name in the profiles list and create a dictionary for that profile name
            wifi_profile =dict()
            #if security key is not absent then I may be able to grab the password
            profile_info = subprocess.run(['netsh','wlan','show','profile',name[1:]],capture_output=True).stdout.decode()####
    #delete        #print(profile_info)
            if re.search('Security key           : Absent',profile_info):
                continue
                # if no ket is found loop to the next interation
            else:
                #Assign the SSID of th eifi profile to the dictionary
                
    #delete            #wifi_profile['ssid'] = name[1:]
                #this condition means that a password is present
                profile_info_pass = subprocess.run(['netsh','wlan','show', 'profile',name[1:], 'key=clear'],capture_output=True).stdout.decode()
                #run the regualr expression command to capture the group after th " : " which is the password
                password = re.search('Key Content            : (.*)\r',profile_info_pass)
                #check if a password was found
                if password==None:
    #delete                #wifi_profile['password'] = None
                    pwrd=None
                else:
    #delete                #wifi_profile['password']= password[1]
                    pwrd=password[1]
                
                wifi_ids[str(socket.gethostname())][str(id_num)]={'ssid':name[1:],'password':password[1]}
                id_num+=1
    ######################################
    # show all
    #delete pprint(wifi_list)
    #####################################
    import os
    from datetime import datetime
    with open(os.getcwd()+'\wifi_id.py','w') as StoreWifi:
        StoreWifi.write('Sys_wifi='+str(wifi_ids)+'\n')
        StoreWifi.write('SaveTime="'+str(datetime.now())+'"')

pprint(wifi_ids)
#print(SaveTime)


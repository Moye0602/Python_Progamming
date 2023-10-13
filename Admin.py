'''This file will serve as persoanlly built module of functions'''
import time,datetime
import termcolor
from pprint import pprint
# import more as you add to this file
'''the first couple will be for degugging and message output from our first session'''

def blank():
    print(' '*40,end='\r')
########################################

########################################
def crayon(statement='>>here i am<<',color='yellow'):
    from termcolor import colored
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed."""
    if type(statement)==list:
        state=''
        for word in statement:
            state+=str(word)+' '
        statement=[word for word in statement]
        statement=state
    elif statement!=list and type(statement)!=str:
        statement=str(statement)
    try:
        print(colored(statement,color))
    except Exception:
        print(statement)
########################################

########################################
def timeout(Tminus):
    def convert(ttime):
        day = ttime // (60*60*24)
        ttime = ttime % (24 * 3600)
        hour = ttime // 3600
        ttime %= 3600
        minutes = ttime // 60
        ttime %=60
        seconds = ttime
        return "%d:%d:%d:%d" % (day,hour, minutes, seconds)
    while 0<Tminus:
        crayon(['Timeout',convert(round(Tminus,2)) ,'seconds remaining                                  '])
        print(end="\033[F"*(1))
        TminusStart=Tminus
        Tminus-=1
        time.sleep(round(TminusStart-Tminus,2))
    blank()
########################################

########################################
def restart_file(auto=False):
    '''place at the end of a program either at the end of a loop or in an exception.
    when called, press "y" to restart or 'n' to exit the program'''
    import gc,sys,subprocess
    import keyboard
    subprocess.call(["cmd", "/c", "cls"])
    print('restart file? y/n ')
    while 1:
        try:
            if auto==True or auto==False and keyboard.is_pressed('y'):
                gc.collect()
                subprocess.call([sys.executable] + sys.argv)
                sys.exit() 
            elif keyboard.is_pressed('n'):
                crayon('User Stopped Program')
                break
        except KeyboardInterrupt:
            crayon('Keyboard Interupt')
            break
########################################

########################################
def file_backup(fileName,recover=False):
    import shutil
    path=__file__.split('/')
    path=('/').join(path[:-1])
    if recover==False :
     #"path/to/source/"+str(fileName)+'.py'

        source_path =path+str(fileName)+'.py'
        destination_path = path+str(fileName)+'_dup.py'
        shutil.copy(source_path, destination_path)
        print('backup of ',fileName, 'complete')
    if recover:
        source_path =path+str(fileName)+'_dup.py'
        destination_path = path+str(fileName)+'.py'
        shutil.copy(source_path, destination_path)
        print('recovery of ',fileName, 'complete')

########################################

########################################

def get_wifi():
    """when this is ran on a machine, it will create a dictionary of all SSIDs and corresponding
    password, at the completion, a file will be created with a time stamp"""
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
            profile_info=subprocess.run(['netsh','wlan','show','profile',name[1:]],capture_output=True).stdout.decode()
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
    print(wifi_ids)
    with open(os.getcwd()+'\wifi_id.py','w') as StoreWifi:
        StoreWifi.write('Sys_wifi='+str(wifi_ids)+'\n')
        StoreWifi.write('SaveTime="'+str(datetime.now())+'"')

    #####################################
    import os
    from datetime import datetime
    with open(os.getcwd()+'\wifi_id.py','w') as StoreWifi:
        StoreWifi.write('Sys_wifi='+str(wifi_ids)+'\n')
        StoreWifi.write('SaveTime="'+str(datetime.now())+'"')

########################################

########################################    
def internal_copy(name):
    """ When writing to a file place this after all other writes have occured with the filename
    This will make an entry at the end which cause the inital file created to create a copy of itself
    in its current state when imported. This effectively makes the origin file create back ups of itself"""
    path=__file__.split('\\')
    path=('\\').join(path[:-1])+'\\'
    with open(path+name+'.py','a') as addto:
        addto.write('import shutil'+'\n'
        "path=__file__.split('/')"+'\n'
        "path=('/').join(path[:-1])"+'\n'
        "source_path =path+'"+name+"'+'.py'"+'\n'
        "destination_path = path+'"+name+"'+'_dup.py'"+'\n'
        "shutil.copy(source_path, destination_path)"+'\n'
        "print('backup of ','"+name+"', 'complete')"+'\n')
########################################
#$$$
########################################

if __name__=='__main__':
    print('I am main')
    
########################################

########################################


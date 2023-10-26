'''this file will be a bit differnt to the Admin file in that you import the admin file as a module
and run the various functions here'''

from termcolor import colored
import time,sys,subprocess
from importlib import reload
from pprint import pprint
    # See Admin is already able to be imported

while True:
    try:
        import Admin
        reload(Admin)
        from Admin import *
    except Exception as errorcode:
        print(errorcode)
        
        crayon('Admin file error','red','on_grey',['bold'])

    try:
        crayon('my list of functions will go here functions will go here','green')
        options=['Timer','Get Wifi','Ping Sweep'] 
        for option in range(0,len(options)):
            print('>'+str(option+1)+': '+options[option])
        option=int(input('what function do you want?: '))
        
        #this will be a set of if/e;if states that when true, execute the function associated
        if option==1:
            timer=int(input('What is the Wait time?: '))
            timeout(timer)
        elif option==2:
            get_wifi()
        elif option==3:
            rootIP=input('what is the IP scheme?: ')
            ping_sweep(rootIP)
    except KeyboardInterrupt as exceptioncode:
        
        crayon('\n','User Interuption')
        crayon(exceptioncode)
        restart_file()
    except Exception as exceptioncode:
        
        crayon(exceptioncode)
        print()
        continue
    blank()
    crayon('/'*40,'cyan')
        
from termcolor import colored
import time,sys,subprocess
from importlib import reload
from pprint import pprint
import time 

while True:
    try:
        import  Admin
        reload (Admin)
        from Admin import *
    except ImportError as errocode:
        print(errocode)
        print(colored('error occured','red'))
    try:
        print(colored('my functions will go here','green'))
        options=['Timer', 'Get Wifi',]
        for option in range (0,len(options)):
            print('>'+ str(option+1)+': '+options[option])
        option=int(input('what function do you want?:' ))
        if option ==1:
            timer=int(input('what is the wait time?'))
            while timer>0:
                print(timer)
                timer-=1
                time.sleep(1)
        elif option ==2:
            get_wifi_Legacy()
    except KeyboardInterrupt as global_error:
        print('user interupted')
        print(global_error)
    except Exception as global_error:
        print(colored('global error occured','red'))

        continue
print('end loop')
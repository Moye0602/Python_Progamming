'''This file will serve as persoanlly built module of functoins'''
'''first import other in-built python module that you may want to use'''
import time,datetime
import termcolor
from pprint import pprint
# import more as you add to this file
'''the first couple will be for degugging and message output from our first session'''


'''next, for debugging purpose while creating and testing functions in admin we make a condition to only run a 
function here if this is the file that is executing the function'''
#print()
#print(__name__,'if we creat a condition that checks if this is true, we can use it as a verifier')
def blank():
    print(' '*25,end='\r')

def crayon(statement,color='yellow',background=None,fancy_stuff=None):
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
        bold, dark, underline, blink, reverse, concealed.
        Example:
        colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])"""
    try:
        if isinstance(statement, type):
            print('here')
            print(type(statement))
            print(statement)
            print('there')
        if type(statement) !=  str:
            statement=[str(word) for word in statement]
            statement = ' '.join(statement)
        
        print(termcolor.colored(statement,color,fancy_stuff,background))
    except Exception:
        print(statement)
########################################

########################################
def timeout(Tminus):
    def convert(time):
        day = time // (60*60*24)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %=60
        seconds = time
        return "%d:%d:%d:%d" % (day,hour, minutes, seconds)
    while 0<Tminus:
        print('Timeout',convert(round(Tminus,2)) ,'seconds remaining                                  ',end='\r')
        TminusStart=Tminus
        Tminus-=1
        time.sleep(round(TminusStart-Tminus,2))
    print(' '*50,end='\r')
########################################

########################################
def restart_file():
    import gc,sys,subprocess
    import keyboard
    blank()
    print('restart file?')
    try:
        if keyboard.wait('y')==None:
            subprocess.call([sys.executable] + sys.argv)
            sys.exit() 
    except KeyboardInterrupt:
        crayon('User Stopped Program')
########################################

########################################
def file_backup(fileName,backup=True,recover=False):
    import shutil
    path=__file__.split('/')
    path=('/').join(path[:-1])
    if recover==False :
     #"path/to/source/"+str(fileName)+'.py'

        source_path =path+str(fileName)+'.py'
        destination_path = path+str(fileName)+'_dup.py'
        shutil.copy(source_path, destination_path)
        #print('backup of ',fileName, 'complete')
    if recover:
        source_path =path+str(fileName)+'_dup.py'
        destination_path = path+str(fileName)+'.py'
        shutil.copy(source_path, destination_path)
        #print('recovery of ',fileName, 'complete')
########################################
#$$$
########################################
if 0 and __name__=='__main__':
    print('I am main and I will do the function')
    crayon('words') #this will work
    statement='words',32
    #statement=list(statement)
    #statement = ' '.join(statement)
    crayon(statement,'blue',['blink'],'on_black')
    restart_file()
        # crayon works
        # with having default values, this shortcuts the list of arguements we need to put but instead allows
        #us to modify the behaviour when needed
    
    #normally I would place a try except here but when things break here we need
    #to know so we can fix the issues as they show up
########################################

########################################


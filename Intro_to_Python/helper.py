import importlib,time
from termcolor import colored
def crayon(statement,color='yellow'):
    '''Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.'''
    try:
        print(colored(str(statement)),color)
    except TypeError:
        print(statement)

def install_if_missing(package_name):
    """This functions takes in a list of module names and confirms thay they exist on the current system
    if the module is missing, the function will automatically download the module."""
    try:
        importlib.import_module(package_name)
    except ImportError:
        print('><'*50,'\n')
        print(f"{package_name} is not installed. Lets change that...\n")
        print('><'*50,'\n')
        try:
            import subprocess
            subprocess.check_call(["pip", "install", package_name])
            print(f"{package_name} has been successfully installed.")
        except Exception as e:
            print(f"Error installing {package_name}: {e}")


def timeout(Tminus=10):
    '''When called, will start a coundown based on the Tminus value.
       Default value is 10'''
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
# Example usage:
 
# Replace with the name of the module you want to install


if __name__=='__main__':
    package_names =[ "requests",'importlib','requests','icecream',
                'pyttsx3','termcolor','keyboard',
                'beautifulsoup4','pandas','pytz','schedule','Faker','tello-python'] 
    for module in package_names:
        print(module)
        install_if_missing(module)

#import tello-python as tp
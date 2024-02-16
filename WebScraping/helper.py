import importlib,time
from termcolor import colored
def install_if_missing(package_name):
    """This functions takes in a list of module names and confirms thay they exist on the current system
    if the module is missing, the function will automatically download the module."""
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"{package_name} is not installed. Installing...")
        try:
            import subprocess
            subprocess.check_call(["pip", "install", package_name])
            print(f"{package_name} has been successfully installed.")
        except Exception as e:
            print(f"Error installing {package_name}: {e}")


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
        try:
            print('Timeout',convert(round(Tminus,2)) ,'seconds remaining                                  ',end='\r')
            TminusStart=Tminus
            Tminus-=1
            time.sleep(round(TminusStart-Tminus,2))
        except KeyboardInterrupt:
            print('User stopped process')
            break
        print(' '*50,end='\r')
# Example usage:

# Replace with the name of the module you want to install
def crayon(statement,color='yellow'):
    '''Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.'''
    try:
        print(colored(str(statement)),color)
    except TypeError:
        print(statement)

if __name__=='__main__':
    package_names =[ "requests",'importlib','requests','icecream',
                'pyttsx3','random','termcolor','keyboard',
                'beautifulsoup4','pandas','pytz','schedule','Faker','tello-python'] 
    for module in package_names:
        print(module)
        install_if_missing(module)

#import tello-python as tp
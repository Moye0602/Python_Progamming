import importlib,time

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
        print('Timeout',convert(round(Tminus,2)) ,'seconds remaining                                  ',end='\r')
        TminusStart=Tminus
        Tminus-=1
        time.sleep(round(TminusStart-Tminus,2))
    print(' '*50,end='\r')
# Example usage:
 
# Replace with the name of the module you want to install


####
def file_backup(fileName,backup=True,recover=False):
    import shutil
    path=__file__.split('/')
    path=('/').join(path[:-1])
    if recover==False:
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


####


if 0 and __name__=='__main__':
    package_names =[ "requests",'importlib','requests','icecream',
                'pyttsx3','random','termcolor','keyboard',
                'beautifulsoup4','pandas','pytz','schedule','Faker',
                'tda-api','selenium']

                #' tello-python'] 
    for module in package_names:
        print(module)
        install_if_missing(module)

#import tello-python as tp
import subprocess
imports=[ 'importlib','icecream','pandas','Faker','numpy',]
#for name in imports :
#    try:
#        subprocess.check_call(["pip", "install", name])        
#    except:
#        print(name,'failed')



from faker import Faker
fake=Faker()

people=500
book3={}
from datetime import datetime
for num in range(people):
    book3[num]={'First Name':str(fake.name()).split(' ')[0] ,


        'Last Name':str(fake.name()).split(' ')[1],
        'Address':fake.address(),
        'Email':fake.free_email(),
        'Phone Number':fake.basic_phone_number(),
        'DoB':str(datetime.fromisoformat(str(fake.date_of_birth())))[:10]}


#print(book3)
    

    
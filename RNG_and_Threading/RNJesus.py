from Admin import*
import random
from datetime import datetime
path=__file__.split('\\')
path=('\\').join(path[:-1])+'\\'


while 1: 
    try:
        myNumber=random.randint(0,100000)
        print(myNumber)
        with open(path+'hidden_number.py','w') as storeNumber:
            storeNumber.write('hiddenVal='+str(myNumber)+'\n'+'timeStamp="'+str(datetime.now())+'"')
            crayon('New Value Stored')
        #timeout(30)
        timeout(random.randint(2,20))
    except KeyboardInterrupt:
        restart_file()
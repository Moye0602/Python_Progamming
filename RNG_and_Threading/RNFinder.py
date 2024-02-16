from Admin import *
from importlib import reload
import threading
from icecream import*
from datetime import datetime
max_threads=4
max_range=100000
timeout(3)
def guessingMachine(start=0,end=100,multi='solo',thread_count=1):
    if thread_count>1:
        print('threads per lane',max_range/max_threads)
    from hidden_number import hiddenVal
    
    for i in range(start,end):
        if datetime.now().second%2==0:
            import hidden_number
            reload(hidden_number)
            from hidden_number import hiddenVal,timeStamp
            startTime=datetime.fromisoformat(timeStamp)
        print(i,'     ',end='\r')
        if i==hiddenVal:
            crayon(['found it:',i,'time elapsed:',datetime.now()-startTime])
            with open('foundit.py','a') as found:
                if 0:
                    import foundit 
                    reload(foundit)
                    from foundit import found
                  #  if found['Multi/Solo']=='multi':
                 #       found[]
                   # elif found['Multi/Solo']=='solo':
                #scoreBoard={'Time':'Multi/Solo':multi,'Threads':thread_count}}
                foundIt={str(datetime.now()-startTime):{'Value':i,'Multi/Solo':multi,'Threads':thread_count}}
                
                
                found.write('\n'+'found='+str(foundIt)+'\n')

    
#for i in range(max_threads):
#    print(i*(max_range/max_threads),(i+1)*(max_range/max_threads),i*(max_range/max_threads)-(i+1)*(max_range/max_threads))
guesses={i for i in range (0,max_range)}
try:
    while 1:
        if 0:#multilane
            multi='multi'
            threads=[]
            for whoami in range(0, max_threads):
                print(whoami*10000,(whoami+1)*0000)
                section=int(max_range/max_threads)
                thread = threading.Thread(target=guessingMachine, args=(whoami*section,(whoami+1)*section,multi,max_threads))
                threads.append(thread)
                thread.start()#

            for thread in threads:
                thread.join()
        else:
            print(0,max_range)
            guessingMachine(0,max_range)
            #ic()
        #timeout(20)
except KeyboardInterrupt:
    pass
restart_file()

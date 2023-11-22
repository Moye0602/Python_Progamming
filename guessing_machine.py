from Admin import *
from importlib import reload
import threading
from icecream import *
from datetime import datetime
max_threads=8
max_range=100000

print(3**13)#%29)
timeout(90000)
try:
    def guessingMachine(start=0,end=100,multi='solo',thread_count=1):
        if thread_count>1:
            print('threads per lane:', max_range/max_threads)
        from hidden_number import hiddenVal
        
        for number in range(start,end):
            if datetime.now().second%2==0:
                import hidden_number
                reload(hidden_number)
                from hidden_number import hiddenVal,timeStamp
                startTime=datetime.fromisoformat(timeStamp)
            print(number,'         ',end='\r')
            if number==hiddenVal:
                crayon(['found it:',number,'time elapsed:',datetime.now()-startTime])
                with open('foundIT.py','a') as found:
                    foundIT={str(datetime.now()-startTime):{'Value':number,'Multi/Solo':multi,'Threads':thread_count}}
                    found.write('\nfound='+str(foundIT)+'\n')

    guesses={i for i in range (0,max_range)}
    try:
        while 1:
            if 1: #multilane
                multi='multi'
                threads=[]
                for whoami in range (0,max_threads):
                    print(whoami*10000, (whoami+1)*10000)
                    section=int(max_range/max_threads)
                    thread= threading.Thread(target=guessingMachine, args=(whoami*section,(whoami+1)*section,max_threads))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            else:
                guessingMachine(0,max_range)
    except KeyboardInterrupt:
        print('end')
    guessingMachine(start=0,end=100,multi='solo',thread_count=1)

except KeyboardInterrupt:
    restart_file()
except Exception as err:
    print(err)
    restart_file()
restart_file()
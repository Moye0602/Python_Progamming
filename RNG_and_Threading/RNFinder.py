from Admin import *
from importlib import reload
import threading
from icecream import*
from datetime import datetime
max_threads=6
max_range=100000
import csv
path=__file__.split('\\')
path=('\\').join(path[:-1])+'\\'
fieldnames=['x','time','hidden val']
with open(path+'RNFinder.csv', 'w') as RN_csv_writer:
    csv_writer = csv.DictWriter(RN_csv_writer, fieldnames = fieldnames )
    csv_writer.writeheader()
graph={}
timeout(0)
def guessingMachine(start=0,end=100,multi='solo',thread_count=1,x=0):
    if thread_count>1:
        print('threads per lane',max_range/max_threads)
    from hidden_number import hiddenVal,timeStamp
    startTime=datetime.fromisoformat(timeStamp)
    for i in range(start,end):
        if datetime.now().second%2==0:
            import hidden_number
            reload(hidden_number)
            from hidden_number import hiddenVal,timeStamp
            startTime=datetime.fromisoformat(timeStamp)
        #print(i,'     ',end='\r')
        print(end='\r')
        if i==hiddenVal:
            blank()
            crayon(['found it:',i,'time elapsed:',datetime.now()-startTime])
            print()
            
            RN_csv_reader= open(path+'RNFinder.csv','r')
            print(f"last line {x} {len(RN_csv_reader.readlines())}")
            x=int((len(RN_csv_reader.readlines()))/2)
            if x<2 or RN_csv_reader.readlines()[-2].split(',')[2].isdigit() and RN_csv_reader.readlines()[-2].split(',')[2]!=hiddenVal:
                print(f"last line {x} {len(RN_csv_reader.readlines())}")#{RN_csv_reader.readlines()[-2].split(',')[2]} != {hiddenVal}")
                
                #len(RN_csv_reader.readlines())>2 and
                with open(path+'foundit.py','a') as found:
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
                
                
                RN_csv_reader.close
                #print('>>>>',datetime.now().second,startTime.microsecond+startTime.second,'\n'*3)
                findTime= (datetime.now().second-startTime.second+(datetime.now().microsecond-startTime.microsecond)/1000000) if (datetime.now().second-startTime.second+(datetime.now().microsecond-startTime.microsecond)/1000000)>0 else 0           
                with open(path+'RNFinder.csv','a') as RN_csv_writer:
                    graph['x']=x
                    graph['time']=findTime
                    graph['hidden val']=hiddenVal
                    csv_writer = csv.DictWriter(RN_csv_writer, fieldnames = fieldnames )
                    csv_writer.writerow(graph)
                    RN_csv_writer.close()

        
#for i in range(max_threads):
#    print(i*(max_range/max_threads),(i+1)*(max_range/max_threads),i*(max_range/max_threads)-(i+1)*(max_range/max_threads))
guesses={i for i in range (0,max_range)}
try:
    x=0
    while 1:
        if 1:#multilane
            multi='multi'
            threads=[]
            for whoami in range(0, max_threads):
                print(whoami*10000,(whoami+1)*0000)
                section=int(max_range/max_threads)
                thread = threading.Thread(target=guessingMachine, args=(whoami*section,(whoami+1)*section,multi,max_threads,x))
                threads.append(thread)
                thread.start()#

            for thread in threads:
                thread.join()
        else:
            print(0,max_range)
            guessingMachine(0,max_range,x=x)
            #ic()
        #timeout(20)
except KeyboardInterrupt:
    pass
restart_file()

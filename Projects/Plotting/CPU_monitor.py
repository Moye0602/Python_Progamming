import time, psutil,csv
#while 1:
#    print(psutil.cpu_percent(),psutil.virtual_memory())
#    time.sleep(.25)
with open('memwriter.csv','w') as mem_writer:
    stuff=['xval','cpu','mem']
    mem_writer=csv.DictWriter(mem_writer,fieldnames=stuff)
    mem_writer.writeheader()

def usage(cpu_useage,mem_usage,xval=0,bars=25):
    
    
    cpu_perc=cpu_useage/100
    cpu_bar='█'*int(cpu_perc*bars)+'-'*(bars-int(cpu_perc*bars))
    
    mem_perc=mem_usage/100
    mem_bar='█'*int(mem_perc*bars)+'-'*(bars-int(mem_perc*bars))
    #print('CPUsage: |',cpu_bar,str(round(cpu_useage,2))+'%',end='\r')
    print(f'\rCPU Ussage: |{cpu_bar}| {cpu_useage:.2f}%', end="")
    print(f'MEM Ussage: |{mem_bar}| {mem_usage:.2f}%', end='\r')
    with open('memwriter.csv','a') as mem_writer:
        mem_writer = csv.DictWriter(mem_writer, fieldnames= stuff)
        info={
            'xval':xval,
            'cpu':cpu_useage,
            'mem':mem_usage
        }
        #mem_writer.csv.writerow(info)
        mem_writer.writerow(info)
try:
    xval=0
    while 1:
        usage(psutil.cpu_percent(),psutil.virtual_memory().percent,xval,bars=25)
        xval+=1
        time.sleep(.25)
except KeyboardInterrupt:
    pass
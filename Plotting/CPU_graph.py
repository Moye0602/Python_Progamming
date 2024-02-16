import time, psutil,csv
track=0

#while 1:
#    print(psutil.cpu_percent(),psutil.virtual_memory())
#    time.sleep(.25)
if track:
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
xval=0
while track:

    usage(psutil.cpu_percent(),psutil.virtual_memory().percent,xval,bars=25)
    xval+=1
    time.sleep(.5)
#((((((((((((((((((((((((((((()))))))))))))))))))))))))))))

import pandas as pd
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
from Admin import *
import sys,subprocess,csv
from datetime import datetime, timedelta,date,time
import random
#dates.insert(0,'% Global gain')
filename='memwriter'
try:
    data = pd.read_csv(filename+'.csv')

    details= [day for day in data.columns].sort()
    #details.pop(-1)
except Exception as error:
    crayon(error)
    crayon('somethin is missing','red')
#################################



# Read the CSV file

with open(filename+'.csv', 'r') as my_file:
    reader = csv.reader(my_file)
    header = next(reader)  # Read the header row

# Create variables based on the headers  dynamically
# as the list grows
variables_ini,col_count = {},0
for i, column_name in enumerate(header):
    variable_name = f"y1_{i+1}"
    variables_ini[variable_name] = column_name
    col_count+=1



#################################
# Accessing the variables
styles=plt.style.available
style=styles[random.randrange(0,len(styles)-1)]
if 1:
    try:

        
        #File_Location='C:/Users/00775/OneDrive/Documents/Trade_Bot/Gen_12_1/DashBoard_CSV/'
        
        #filename+=str(datetime.date(datetime.today()))+'_'+str(lane)
        #if afterHoursLoop==1:
        #    filename+='_AH'
        #filename='Dashboard_History_2023-05-21_0'
        print('Style:',style)
        print('Now showing live graph for: '+ filename)

        #plt.style.use('seaborn')


        
        plt.style.use(style)
        
        plt.gcf()
        plt.gca()
        
        fig1=plt.figure(1)
        plt.close(fig1)
        #fig2, (ax1, ax2, ax3) = plt.subplots(nrows=3,ncols=1)
        #fig2, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4,ncols=1)
        fig2, (ax1, ax2) = plt.subplots(nrows=2,ncols=1)
        x_vals = []
        y_vals = []
        index = count()
        
        def update(i):
            ##ax1.cla()
            #ax2.cla()
            data = pd.read_csv(filename+'.csv')
            #if len(data.columns)!=

            x = data['xval']
            info,run_count,variables={},0,{}
            for i, column_name in enumerate(header):
                variable_name = f"y1_{i+1}"
                variables[variable_name] = column_name
                run_count+=1
            if run_count!=col_count:
                subprocess.call([sys.executable] + sys.argv)
                sys.exit()
            #expand the list of variables with the information given from file (automatically)
            for vari in variables_ini:
                if variables_ini[vari]!='x_value':
                    info[vari]=data[variables_ini[vari]]
                    if 'cpu' in variables_ini[vari]:
                        ax1.plot(x, data[variables_ini[vari]], label=variables_ini[vari])

                    elif 'mem' in variables_ini[vari]:
                        ax2.plot(x, data[variables_ini[vari]], label=variables_ini[vari])
                    print(data,variables_ini,vari)
                #old static method of updating variables
#                y1_11= data[dates[10]]
#                ax2.plot(x, y1_11, label=dates[10])
            ax1.set_xlim(left=max(x-480),right=max(x+15))
            #ax1.legend(loc='upper left')
            ax1.plot(x_vals,y_vals)

            ax2.set_xlim(left=max(x-480),right=max(x+15))
            #ax2.legend(loc='upper left')
            ax2.plot(x_vals,y_vals)

        plt.tight_layout()

        ani_RSI = FuncAnimation(plt.gcf(), update, interval = 1000)

        plt.show()

        count = 0
    
    except ConnectionError:#Exception:
        print('restarting graph')#,end=\\r')
        subprocess.call([sys.executable] + sys.argv)
        sys.exit()    

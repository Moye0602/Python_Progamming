import random
import subprocess
my_ip='192.168.1.1'
ipList=[]
from pprint import pprint
for i in range(50):
    ipList.append('255.255.'+str(random.randrange(1,255))+'.'+str(random.randrange(1,255)))

ipList2=['255.255.'+str(random.randrange(1,255))+'.'+str(random.randrange(1,255)) for i in range(50)]
#pprint(ipList2)
filename='stats'
filetype='.txt'
filename+=filetype
apple= subprocess.call(["ls", "-l"])#echo","hello world"])
#subprocess.(["ipconfig"])#echo","hello world"])
#with open('stats.txt','r') as stats:
#    print(stats.read())
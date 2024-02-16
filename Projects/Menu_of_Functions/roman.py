roman={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'VIIII',10:'X',50:'L'}
roman_keys=list(roman.keys())
revrom={}
for key in roman_keys:
    revrom[roman[key]]=key
print(revrom)

num=12
def romanNum(num):
    if num>9:
        numPosTens=num//10
    numPosOnes=num%10
    if numPosOnes>=5:
        rom1=roman[5+(numPosOnes%5)]
    elif numPosOnes<5 and numPosOnes!=0:
        rom1=roman[(numPosOnes%5)]
    else:
        rom1=''
    
    if numPosTens<4:
        rom10=roman[10]*numPosTens
    elif numPosTens==4:
        rom10=roman[10]+roman[50]
    else:
         rom10=roman[50]+roman[10]*(numPosTens%5)
    return rom10+rom1
print(romanNum(99))


#print(revroman['III'])
import subprocess
subprocess.call(['ping google.com'])
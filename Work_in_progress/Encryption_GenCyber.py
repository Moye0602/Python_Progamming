#word='abcefghijklmnopqrstuvwxyz'

from icecream import *
def entry():
    word= input('What do you want to say? ')
    word=word.lower()
    method=[]
    crypto_key_entry=None
    while crypto_key_entry!='':
        crypto_key_entry=input('What is your cipher key?')
        print('                           ',end="\033[F"*(1))
        if crypto_key_entry=='':
            break
        method.append(int(crypto_key_entry))
        continue
    print('key:',method,'                     ')
    #print(word)
    return(method,word)

def encrypt_a_word(method,word):
    encrypt_word={}
    base_Dictionary={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
                     'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,
                    't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':0,'.':99}
    reverse_Dictionary={}
    roman_keys=list(base_Dictionary.keys())
    reverse_Dictionary={}
    for key in roman_keys:
        reverse_Dictionary[base_Dictionary[key]]=key
    encrypt_word_list=[]
    loop=0
    for letter in word:
        loop+=1
        if letter not in encrypt_word:
            encrypt_word[letter]=base_Dictionary[letter]
            ic()
            if letter not in base_Dictionary:
                base_Dictionary[letter]=len(base_Dictionary)+1
                ic()
                print(base_Dictionary)
            encrypt_word_list.append(base_Dictionary[letter])
        else:
            encrypt_word[letter+' '+str(loop)]=base_Dictionary[letter]
            encrypt_word_list.append(base_Dictionary[letter])
#    print(encrypt_word)#dictionary created for phrase
    
#    print(encrypt_word_list)#number value after encryptio
    for value in method:
        if value%2==0: 
            for letter in encrypt_word:
                if encrypt_word[letter]+value>=27:
                    encrypt_word[letter]=encrypt_word[letter]+value-26
                    
                elif encrypt_word[letter]==0:
                    encrypt_word[letter]=0
                else:
                    encrypt_word[letter]=encrypt_word[letter]+value
        if value%2==1: 
            for letter in encrypt_word:
                if encrypt_word[letter]==0:
                        encrypt_word[letter]=0
                elif encrypt_word[letter]-value<1:
                    encrypt_word[letter]=encrypt_word[letter]-value+26
                else:
                    encrypt_word[letter]=encrypt_word[letter]-value
#not used           print(letter,encrypt_word[letter])
#not used           print(encrypt_word_list)
            
#        print(encrypt_word)#print encryption dictionary

    encrypt_out=[]
    for char in encrypt_word:
       encrypt_out.append(reverse_Dictionary[encrypt_word[char]]) 
    message=''.join(encrypt_out)
    print(message)
    save_encryption=open('GenCyber_Secret_Message','w')
    save_encryption.write(str(message)+'='+str(encrypt_word))
    save_encryption.close()
if 0:
    while 1:
        try:
            method,word=entry()
            encrypt_a_word(method,word)
            word.clear()
            method.clear()
        except Exception:
            continue
def reverse_entry():
    eword= input('What was the message? ')
    eword=eword.lower()
    emethod=[]
    ecrypto_key_entry=None
    while ecrypto_key_entry!='':
        ecrypto_key_entry=input('What is the cipher key?')
        print('                           ',end="\033[F"*(1))
        if ecrypto_key_entry=='':
            break
        emethod.append(int(ecrypto_key_entry))
        emethod.reverse()
        continue
    print('key:',emethod,'                     ')
    #print(eword)
    return(emethod,eword)
#emethod,eword=reverse_entry()
def decrypt_a_word(method,word):
   
    encrypt_word={}
    base_Dictionary={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
                     'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,
                    't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':0,'.':99}
    reverse_Dictionary={ 1 :"a",2  :"b",3  :"c",4  :"d",5  :"e",6  :"f",
                        7 :"g",8  :"h",9  :"i",10 :"j",11 :"k",12 :"l",13 :"m",
                        14 :"n",15 :"o",16 :"p",17 :"q",18 :"r",19 :"s",20 :"t",
                        21 :"u",22 :"v",23 :"w",24 :"x",25 :"y",26 :"z",0 :" ",99:'.'}
    encrypt_word_list=[]
    loop=0
    for letter in word:
        loop+=1
        if letter not in encrypt_word:
            encrypt_word[letter]=base_Dictionary[letter]
            encrypt_word_list.append(base_Dictionary[letter])
        else:
            encrypt_word[letter+' '+str(loop)]=base_Dictionary[letter]
            encrypt_word_list.append(base_Dictionary[letter])
#    print(encrypt_word)#dictionary created for phrase
    
#    print(encrypt_word_list)#number value after encryptio
    for value in method:
        if value%2==1: 
            for letter in encrypt_word:
                if encrypt_word[letter]+value>=27:
                    encrypt_word[letter]=encrypt_word[letter]+value-26
                    
                elif encrypt_word[letter]==0:
                    encrypt_word[letter]=0
                else:
                    encrypt_word[letter]=encrypt_word[letter]+value
        if value%2==0: 
            for letter in encrypt_word:
                if encrypt_word[letter]==0:
                        encrypt_word[letter]=0
                elif encrypt_word[letter]-value<1:
                    encrypt_word[letter]=encrypt_word[letter]-value+26
                else:
                    encrypt_word[letter]=encrypt_word[letter]-value
#not used           print(letter,encrypt_word[letter])
#not used           print(encrypt_word_list)
            
#        print(encrypt_word)#print encryption dictionary

    encrypt_out=[]
    for char in encrypt_word:
       encrypt_out.append(reverse_Dictionary[encrypt_word[char]]) 
    message=''.join(encrypt_out)
    print(message)
word,eword=None,None
while 1:
    try:
        while word!='decrypt':
            try:
                method,word=entry()
                if word=='decrypt' and method[0]==0:
                    eword=word
                    continue
                encrypt_a_word(method,word)
                print()
                word.clear()
                method.clear()
            except Exception:
                #print("Let's decrypt a message")
                continue
        while eword!='encrypt':
            try:
                emethod,eword=reverse_entry()
                if eword=='encrypt' and emethod[0]==0:
                #    print('stuck on loop here')
                    word=eword
                    continue
                decrypt_a_word(emethod,eword)
                print()
                eword.clear()
                
                emethod.clear()
            except Exception:
                print("Let's encrypt a message")
                continue
            if eword=='encrypt' and emethod[0]==0:
                    #    print('stuck on loop here')
                word='encrypt'
        continue
    except KeyboardInterrupt:
        pass
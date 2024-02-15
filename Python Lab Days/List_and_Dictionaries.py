import time
#from Admin import*
list1=[1,2,3,4,5,6,7,8,9,10]
print('list1:',list1,'\n')

##################
list2=[]
for i in range(10):
    list2.append(i)
print('list2:',list2,'\n')

##################
list3=[ i for i in range(1,11) if(any([i%2,i>6]))]
list4=[]
for i in range(1,11):
    if(any([i%2,i>6])):
        list4.append(i)


print(list3)
print(list4)
dict1={i:i**2 for i in range (11)}
print(dict1)
dict1['A']=225
list4.append('A')

print(dict1[3])
print(dict1['A'])

print(list4[4])
print(list4['A'])



time.sleep(900000)
list3.pop()
print('list3 pop:',list3)
print('list3 count:',list3.count(2))
print('list3 index:',list3.index(5))


#################
import random
list4=[random.randrange(0,100) for i in range (10)]

print('list4 unsorted:',list4)
list4.sort()
print('list4 sorted:',list4)
print('list4 set:',list(set(list4)))


################
print()
book1={'Name':[],'buyPrice':[],'sellPrice':[],'P/L':[],'sellType':[],'Equity':[],'EqChng':[]}
book1['Name']=['John Smith']
print('book1:',book1,'\n')


###############
from faker import Faker
fake=Faker()

book2={ 'First Name':[fake.name()],
        'Last Name':[fake.name()],
        'Address':[fake.address()],
        'Email':[fake.free_email()],
        'Phone Number':[fake.basic_phone_number()],
        'DoB':[fake.date_of_birth()]}
print(book2,'\n')


###############
people=100
from datetime import datetime
book3={ 'First Name':[str(fake.name()).split(' ')[0] for person in range (people)],
        'Last Name':[str(fake.name()).split(' ')[1] for person in range (people)],
        'Address':[fake.address() for person in range (people)],
        'Email':[fake.free_email() for person in range (people)],
        'Phone Number':[fake.basic_phone_number() for person in range (people)],
        'DoB':[str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] for person in range (people)]}

crayon(['<'*5,'normal dictionary',5*'>'],'cyan')
print(book3)
#timeout(5)
import pprint
crayon(['<'*5,'pprint of a dictionary',5*'>'],'cyan')
print()
pprint.pprint(book3)
print()
#timeout(5)
import pandas as pd

datafram=pd.DataFrame(book3)
crayon(['<'*5,'Pandas dataframe of dictionary',5*'>'],'cyan')
print(datafram,'\n'*2)
crayon(['keys>>>',datafram.keys()],'cyan')
#timeout(5)
################
if 1:
    people=5
    from datetime import datetime
    book3={}
    for num in range(people):
        book3[num]={'First Name':str(fake.name()).split(' ')[0] ,
            'Last Name':str(fake.name()).split(' ')[1],
            #'Address':fake.address(),
            'Email':fake.free_email(),
            'Phone Number':fake.basic_phone_number(),
            'DoB':str(datetime.fromisoformat(str(fake.date_of_birth())))[:10]}
    from datetime import datetime
    #import Admin
    Admin.insideout('stuff')
    crayon(['<'*5,'normal',5*'>'],'cyan')
    print(book3)
    timeout(9000)
    import pprint
    crayon(['<'*5,'pprint',5*'>'],'cyan')
    print()
    pprint.pprint(book3)
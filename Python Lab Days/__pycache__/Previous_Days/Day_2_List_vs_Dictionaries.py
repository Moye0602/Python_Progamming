''' remember if there is an "if 0" in above the the code, then it's turned off
switch it to "if 1" to turn on that segment of code'''

'''a basic list'''
list1=[1,2,3,4,5,6,7,8,9,10]
print('list1:',list1,'\n')

##################
''' a list created by a for loop'''
if 0:
    list2=[]
    for i in range(10):
        list2.append(i)
    print('list2:',list2,'\n')

##################
'''a one line list created by a for loop '''
if 0:
    list3=[ i for i in range(1,11)]
    print('list3:',list3,'\n')

##################

'''list data call outs'''
if 0:
    list3.pop()
    print('list3 pop:',list3)
    print('list3 count:',list3.count(2))
    print('list3 index:',list3.index(5))


#################
''' list sorting and removing duplicates'''
if 0:
    import random
    list4=[random.randrange(0,100) for i in range (50)]

    print('list4 unsorted:',list4)
    list4.sort()
    print('list4 sorted:',list4)
    print('list4 set:',list(set(list4)))


################
'''a dictionary'''
if 0:
    print()
    book1={'Name':[],'buyPrice':[],'sellPrice':[],'P/L':[],'sellType':[],'Equity':[],'EqChng':[]}
    book1['Name']=['John Smith']
    print('book1:',book1,'\n')


###############
from faker import Faker
fake=Faker()
'''inputing data into a dictionary'''
if 0:
    people=5
        
    book2={ 'First Name':[str(fake.name()).split(' ')[0] for person in  range (people)],
            'Last Name':[str(fake.name()).split(' ')[1] for person in  range (people)],
            'Address':[fake.address() for person in  range (people)],
            'Email':[fake.free_email() for person in  range (people)],
            'Phone Number':[fake.basic_phone_number() for person in  range (people)],
            'DoB':[fake.date_of_birth() for person in  range (people)]}
    print(book2,'\n')


###############

'''expanding a dictionary with lists'''
if 0:
    
    print([str(fake.name()).split(' ')[0] for person in range (people)])

if 0:
    people=50
    from datetime import datetime
    book3={ 
            'Email':[fake.free_email() for person in range (people)],
            'Address':[fake.address() for person in range (people)],
            'Last Name':[str(fake.name()).split(' ')[1] for person in range (people)],
            'Phone Number':[fake.basic_phone_number() for person in range (people)],
            'DoB':[str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] for person in range (people)],
            'First Name':[str(fake.name()).split(' ')[0] for person in range (people)]}
            
'''what does a dictionary look like as an output?'''
if 0:
    print('<'*5,'normal',5*'>','\n',book3)

    import pprint
    print('<'*5,'pprint',5*'>','\n',)
    pprint.pprint(book3)
    print()

'''a different way of showing a dictionary'''
if 0:
    import pandas as pd
    dataframe=pd.DataFrame(book3)
    print(dataframe,'\n'*2)
    print('keys>>>',dataframe.keys())
    my_keys=list(book3.keys())
    print(book3[my_keys[4]])

################
if 0:
    people=5
    from datetime import datetime
    book3={ 'First Name':[str(fake.name()).split(' ')[0] for person in range (people)],
            'Last Name':[str(fake.name()).split(' ')[1] for person in range (people)],
            'Address':[fake.address() for person in range (people)],
            'Email':[fake.free_email() for person in range (people)],
            'Phone Number':[fake.basic_phone_number() for person in range (people)],
            'DoB':[str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] for person in range (people)]}
    print('<'*5,'normal',5*'>','\n',book3)

if 0:
    import pprint
    print('<'*5,'pprint',5*'>','\n',)
    pprint.pprint(book3)

    import pandas as pd

    dataframe=pd.DataFrame(book3)
    print(dataframe)
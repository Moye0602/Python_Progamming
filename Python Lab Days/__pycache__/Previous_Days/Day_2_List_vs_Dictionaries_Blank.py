'''a basic list'''
list1=[1,2,3,4,5,6,7,8,9,10]
print('list1:',list1,'\n')

##################
''' a list created by a for loop'''
#print('list2:',list2,'\n')

##################
'''a one line list created by a for loop '''
#print('list3:',list3,'\n')

##################

'''list data call outs'''
#print('list3 pop:',list3)
#print('list3 count:',list3.count(2))
#print('list3 index:',list3.index(5))


#################
''' list sorting and removing duplicates'''
import random
#print('list4 unsorted:',list4)

#print('list4 sorted:',list4)
#print('list4 set:',list(set(list4)))


################
'''a dictionary'''
print()

#print('book1:',book1,'\n')


###############

'''inputing data into a dictionary'''
from faker import Faker
fake=Faker()

#    print(book2,'\n')


###############
'''expanding a dictionary with lists'''
people=5
#print([str(fake.name()).split(' ')[0] for person in range (people)])

from datetime import datetime

'''what does a dictionary look like as an output?'''
#print('<'*5,'normal',5*'>','\n',book3)

import pprint
#print('<'*5,'pprint',5*'>','\n',)
#pprint.pprint(book3)
print()

'''a different way of showing a dictionary'''
import pandas as pd

#print(dataframe,'\n'*2)
#print('keys>>>',dataframe.keys())

################
'''whats the best way to show a dataframe?'''
people=5
from datetime import datetime

#print('<'*5,'normal',5*'>','\n',book3)




'''can we  use pprint to show a '''
import pprint
#print('<'*5,'pprint',5*'>','\n',)
#pprint.pprint(book3)


'''what about a pandas dataframe?'''
import pandas as pd

#print(dataframe)

####################
''' what if we dont want to waste time creating (or requesting) data?'''
if 0:
    #try:
        import helper
        from my_data import book

    #except ImportError as errorcode:
    #    book3={'test':[1,2,3]}
    #    with open('my_data.py','w') as writeFile:
    #        writeFile.write('book='+str(book3))
    #    writeFile.close()
    #    print(errorcode)
#print(book3)
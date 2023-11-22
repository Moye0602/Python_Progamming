#######
"""Welcome to the Radio Challenge,
    When this file is executed, a list of people and items are given
    Each person needs find someone 
    Each person also has an item they need and an item to give

    The point of the game is to relay message what each person has to the group
    and get the items and people paired up as quickly as possible
 """

######
from RC_What_to_Find import people, emergancy_items
from random import randint

def call_a_phone(i_have):
    phone_number=None
    if i_have=='Cell phone':
        #print('ihave it',i_have)
        phone_number="("+str(randint(211,888))+")-"+str(randint(211,888))+'-'+str(randint(2110,8889))
    return phone_number

def food_type(i_have):
    if i_have =='Food':
        perishability='perishable'
        if randint(0,100)>50:
            perishability='Non-perishable'
    return perishability

def batt_type (i_need,i_have):
    battery=None
    batt_size={0:'AAA',1:"AA",2:"C",3:"D",4:"Battery Pack"}
    if i_need=='Batteries' or i_have=='Batteries':
        batt_sizeN=randint(0,100)//25
        battery=batt_size[batt_sizeN]
    return battery
    
        




players=6
PeopleTOpair={}
for i in range(players):
    name=(people[randint(0,len(people))])   
    PeopleTOpair[name]={'person to find':None,'item to find':None}
find_a_friend=list(PeopleTOpair.keys())
find_some_gear=list(emergancy_items.keys())


for player in PeopleTOpair:
    person_to_find=find_a_friend[randint(0,len(find_a_friend)-1)]
    item_to_find=  find_some_gear[randint(0,len(find_some_gear)-1)]
    i_have=  find_some_gear[randint(0,len(find_some_gear)-1)]
    phone_number=call_a_phone(i_have)
    battery=batt_type (item_to_find,i_have)
    if phone_number!=None:
        i_have=i_have+' '+str( phone_number)
    if battery!=None:
        if i_have=='Batteries':
            i_have=str(battery)+' '+i_have
        else:
            item_to_find=str(battery)+' '+item_to_find
    while person_to_find ==player:
        person_to_find=find_a_friend[randint(0,len(find_a_friend))]
    while i_have==item_to_find:
        i_have=  find_some_gear[randint(0,len(find_some_gear)-1)]
        phone_number=call_a_phone(i_have)
        battery=batt_type (item_to_find,i_have)
    PeopleTOpair[player]['person to find']=person_to_find
    
    PeopleTOpair[player]['item to find']=  item_to_find
    
    PeopleTOpair[player]['item to give']=  i_have

for player in PeopleTOpair:
    print(player,PeopleTOpair[player])
    print()
people_frame={'Person':[person for person in PeopleTOpair],'Item to give':[[itemToGive for itemToGive in PeopleTOpair[person]] for person in PeopleTOpair],'Item I have':[[itemToGive for itemToGive in PeopleTOpair[person]] for person in PeopleTOpair]}
#print(person,PeopleTOpair[person],'\n'*2)
import pandas as pd
People_dataFrame=pd.DataFrame(PeopleTOpair)
#People_dataFrame.loc[len(People_dataFrame.index)]= ['Person','Person to Find','item to find','item to give']
#print(People_dataFrame)
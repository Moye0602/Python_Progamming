<<<<<<< HEAD:Projects/Database_DisneyLand/Digital_Disney.py
"""This project will simulate lead to the following
    1. creating classes to more efficiently use functions and use memory efficiently
    2. simulate a theme park of patrons and actions by patrons
    3. store the actions of the simulated patrons
    4. analyze the actions and trends of the simulated theme park
    """
from collections import defaultdict
from datetime import datetime,date,timedelta
from faker import Faker
from pprint import pprint   #for debuging
from icecream import * #for debuging
import pandas as pd
import random
import tkinter as tk
fake=Faker()
# this is the method of activating a class
def blank():
    print(' '*110,'|',end='\r')

def crayon(statement='>>here i am<<',color='yellow'):
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed."""
    from termcolor import colored
    blank()
    if type(statement)==list:
        state=''
        for word in statement:
            state+=str(word)+' '
        statement=[word for word in statement]
        statement=state
    elif statement!=list and type(statement)!=str:
        statement=str(statement)
    try:
        print(colored(statement,color))
    except TypeError:
        print(statement)


class Disney_Land():
    import Disney_Land_Data as Disney_Land_Data
    #this is how you start defining a class
    def __init__(self,database=Disney_Land_Data.database):

        self.guestlist={}
        self.guestlibrary=database
        self.colors=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
#        the first function will always start with "__init__" to initialize any variables in the functions to follow.
#        self.guest=guest_today
    def patrons(self,guest_today):
        
        def format_phone_number(phone_number):
#             Remove non-numeric characters
            numeric_chars = [char for char in phone_number if char.isdigit()]
            
#             Format the phone number with parentheses and hyphens
            formatted_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numeric_chars)
            
            return formatted_number

#         Apply the formatting function to phone numbers            
        self.guestlist={ 'First_Name':[str(fake.name()).split(' ')[0] for person in range (guest_today)],
        'Last_Name':[str(fake.name()).split(' ')[1] for person in range (guest_today)],
        'Guest_Id':[num for num in range(0,guest_today)],
        'Address':[fake.address() for person in range (guest_today)],
        'Email':[fake.free_email() for person in range (guest_today)],
        'Phone_Number':[fake.basic_phone_number() for person in range (guest_today)],
        'DoB':[str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] for person in range (guest_today)],
        'Age_Cat':[[15,'young'] for person in range(guest_today)]
        }
        guest_id=0
        for person in range (guest_today):
            guest_id+=1
            self.guestlibrary[guest_id]={ 
                'Guest_Id':guest_id,
                'First_Name':str(fake.name()).split(' ')[0] ,
                'Last_Name':str(fake.name()).split(' ')[1] ,
                'Address':fake.address() ,
                'Email':fake.free_email() ,
                'Phone_Number':fake.basic_phone_number() ,
                'DoB':str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] ,
                'Age_Cat':[15,'young'] # default value when creating patrons
                 }
        
#         becuase the faker module sometimes creates bad data, we need to sanatize/reformat certain sections
        self.guestlist['Address'] = [address.replace('\n', ' ') for address in self.guestlist['Address']]
        self.guestlist['Phone_Number'] = [format_phone_number(phone) for phone in self.guestlist['Phone_Number']]
        
#        now lets add more details like age category this will simplify some things later by just identifying each patron by an  age category
        today=datetime.today()
#            while normally it would be okay to place date.today in the condition, it's faster to create the variable once and reference it each time rather than calculate it
        for guest_age in self.guestlist['DoB']:
            age= int(((today-datetime.fromisoformat(guest_age)).days)/365)
            if age<4: 
                age=4
                
            elif age>50:
                age=14+random.randint(0,5)
            
#             while typically this would be an else statement, setting it as the default value ensures something a categroy will always be given
            age_cat='minor' 
#             the following conditions check for age in one of two ranges, the top modifies the age to get a more realistic ratio of aults to young adults/children
#            the second if /else statement places each guest into one of the two remaining categories if the conditions are met
            if age>=13 and age<18:
                age-=random.randint(0,5)
            if age>=18:
                age_cat='adult'    
            elif age>=13 and age<18:
                age_cat='young'
            self.guestlist['Age_Cat'][self.guestlist['DoB'].index(guest_age)]=[age,age_cat]

            for guest_id in self.guestlibrary:
                age= int(((today-datetime.fromisoformat(self.guestlibrary[guest_id]['DoB'])).days)/365)
                if age<4: 
                    age=4
                elif age>50:
                    age=14+random.randint(0,5)
                # while typically this would be an else statement, setting it as the default value ensures something a categroy will always be given
                age_cat='minor' 
                # the following conditions check for age in one of two ranges, the top modifies the age to get a more realistic ratio of aults to young adults/children
                #the second if /else statement places each guest into one of the two remaining categories if the conditions are met
                if age>=13 and age<18:
                    age-=random.randint(0,5)
                if age>=18:
                    age_cat='adult'    
                elif age>=13 and age<18:
                    age_cat='young'
                self.guestlibrary[guest_id]['Age_Cat']=[age,age_cat]
                if age>=18:
                    self.guestlibrary[guest_id]['Spouse']=None
                else:
                    self.guestlibrary[guest_id]['Parent_Id']=None
        

#!    ## this can be combined into the above function of patrons
#        next we identify if a patron is a child or an adult 
        for guest_id in self.guestlibrary:
            self.guestlibrary[guest_id]['Guest_Type']='Child'
            if self.guestlibrary[guest_id]['Age_Cat'][1]=='adult':
#                 if a patron is an adult, give them the guest type "Parent" with a an empty list of children to be populated later
                self.guestlibrary[guest_id]['Guest_Type']='Parent'
                self.guestlibrary[guest_id]['Children']=[]
#! this could be condensed in a previous loop  
#next we make a random decision of creating one and two parent families
        for guest_id in self.guestlibrary:
            guest_spouse=random.randint(1,len(self.guestlibrary))
            if random.randint(0,1)==1 and self.guestlibrary[guest_id]['Guest_Type']=='Parent':
                while  1:
#iterate through guest until a pair is made
                    if self.guestlibrary[guest_spouse]['Guest_Type']=='Parent' and 'Spouse' in self.guestlibrary[guest_spouse] and self.guestlibrary[guest_spouse]['Spouse']==None:
                        break
                    elif self.guestlibrary[guest_spouse]['Guest_Type']=='Child' or 'Spouse' in self.guestlibrary[guest_spouse] and self.guestlibrary[guest_spouse]['Spouse']!=None:
                        guest_spouse=random.randint(1,len(self.guestlibrary))
                        continue
#update the guest library and associate the spouses with each other and create an empty children list
                self.guestlibrary[guest_id]['Spouse']=guest_spouse
                self.guestlibrary[guest_spouse]['Spouse']=guest_id
                self.guestlibrary[guest_spouse]['Children']=[]
            #two parent family
#                family_color=colors[random.randint(0,len(colors)-1)]
#                crayon(self.guestlibrary[guest_id],family_color)    
#                crayon(self.guestlibrary[guest_spouse],family_color)
#                print()
            #one parent family
            #print('>>',self.guestlibrary[guest_id])#
            #print()
                
        for child_id in self.guestlibrary:
            if self.guestlibrary[child_id]['Guest_Type']=='Child':
                parent_id=random.randint(1,len(self.guestlibrary))
                while 1:
                    parent_id=random.randint(1,len(self.guestlibrary))
                    if self.guestlibrary[parent_id]['Guest_Type']=='Parent':
                        if  self.guestlibrary[child_id]['Parent_Id']==None:
                            self.guestlibrary[child_id]['Parent_Id']=parent_id
                        self.guestlibrary[parent_id]['Children'].append(child_id)
                    break
# show the family in full
                if 0: # 1 will show the familiy
                    print('Parent 1:',self.guestlibrary[parent_id])
                    if 'Spouse' in self.guestlibrary[parent_id] and self.guestlibrary[parent_id]['Spouse']!=None:
                        print('Parent 2:',self.guestlibrary[self.guestlibrary[parent_id]['Spouse']])
                    child=1
                    for kids in self.guestlibrary[parent_id]['Children']:
                        print('Child '+str(child)+':',self.guestlibrary[kids])
                        child+=1
                    print()
        #return self.guestlist #list version
# ehh nothing ever perfect but we can catch the lost children we created with this list below
        lost_children=[guest for guest in self.guestlibrary if (self.guestlibrary[guest]['Guest_Type']=='Child')]
        for child_id in lost_children:
            parent_id=random.randint(1,len(self.guestlibrary))
            if self.guestlibrary[parent_id]['Guest_Type']=='Parent':
                if  self.guestlibrary[child_id]['Parent_Id']==None:
                    self.guestlibrary[child_id]['Parent_Id']=parent_id
                self.guestlibrary[parent_id]['Children'].append(child_id)
        self.family()
        return self.guestlibrary,self.guestlist

    def guest_info_associate(self,guest_id_primary,guest_id_secondary):
            '''Assosicates secondary guest to a primary guest/parent'''
            self.guestlibrary[guest_id_secondary]['Last_Name']=self.guestlibrary[guest_id_primary]['Last_Name']
            self.guestlibrary[guest_id_secondary]['Address']=self.guestlibrary[guest_id_primary]['Address']

    def family(self):
        """Generates a new list of families based on the existing patrons"""
        self.household={}
        family_num=1
        for guest_id in self.guestlibrary:
            if self.guestlibrary[guest_id]['Guest_Type']=='Parent' and self.guestlibrary[guest_id]['Age_Cat']!='minor':
                self.household[family_num]={'Family':{'Parents':[guest_id]}}
                if 'Spouse' in self.guestlibrary[guest_id] and self.guestlibrary[guest_id]['Spouse']!=None:
                    self.guest_info_associate(guest_id,self.guestlibrary[guest_id]['Spouse'])
                    self.household[family_num]['Family']['Parents'].append(self.guestlibrary[guest_id]['Spouse'])
                if 'Children' in self.guestlibrary[guest_id] and len(self.guestlibrary[guest_id]['Children'])>0:
                    #print(self.guestlibrary[guest_id],len(self.guestlibrary[guest_id]['Children']))
                    self.household[family_num]['Family']['Children']=[]
                    for child in range(0,len(self.guestlibrary[guest_id]['Children'])):
                        child_id=self.guestlibrary[guest_id]['Children'][child]
                        self.guest_info_associate(guest_id,child_id)
                        self.household[family_num]['Family']['Children'].append(child_id)
                
                
                self.household[family_num]['Family_Color']=self.colors[random.randint(0,len(self.colors)-1)]
                crayon([family_num,self.household[family_num]],self.household[family_num]['Family_Color'])
                print()
                family_num+=1
        path=__file__.split('\\')
        path=('\\').join(path[:-1])+'\\'
        with open(path+'Disney_Land_Data.py','w') as write_disneyland:
            write_disneyland.write('save_time="'+str(datetime.now())+'"\n'+
            'database='+str(self.guestlibrary)+'\n'+'household_library='+str(self.household)+'\n')
    

class File_Handler:
    def __init__(self,Themepark_libary={},current_time=datetime.now()):
        import Disney_Land_Data as Disney_Land_Data
        if 0: #auto generate new info if stale
            try:       
                
                #Themepark_libary=Disney_Land_Data.database['Age_Cat']
                patron_count=int(len(Disney_Land_Data.database))#*(random.randint(80,120)/100))
                if any( [len(Themepark_libary)==0 , datetime.fromisoformat(Disney_Land_Data.save_time)<current_time-timedelta(minutes=30)]):
                    #print(Disney_Land_Data.save_time,current_time-timedelta(minutes=30))
                    disney_land=Disney_Land()
                    Themepark_data=disney_land.patrons(patron_count)
                else:
                    Themepark_data=Disney_Land_Data.database
            except Exception as err:
                    print(err)
                    disney_land=Disney_Land()
                    Themepark_data=disney_land.patrons(patron_count)
        #self.database=Themepark_data
        self.database=Disney_Land_Data.database
        self.houesholds=Disney_Land_Data.household_library
        self.time=current_time
        self.load_time=Disney_Land_Data.save_time
    def save_file(self,file):
        path=__file__.split('\\')
        path=('\\').join(path[:-1])+'\\'
#        path is is finds your current directory based on the file we're working with and uses everything but the file name as a directory to save in
        with open(path+'Disney_Land_Data.py','w') as write_file:
            write_file.write('save_time="'+str(self.time)+'"\n'+'database='+str(file)+'\n'+'household_library='+str(self.houesholds)+'\n'*2)
            print('File Saved @',self.time)

    def load_file(self):
        print('File loaded from',self.load_time)
        return self.database,self.houesholds

class Analysis():
    
    
    def __init__(self):
        self.tpd,self.households=File_Handler().load_file()

        #as we come up with more questions to analyze the data, we can add key things to the __init_ function which is pulled into other functions 
        #this pointer saves time in typing and make memory management easier
    def show_family(self,family_id=0):
        if family_id!=0:
            for familiy_member_cat in self.households[family_id]['Family']:
                for guest_id in self.households[family_id]['Family'][familiy_member_cat]:
                    crayon(self.tpd[guest_id],self.households[family_id]['Family_Color'])
        else:
            for family_id in self.households:
                #print(self.households[family_id])
                for familiy_member_cat in self.households[family_id]['Family']:
                    #print(self.households[family_id]['Family'][familiy_member_cat])
                    for guest_id in self.households[family_id]['Family'][familiy_member_cat]:
                        crayon(self.tpd[guest_id],self.households[family_id]['Family_Color'])
                print()
    def age_groups(self):
        crayon('Age Groups')
        age_groups=defaultdict(int)
        for guest_id in self.tpd:
            age_groups[self.tpd[guest_id]['Age_Cat'][1]]+=1
        return dict(age_groups)
    
    def child_count(self):
        crayon('Child count per family')
        child_count=defaultdict(int)
        for guest_id in self.tpd:
            if self.tpd[guest_id]['Guest_Type']=='Parent' :
                child_count[len(self.tpd[guest_id]['Children'])]+=len(self.tpd[guest_id]['Children'])
        return dict(child_count)
    
    def orphans(self):
        print([guest for guest in self.tpd if (self.tpd[guest]['Guest_Type']=='Child')])
    
    #def child_count(self):

class Attractions:
    def __init__(self):
        self
        self.guest_list=File_Handler().load_file()
    
    def get_attractions(self,guest,age_group):
        import time
        attraction_library={"Space Mountain":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Pirates of the Caribbean":{'age_cats':{'young','adult'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Haunted Mansion":{'age_cats':{'young','adult'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Splash Mountain":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Big Thunder Mountain Railroad":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "It's a Small World":{'age_cats':{'minor','young'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Indiana Jones Adventure":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Peter Pan's Flight":{'age_cats':{'minor','young'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "The Jungle Cruise":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Matterhorn Bobsleds":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Enchanted Tiki Room":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Buzz Lightyear Astro Blasters":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Dumbo the Flying Elephant":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Ratatouille: The Adventure":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Star Tours, The Adventures Continue":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "California Screamin":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Alice in Wonderland":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Finding Nemo Submarine Voyage":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "The Twilight Zone Tower of Terror":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Walt Disney's Carousel of Progress":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}}}


class DisneylandSimulation:
    
    def __init__(self,  families, patrons,zones={}):
        if len(zones)==0:
            from Disney_Land_Zones import zones    
        self.zones = zones
        self.patrons=patrons
        self.families = families
        self.family_assignments = {}
        self.family_biases = {family: random.choice(["attractions", "diner", "shopping"]) for family in families}
        self.location_metrics = {zone: {category: 0 for category in ["attractions", "diner", "shopping"]} for zone in zones}

    def assign_families_to_locations(self):
        for family in self.families:
            location,zone,category = self.choose_location_for_family(family)
            self.family_assignments[family] = [location,zone,category]

    def choose_location_for_family(self, family):
        bias = self.family_biases[family]
        zone = random.choice(list(self.zones.keys()))
#         Choose a category based on the family's bias
        rng,rng_limit=random.randint(1, 100),60
        category=bias
        if any([bias == "attractions" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "attractions"
        elif any([bias == "diner" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "diner"
        elif any([bias == "shopping" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "shopping"
#        print(bias==category or rng==True)
#        print(rng==True)
#        print(bias==category,'\n')
#         Choose a specific location within the selected zone and category
        location = random.choice(self.zones[zone][category])
        # Increment the patron count for the chosen location
        self.location_metrics[zone][category] += 1
        return location,zone,category


    def optimize_location_assignments(self):
        for zone in self.zones:
            for category in ["attractions", "diner", "shopping"]:
                # Check if the category dictionary is empty
                if self.location_metrics[zone][category]:
                    least_busy_location = min(self.location_metrics[zone], key=self.location_metrics[zone].get)

                    for family in self.families:
                        if self.family_assignments[family] not in [least_busy_location] + self.get_adjacent_locations(least_busy_location, zone, category):
                            self.family_assignments[family] = least_busy_location
                            #print(self.location_metrics[zone])
                            #print(self.location_metrics[zone][category])
                            #print(self.location_metrics[zone][category])
                            self.location_metrics[zone][category] += 1


    def get_adjacent_locations(self, location, zone, category):
        # Provide logic to get adjacent locations based on the park layout
        # For simplicity, assume each location has two adjacent locations
        # You may need a more sophisticated approach based on the actual layout
        return [location + "_adj1", location + "_adj2"]

    def simulate(self):
        self.assign_families_to_locations()

        # Additional step to optimize location assignments
        #self.optimize_location_assignments()
            #optimize_locations_sets everone to the same location
        # Print family assignments
        #createa  dictionary of zones,attractions and subzones
        zone_counter={local_zone:{attraction:{} for attraction in self.zones[local_zone]} for local_zone in self.zones.keys()}#mainzones
        for local_zone in zone_counter:
            for name in self.zones[local_zone]:
                for place in range (0,len(self.zones[local_zone][name])):
                    zone_counter[local_zone][name][self.zones[local_zone][name][place]]=0

            #for attraction in 
        #print(zone_counter)
        #print({attraction:{} for attraction in self.zones['Fantasyland']})#attractions
        #print({subzone:{} for subzone in self.zones['Fantasyland']['shopping']})#subzone
        #print({attraction:{} for attraction in self.zones['Fantasyland']})#attractions
    

        print("Family Assignments:")
        movement_dataframe={'Family#':[],
                            'Familiy Name':[],
                            'Familiy Size':[],
                            'Bias':[],
                            'SubZone':[],
                            'Zone':[],
                            'Location':[],
                            }

        for family, location in self.family_assignments.items():
                familiy_name=self.patrons[self.families[family]['Family']['Parents'][0]]['Last_Name']
#                print(f" Family {family}: {familiy_name} assigned to {location[0]} (Bias: {self.family_biases[family]})")
#                    print out a verbose line about the actions of the familiy
                movement_dataframe['Family#'].append(family)
                movement_dataframe['Familiy Name'].append(familiy_name)
                parents,children=len(self.families[family]['Family']['Parents']),0
                if 'Children' in self.families[family]['Family']:
                    children=len(self.families[family]['Family']['Children'])
                movement_dataframe['Familiy Size'].append(parents+children)
                                                                          #                              sum(num for num in numbers if num % 2 == 0)
                movement_dataframe['Bias'].append(self.family_biases[family])
                movement_dataframe['Zone'].append([location[1],2])
                movement_dataframe['SubZone'].append(location[2])
                movement_dataframe['Location'].append(location[0])
                zone_counter[location[1]][location[2]][location[0]]+=1
        
#        show a dataframe of families and thier locations
        print(pd.DataFrame(movement_dataframe),'\n')
#        show the patron count by zone,subzone, and attraction
        for zone in zone_counter:
            print(zone,zone_counter[zone],'\n')

#        show the ratio of patrons that are at the locatino they are biased towards
        matchh=0
        mismatch=0
        for num in range(0,len(movement_dataframe['Bias'])):
            if movement_dataframe['Bias'][num]==movement_dataframe['SubZone'][num]:
                matchh+=1
            else:
                mismatch+=1
        print('match:',matchh)
        print('mismatch:',mismatch)
        print('match ratio:',round(100*(matchh/(matchh+mismatch)),2),'%')
    # Example Usage   


class Disney_Land_Visual: 
    def __init__(self):
        pass

    def GUI(self):
        def say_hello():
            response_label.config(text="Hello!")

        def shuffle_families():
            Themepark_data,Themepark_library=Disney_Land().patrons(guest_today=200)
            Disney_Land().family()
            del Themepark_library
            self.filehandling=File_Handler()
            self.filehandling.save_file(Themepark_data)
            response_label.config(text=Disney_Land().family())

        def show_families():
            response_label.config(text=Analysis().show_family())

        def show_age_groups():
            response_label.config(text=Analysis().age_groups())

        def show_child_count():
            response_label.config(text=Analysis().child_count())
            
        # Create the main window
        root = tk.Tk()
        root.title("Disney Land Visualizer")
        
        # Add an input box
        input_entry = tk.Entry(root)
        input_entry.grid(row=1, column=0, sticky="w")
        
        # Add a label
        label = tk.Label(root, text="Welcome to Disney Land Visualizer!")
        label.grid(row=0, columnspan=2)

        # Add buttons
        #button_01 = tk.Button(root, text="Say Hello", command=say_hello)
        #button_01.grid(row=1, column=0, sticky="ew")

        button_02 = tk.Button(root, text="Shuffle Families", command=shuffle_families)
        button_02.grid(row=2, column=0, sticky="ew")

        button_03 = tk.Button(root, text="Show Families", command=show_families)
        button_03.grid(row=3, column=0, sticky="ew")
        
        button_04 = tk.Button(root, text="Show Age Groups", command=show_age_groups)
        button_04.grid(row=3, column=1, sticky="ew")
        
        button_05 = tk.Button(root, text="Show Child Count", command=show_child_count)
        button_05.grid(row=3,column=2, sticky="ew")
        #button_05.place(x=50, y=150)
        
        

        # Add a label to display the response
        response_label = tk.Label(root, text="")
        response_label.grid(row=4, columnspan=2)

        # Run the event loop
        root.mainloop()

# Assuming Disney_Land and Analysis classes are defined elsewhere
# You might need to import them here.


import Disney_Land_Data as Disney_Land_Data
if 0: #create a new data set on command
    crayon(['#'*20,'Disney Land Ini','#'*20])
    #disney_land=Disney_Land()
    Themepark_data,Themepark_library=Disney_Land().patrons(guest_today=100)
    #Disney_Land().family()
    #Disney_Land().family()
    #Themepark_data will use our class we created to create our simulated themepark

#atractions=Attractions()
#atractions.get_attractions()



if 0: #file handling 
    crayon(['#'*20,'File Handler','#'*20])
    filehandling=File_Handler()
    #filehandling.save_file(Themepark_data)
    filehandling.load_file()
    #Themepark_library=filehandling.load_file()
    # for readability we'll use a pandas data frame

if 0:#analysis
    crayon(['#'*20,'Analysis','#'*20])
    import Disney_Land_Data as Disney_Land_Data
    analyze=Analysis()
    #sort by key (Fname, Lname, phone, DoB, Age Cat, State)
    #print(analyze.age_groups())
    #print(analyze.child_count())
    #analyze.show_family(2)

    analyze.orphans()

#print('//  '*40)
#print(pd.DataFrame(Themepark_data).tail(60))
##################################
if 1:#simulation
    crayon(['#'*20,'Simulation','#'*20])
    families=Disney_Land_Data.household_library
    patrons=Disney_Land_Data.database
    disneyland_sim = DisneylandSimulation( families,patrons)
    disneyland_sim.simulate()

if 0:#GUI
    crayon(['#'*20,'GUI','#'*20])
=======
"""This project will simulate lead to the following
    1. creating classes to more efficiently use functions and use memory efficiently
    2. simulate a theme park of patrons and actions by patrons
    3. store the actions of the simulated patrons
    4. analyze the actions and trends of the simulated theme park
    """
from collections import defaultdict
from datetime import datetime,date,timedelta
from faker import Faker
from pprint import pprint   #for debuging
from icecream import * #for debuging
import pandas as pd
import random
import tkinter as tk
fake=Faker()
# this is the method of activating a class
def blank():
    print(' '*110,'|',end='\r')

def crayon(statement='>>here i am<<',color='yellow'):
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed."""
    from termcolor import colored
    blank()
    if type(statement)==list:
        state=''
        for word in statement:
            state+=str(word)+' '
        statement=[word for word in statement]
        statement=state
    elif statement!=list and type(statement)!=str:
        statement=str(statement)
    try:
        print(colored(statement,color))
    except TypeError:
        print(statement)


class Disney_Land():
    import Disney_Land_Data as Disney_Land_Data
    #this is how you start defining a class
    def __init__(self,database=Disney_Land_Data.database):

        self.guestlist={}
        self.guestlibrary=database
        self.colors=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
#        the first function will always start with "__init__" to initialize any variables in the functions to follow.
#        self.guest=guest_today
    def patrons(self,guest_today):
        
        def format_phone_number(phone_number):
#             Remove non-numeric characters
            numeric_chars = [char for char in phone_number if char.isdigit()]
            
#             Format the phone number with parentheses and hyphens
            formatted_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numeric_chars)
            
            return formatted_number

#         Apply the formatting function to phone numbers            
        self.guestlist={ 'First_Name':[str(fake.name()).split(' ')[0] for person in range (guest_today)],
        'Last_Name':[str(fake.name()).split(' ')[1] for person in range (guest_today)],
        'Guest_Id':[num for num in range(0,guest_today)],
        'Address':[fake.address() for person in range (guest_today)],
        'Email':[fake.free_email() for person in range (guest_today)],
        'Phone_Number':[fake.basic_phone_number() for person in range (guest_today)],
        'DoB':[str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] for person in range (guest_today)],
        'Age_Cat':[[15,'young'] for person in range(guest_today)]
        }
        guest_id=0
        for person in range (guest_today):
            guest_id+=1
            self.guestlibrary[guest_id]={ 
                'Guest_Id':guest_id,
                'First_Name':str(fake.name()).split(' ')[0] ,
                'Last_Name':str(fake.name()).split(' ')[1] ,
                'Address':fake.address() ,
                'Email':fake.free_email() ,
                'Phone_Number':fake.basic_phone_number() ,
                'DoB':str(datetime.fromisoformat(str(fake.date_of_birth())))[:10] ,
                'Age_Cat':[15,'young'] # default value when creating patrons
                 }
        
#         becuase the faker module sometimes creates bad data, we need to sanatize/reformat certain sections
        self.guestlist['Address'] = [address.replace('\n', ' ') for address in self.guestlist['Address']]
        self.guestlist['Phone_Number'] = [format_phone_number(phone) for phone in self.guestlist['Phone_Number']]
        
#        now lets add more details like age category this will simplify some things later by just identifying each patron by an  age category
        today=datetime.today()
#            while normally it would be okay to place date.today in the condition, it's faster to create the variable once and reference it each time rather than calculate it
        for guest_age in self.guestlist['DoB']:
            age= int(((today-datetime.fromisoformat(guest_age)).days)/365)
            if age<4: 
                age=4
                
            elif age>50:
                age=14+random.randint(0,5)
            
#             while typically this would be an else statement, setting it as the default value ensures something a categroy will always be given
            age_cat='minor' 
#             the following conditions check for age in one of two ranges, the top modifies the age to get a more realistic ratio of aults to young adults/children
#            the second if /else statement places each guest into one of the two remaining categories if the conditions are met
            if age>=13 and age<18:
                age-=random.randint(0,5)
            if age>=18:
                age_cat='adult'    
            elif age>=13 and age<18:
                age_cat='young'
            self.guestlist['Age_Cat'][self.guestlist['DoB'].index(guest_age)]=[age,age_cat]

            for guest_id in self.guestlibrary:
                age= int(((today-datetime.fromisoformat(self.guestlibrary[guest_id]['DoB'])).days)/365)
                if age<4: 
                    age=4
                elif age>50:
                    age=14+random.randint(0,5)
                # while typically this would be an else statement, setting it as the default value ensures something a categroy will always be given
                age_cat='minor' 
                # the following conditions check for age in one of two ranges, the top modifies the age to get a more realistic ratio of aults to young adults/children
                #the second if /else statement places each guest into one of the two remaining categories if the conditions are met
                if age>=13 and age<18:
                    age-=random.randint(0,5)
                if age>=18:
                    age_cat='adult'    
                elif age>=13 and age<18:
                    age_cat='young'
                self.guestlibrary[guest_id]['Age_Cat']=[age,age_cat]
                if age>=18:
                    self.guestlibrary[guest_id]['Spouse']=None
                else:
                    self.guestlibrary[guest_id]['Parent_Id']=None
        

#!    ## this can be combined into the above function of patrons
#        next we identify if a patron is a child or an adult 
        for guest_id in self.guestlibrary:
            self.guestlibrary[guest_id]['Guest_Type']='Child'
            if self.guestlibrary[guest_id]['Age_Cat'][1]=='adult':
#                 if a patron is an adult, give them the guest type "Parent" with a an empty list of children to be populated later
                self.guestlibrary[guest_id]['Guest_Type']='Parent'
                self.guestlibrary[guest_id]['Children']=[]
#! this could be condensed in a previous loop  
#next we make a random decision of creating one and two parent families
        for guest_id in self.guestlibrary:
            guest_spouse=random.randint(1,len(self.guestlibrary))
            if random.randint(0,1)==1 and self.guestlibrary[guest_id]['Guest_Type']=='Parent':
                while  1:
#iterate through guest until a pair is made
                    if self.guestlibrary[guest_spouse]['Guest_Type']=='Parent' and 'Spouse' in self.guestlibrary[guest_spouse] and self.guestlibrary[guest_spouse]['Spouse']==None:
                        break
                    elif self.guestlibrary[guest_spouse]['Guest_Type']=='Child' or 'Spouse' in self.guestlibrary[guest_spouse] and self.guestlibrary[guest_spouse]['Spouse']!=None:
                        guest_spouse=random.randint(1,len(self.guestlibrary))
                        continue
#update the guest library and associate the spouses with each other and create an empty children list
                self.guestlibrary[guest_id]['Spouse']=guest_spouse
                self.guestlibrary[guest_spouse]['Spouse']=guest_id
                self.guestlibrary[guest_spouse]['Children']=[]
            #two parent family
#                family_color=colors[random.randint(0,len(colors)-1)]
#                crayon(self.guestlibrary[guest_id],family_color)    
#                crayon(self.guestlibrary[guest_spouse],family_color)
#                print()
            #one parent family
            #print('>>',self.guestlibrary[guest_id])#
            #print()
                
        for child_id in self.guestlibrary:
            if self.guestlibrary[child_id]['Guest_Type']=='Child':
                parent_id=random.randint(1,len(self.guestlibrary))
                while 1:
                    parent_id=random.randint(1,len(self.guestlibrary))
                    if self.guestlibrary[parent_id]['Guest_Type']=='Parent':
                        if  self.guestlibrary[child_id]['Parent_Id']==None:
                            self.guestlibrary[child_id]['Parent_Id']=parent_id
                        self.guestlibrary[parent_id]['Children'].append(child_id)
                    break
# show the family in full
                if 0: # 1 will show the familiy
                    print('Parent 1:',self.guestlibrary[parent_id])
                    if 'Spouse' in self.guestlibrary[parent_id] and self.guestlibrary[parent_id]['Spouse']!=None:
                        print('Parent 2:',self.guestlibrary[self.guestlibrary[parent_id]['Spouse']])
                    child=1
                    for kids in self.guestlibrary[parent_id]['Children']:
                        print('Child '+str(child)+':',self.guestlibrary[kids])
                        child+=1
                    print()
        #return self.guestlist #list version
# ehh nothing ever perfect but we can catch the lost children we created with this list below
        lost_children=[guest for guest in self.guestlibrary if (self.guestlibrary[guest]['Guest_Type']=='Child')]
        for child_id in lost_children:
            parent_id=random.randint(1,len(self.guestlibrary))
            if self.guestlibrary[parent_id]['Guest_Type']=='Parent':
                if  self.guestlibrary[child_id]['Parent_Id']==None:
                    self.guestlibrary[child_id]['Parent_Id']=parent_id
                self.guestlibrary[parent_id]['Children'].append(child_id)
        self.family()
        return self.guestlibrary,self.guestlist

    def guest_info_associate(self,guest_id_primary,guest_id_secondary):
            '''Assosicates secondary guest to a primary guest/parent'''
            self.guestlibrary[guest_id_secondary]['Last_Name']=self.guestlibrary[guest_id_primary]['Last_Name']
            self.guestlibrary[guest_id_secondary]['Address']=self.guestlibrary[guest_id_primary]['Address']

    def family(self):
        """Generates a new list of families based on the existing patrons"""
        self.household={}
        family_num=1
        for guest_id in self.guestlibrary:
            if self.guestlibrary[guest_id]['Guest_Type']=='Parent' and self.guestlibrary[guest_id]['Age_Cat']!='minor':
                self.household[family_num]={'Family':{'Parents':[guest_id]}}
                if 'Spouse' in self.guestlibrary[guest_id] and self.guestlibrary[guest_id]['Spouse']!=None:
                    self.guest_info_associate(guest_id,self.guestlibrary[guest_id]['Spouse'])
                    self.household[family_num]['Family']['Parents'].append(self.guestlibrary[guest_id]['Spouse'])
                if 'Children' in self.guestlibrary[guest_id] and len(self.guestlibrary[guest_id]['Children'])>0:
                    #print(self.guestlibrary[guest_id],len(self.guestlibrary[guest_id]['Children']))
                    self.household[family_num]['Family']['Children']=[]
                    for child in range(0,len(self.guestlibrary[guest_id]['Children'])):
                        child_id=self.guestlibrary[guest_id]['Children'][child]
                        self.guest_info_associate(guest_id,child_id)
                        self.household[family_num]['Family']['Children'].append(child_id)
                
                
                self.household[family_num]['Family_Color']=self.colors[random.randint(0,len(self.colors)-1)]
                crayon([family_num,self.household[family_num]],self.household[family_num]['Family_Color'])
                print()
                family_num+=1
        path=__file__.split('\\')
        path=('\\').join(path[:-1])+'\\'
        with open(path+'Disney_Land_Data.py','w') as write_disneyland:
            write_disneyland.write('save_time="'+str(datetime.now())+'"\n'+
            'database='+str(self.guestlibrary)+'\n'+'household_library='+str(self.household)+'\n')
    

class File_Handler:
    def __init__(self,Themepark_libary={},current_time=datetime.now()):
        import Disney_Land_Data as Disney_Land_Data
        if 0: #auto generate new info if stale
            try:       
                
                #Themepark_libary=Disney_Land_Data.database['Age_Cat']
                patron_count=int(len(Disney_Land_Data.database))#*(random.randint(80,120)/100))
                if any( [len(Themepark_libary)==0 , datetime.fromisoformat(Disney_Land_Data.save_time)<current_time-timedelta(minutes=30)]):
                    #print(Disney_Land_Data.save_time,current_time-timedelta(minutes=30))
                    disney_land=Disney_Land()
                    Themepark_data=disney_land.patrons(patron_count)
                else:
                    Themepark_data=Disney_Land_Data.database
            except Exception as err:
                    print(err)
                    disney_land=Disney_Land()
                    Themepark_data=disney_land.patrons(patron_count)
        #self.database=Themepark_data
        self.database=Disney_Land_Data.database
        self.houesholds=Disney_Land_Data.household_library
        self.time=current_time
        self.load_time=Disney_Land_Data.save_time
    def save_file(self,file):
        path=__file__.split('\\')
        path=('\\').join(path[:-1])+'\\'
#        path is is finds your current directory based on the file we're working with and uses everything but the file name as a directory to save in
        with open(path+'Disney_Land_Data.py','w') as write_file:
            write_file.write('save_time="'+str(self.time)+'"\n'+'database='+str(file)+'\n'+'household_library='+str(self.houesholds)+'\n'*2)
            print('File Saved @',self.time)

    def load_file(self):
        print('File loaded from',self.load_time)
        return self.database,self.houesholds

class Analysis():
    
    
    def __init__(self):
        self.tpd,self.households=File_Handler().load_file()

        #as we come up with more questions to analyze the data, we can add key things to the __init_ function which is pulled into other functions 
        #this pointer saves time in typing and make memory management easier
    def show_family(self,family_id=0):
        if family_id!=0:
            for familiy_member_cat in self.households[family_id]['Family']:
                for guest_id in self.households[family_id]['Family'][familiy_member_cat]:
                    crayon(self.tpd[guest_id],self.households[family_id]['Family_Color'])
        else:
            for family_id in self.households:
                #print(self.households[family_id])
                for familiy_member_cat in self.households[family_id]['Family']:
                    #print(self.households[family_id]['Family'][familiy_member_cat])
                    for guest_id in self.households[family_id]['Family'][familiy_member_cat]:
                        crayon(self.tpd[guest_id],self.households[family_id]['Family_Color'])
                print()
    def age_groups(self):
        crayon('Age Groups')
        age_groups=defaultdict(int)
        for guest_id in self.tpd:
            age_groups[self.tpd[guest_id]['Age_Cat'][1]]+=1
        return dict(age_groups)
    
    def child_count(self):
        crayon('Child count per family')
        child_count=defaultdict(int)
        for guest_id in self.tpd:
            if self.tpd[guest_id]['Guest_Type']=='Parent' :
                child_count[len(self.tpd[guest_id]['Children'])]+=len(self.tpd[guest_id]['Children'])
        return dict(child_count)
    
    def orphans(self):
        print([guest for guest in self.tpd if (self.tpd[guest]['Guest_Type']=='Child')])
    
    #def child_count(self):

class Attractions:
    def __init__(self):
        self
        self.guest_list=File_Handler().load_file()
    
    def get_attractions(self,guest,age_group):
        import time
        attraction_library={"Space Mountain":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Pirates of the Caribbean":{'age_cats':{'young','adult'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Haunted Mansion":{'age_cats':{'young','adult'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Splash Mountain":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Big Thunder Mountain Railroad":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "It's a Small World":{'age_cats':{'minor','young'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Indiana Jones Adventure":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Peter Pan's Flight":{'age_cats':{'minor','young'},
                            ###########################################################
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "The Jungle Cruise":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Matterhorn Bobsleds":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Enchanted Tiki Room":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Buzz Lightyear Astro Blasters":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Dumbo the Flying Elephant":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Ratatouille: The Adventure":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Star Tours, The Adventures Continue":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "California Screamin":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Alice in Wonderland":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Finding Nemo Submarine Voyage":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "The Twilight Zone Tower of Terror":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}},
                            "Walt Disney's Carousel of Progress":{'age_cats':{'minor','young','adult'},
                                            'wait_time':{'minutes':5,'seconds':30},
                                            'patrons':{'priority_guest':0,'total_guest':0,}}}


class DisneylandSimulation:
    
    def __init__(self,  families, patrons,zones={}):
        if len(zones)==0:
            from Disney_Land_Zones import zones    
        self.zones = zones
        self.patrons=patrons
        self.families = families
        self.family_assignments = {}
        self.family_biases = {family: random.choice(["attractions", "diner", "shopping"]) for family in families}
        self.location_metrics = {zone: {category: 0 for category in ["attractions", "diner", "shopping"]} for zone in zones}

    def assign_families_to_locations(self):
        for family in self.families:
            location,zone,category = self.choose_location_for_family(family)
            self.family_assignments[family] = [location,zone,category]

    def choose_location_for_family(self, family):
        bias = self.family_biases[family]
        zone = random.choice(list(self.zones.keys()))
#         Choose a category based on the family's bias
        rng,rng_limit=random.randint(1, 100),60
        category=bias
        if any([bias == "attractions" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "attractions"
        elif any([bias == "diner" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "diner"
        elif any([bias == "shopping" and rng>=rng_limit , rng<rng_limit]): #or rng>50:
            category = "shopping"
#        print(bias==category or rng==True)
#        print(rng==True)
#        print(bias==category,'\n')
#         Choose a specific location within the selected zone and category
        location = random.choice(self.zones[zone][category])
        # Increment the patron count for the chosen location
        self.location_metrics[zone][category] += 1
        return location,zone,category


    def optimize_location_assignments(self):
        for zone in self.zones:
            for category in ["attractions", "diner", "shopping"]:
                # Check if the category dictionary is empty
                if self.location_metrics[zone][category]:
                    least_busy_location = min(self.location_metrics[zone], key=self.location_metrics[zone].get)

                    for family in self.families:
                        if self.family_assignments[family] not in [least_busy_location] + self.get_adjacent_locations(least_busy_location, zone, category):
                            self.family_assignments[family] = least_busy_location
                            #print(self.location_metrics[zone])
                            #print(self.location_metrics[zone][category])
                            #print(self.location_metrics[zone][category])
                            self.location_metrics[zone][category] += 1


    def get_adjacent_locations(self, location, zone, category):
        # Provide logic to get adjacent locations based on the park layout
        # For simplicity, assume each location has two adjacent locations
        # You may need a more sophisticated approach based on the actual layout
        return [location + "_adj1", location + "_adj2"]

    def simulate(self):
        self.assign_families_to_locations()

        # Additional step to optimize location assignments
        #self.optimize_location_assignments()
            #optimize_locations_sets everone to the same location
        # Print family assignments
        #createa  dictionary of zones,attractions and subzones
        zone_counter={local_zone:{attraction:{} for attraction in self.zones[local_zone]} for local_zone in self.zones.keys()}#mainzones
        for local_zone in zone_counter:
            for name in self.zones[local_zone]:
                for place in range (0,len(self.zones[local_zone][name])):
                    zone_counter[local_zone][name][self.zones[local_zone][name][place]]=0

            #for attraction in 
        #print(zone_counter)
        #print({attraction:{} for attraction in self.zones['Fantasyland']})#attractions
        #print({subzone:{} for subzone in self.zones['Fantasyland']['shopping']})#subzone
        #print({attraction:{} for attraction in self.zones['Fantasyland']})#attractions
    

        print("Family Assignments:")
        movement_dataframe={'Family#':[],
                            'Familiy Name':[],
                            'Familiy Size':[],
                            'Bias':[],
                            'SubZone':[],
                            'Zone':[],
                            'Location':[],
                            }

        for family, location in self.family_assignments.items():
                familiy_name=self.patrons[self.families[family]['Family']['Parents'][0]]['Last_Name']
#                print(f" Family {family}: {familiy_name} assigned to {location[0]} (Bias: {self.family_biases[family]})")
#                    print out a verbose line about the actions of the familiy
                movement_dataframe['Family#'].append(family)
                movement_dataframe['Familiy Name'].append(familiy_name)
                parents,children=len(self.families[family]['Family']['Parents']),0
                if 'Children' in self.families[family]['Family']:
                    children=len(self.families[family]['Family']['Children'])
                movement_dataframe['Familiy Size'].append(parents+children)
                                                                          #                              sum(num for num in numbers if num % 2 == 0)
                movement_dataframe['Bias'].append(self.family_biases[family])
                movement_dataframe['Zone'].append([location[1],2])
                movement_dataframe['SubZone'].append(location[2])
                movement_dataframe['Location'].append(location[0])
                zone_counter[location[1]][location[2]][location[0]]+=1
        
#        show a dataframe of families and thier locations
        print(pd.DataFrame(movement_dataframe),'\n')
#        show the patron count by zone,subzone, and attraction
        for zone in zone_counter:
            print(zone,zone_counter[zone],'\n')

#        show the ratio of patrons that are at the locatino they are biased towards
        matchh=0
        mismatch=0
        for num in range(0,len(movement_dataframe['Bias'])):
            if movement_dataframe['Bias'][num]==movement_dataframe['SubZone'][num]:
                matchh+=1
            else:
                mismatch+=1
        print('match:',matchh)
        print('mismatch:',mismatch)
        print('match ratio:',round(100*(matchh/(matchh+mismatch)),2),'%')
    # Example Usage   


class Disney_Land_Visual: 
    def __init__(self):
        pass

    def GUI(self):
        def say_hello():
            response_label.config(text="Hello!")

        def shuffle_families():
            Themepark_data,Themepark_library=Disney_Land().patrons(guest_today=200)
            Disney_Land().family()
            del Themepark_library
            self.filehandling=File_Handler()
            self.filehandling.save_file(Themepark_data)
            response_label.config(text=Disney_Land().family())

        def show_families():
            response_label.config(text=Analysis().show_family())

        def show_age_groups():
            response_label.config(text=Analysis().age_groups())

        def show_child_count():
            response_label.config(text=Analysis().child_count())
            
        # Create the main window
        root = tk.Tk()
        root.title("Disney Land Visualizer")
        
        # Add an input box
        input_entry = tk.Entry(root)
        input_entry.grid(row=1, column=0, sticky="w")
        
        # Add a label
        label = tk.Label(root, text="Welcome to Disney Land Visualizer!")
        label.grid(row=0, columnspan=2)

        # Add buttons
        #button_01 = tk.Button(root, text="Say Hello", command=say_hello)
        #button_01.grid(row=1, column=0, sticky="ew")

        button_02 = tk.Button(root, text="Shuffle Families", command=shuffle_families)
        button_02.grid(row=2, column=0, sticky="ew")

        button_03 = tk.Button(root, text="Show Families", command=show_families)
        button_03.grid(row=3, column=0, sticky="ew")
        
        button_04 = tk.Button(root, text="Show Age Groups", command=show_age_groups)
        button_04.grid(row=3, column=1, sticky="ew")
        
        button_05 = tk.Button(root, text="Show Child Count", command=show_child_count)
        button_05.grid(row=3,column=2, sticky="ew")
        #button_05.place(x=50, y=150)
        
        

        # Add a label to display the response
        response_label = tk.Label(root, text="")
        response_label.grid(row=4, columnspan=2)

        # Run the event loop
        root.mainloop()

# Assuming Disney_Land and Analysis classes are defined elsewhere
# You might need to import them here.


import Disney_Land_Data as Disney_Land_Data
if 0: #create a new data set on command
    crayon(['#'*20,'Disney Land Ini','#'*20])
    #disney_land=Disney_Land()
    Themepark_data,Themepark_library=Disney_Land().patrons(guest_today=100)
    #Disney_Land().family()
    #Disney_Land().family()
    #Themepark_data will use our class we created to create our simulated themepark

#atractions=Attractions()
#atractions.get_attractions()



if 0: #file handling 
    crayon(['#'*20,'File Handler','#'*20])
    filehandling=File_Handler()
    #filehandling.save_file(Themepark_data)
    filehandling.load_file()
    #Themepark_library=filehandling.load_file()
    # for readability we'll use a pandas data frame

if 0:#analysis
    crayon(['#'*20,'Analysis','#'*20])
    import Disney_Land_Data as Disney_Land_Data
    analyze=Analysis()
    #sort by key (Fname, Lname, phone, DoB, Age Cat, State)
    #print(analyze.age_groups())
    #print(analyze.child_count())
    #analyze.show_family(2)

    analyze.orphans()

#print('//  '*40)
#print(pd.DataFrame(Themepark_data).tail(60))
##################################
if 1:#simulation
    crayon(['#'*20,'Simulation','#'*20])
    families=Disney_Land_Data.household_library
    patrons=Disney_Land_Data.database
    disneyland_sim = DisneylandSimulation( families,patrons)
    disneyland_sim.simulate()

if 0:#GUI
    crayon(['#'*20,'GUI','#'*20])
>>>>>>> d5044abfad8f836a7d2f8b942446d6797e08c3b5:Database_DisneyLand/Digital_Disney.py
    Disney_Land_Visual().GUI()
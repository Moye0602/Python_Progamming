import csv,json
import sys,subprocess
from Admin import*
from icecream import *
from pprint import *
showDetails=0
showSave=1
while 1:
    print('loading dependencies')
    try:
        import requests
        from bs4 import BeautifulSoup
        import pandas as pd
        subprocess.call(["cmd", "/c", 'cls'])
        break
    except ModuleNotFoundError as errorname:
        module=str(errorname)
        if 'import' not in module:
            install='pip install '+str(module).split(" '")[1][:-1]
        else:
            print('something else is needed')
        print('executing',install)
        subprocess.call(["cmd", "/c", install])
        subprocess.call([sys.executable] + sys.argv)
        sys.exit()

# Extract and print the URLs
fileName='LinkedIn'
page=25
#origin_source=  'https://www.linkedin.com/jobs/cyber-security-jobs'
    # this link does work but only allows parsing through a small portion of careers
origin_source='https://www.linkedin.com/jobs/search/?currentJobId=3435698262&keywords=cyber%20security&start='
    # this allows continious parsing of careers in incriments of 25 per main request



def page_request(url):
    """ takes the first page from a redfin url and cycles through each home based on search criteria and returns a dictionary of information for each"""
    # Send a GET request to the website
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    elements= soup.find_all("a",class_="base-card__full-link")
    #print(soup.find_all())
    jobs={}
    num=0
    for i in elements:
        num+=1
        jobs[num]={'Link':i.get('href')}
    return jobs

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

base_dict={ 'Role':None,'Link':None,'Salary':None,'datePosted':None,
                'postExperiation':None,'educationReqs':None,
                'experienceReqs':None,'skillReqs':None,'employemenType':None,           
                'Industry':None,'Location':None}    
# base_dict is a template of information for each job
details={
            'Role':'title',
            'Link':'link',
            'Salary':'baseSalary',
            'datePosted':'datePosted',
            'postExperiation':'validThrough',
            'educationReqs':'educationRequirements',
            'experienceReqs':'experienceRequirements',
            'skillReqs':'skills',
            'employemenType':'employmentType',
            'Industry':'industry',
            'Location':'jobLocation'
            }
#details is a local dictionary used for trasnlating the information collected from LinkedIn to our dictionary


#the first is creates a blank excel csv file with field names based on the keys from the dictionary "details"
with open('LinkedIn.csv','w') as iWannaWorkcsv:
        csv_writer = csv.DictWriter(iWannaWorkcsv, fieldnames = list(details.keys()) )
        csv_writer.writeheader()
        crayon('New blank csv file created','green')
#the second is creating a blank python file that will be appended to 
# we can put anything here that is python readable
with open('LinkedIn_jobs.py','w') as iWannaWork:
    crayon('New blank python file created','green')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

try:
    page,pageMax=25,8
    id=0
    job={}
    for i in range(1,pageMax):
        #for pages one to the value of pageMax, do the following instructions
        print('\n','Page:',i,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        jobs = page_request(origin_source+str(page*i))
        #request all html data from the link found
        if showDetails:
            ic(jobs)
        for num in jobs:
            #for all jobs found in our request, search the HTML content using BeautifulSoup
            soup = BeautifulSoup(requests.get(jobs[num]['Link']).content, "html.parser")
            try:
                elements= soup.find_all('script', type='application/ld+json')
                #find anything matching the tag"script" and data type "'application/ld+json'"
                if len(elements)>0:
                    #if we find a list of things then we keep going
                    if showDetails:
                        print(elements)
                    # what we do find, needs to be converted to something useful for both python and us to read
                    elements=elements[0].text
                        #text conversion
                    elements.split('":')
                        #split at the ' ": '
                    elements=json.loads(elements)
                    #json used to convert the string output to a dictionary

                    job[id]=base_dict 
                        #copy over our blank state dictionary
                    for name in details:
                        #for each name inour dictionary translation "details", do the following
                        category=details[name]
                            # not neeeded but I create local variables to reduce typing
                        if category in elements:
                            #check wht the category is and that it's in elements, sometimes there are blanks
                            if category=='jobLocation':
                                job[id][name]={'State':elements['jobLocation']['address']['addressRegion'],'City':elements['jobLocation']['address']['addressLocality']}
                            elif category=='baseSalary':
                                job[id][name]={'max':elements['baseSalary']['value']['maxValue'],'min': elements['baseSalary']['value']['minValue']}
                            elif category=='educationRequirements' :
                                job[id][name]=elements['educationRequirements']['credentialCategory']
                            elif category=='experienceRequirements':
                                job[id][name]=elements['experienceRequirements']['monthsOfExperience']    
                            else:
                                job[id][name]=elements[category]
                            if showDetails:
                                ic(category)
                        if category=='link':
                            job[id][name]=jobs[num]['Link']
                            # this last category is an exception because it was created outside
                            #  of the information we called, but we still need the link of the job
                    if showDetails:
                        crayon([id,job[id]['Role']])
                        pprint(job[id])
                        print('\n')
            except Exception as error:
                #errors can still occur and we want to know what they are so
                pprint(elements)
                    ##pprint to show our request gave
                print('<<<>>>')
                ic(elements)
                    #ic to idenitfy a bit easier
                crayon(error,'red')
                    #error code of what actually happened
                timeout(10)
                    #time to jump in OR ignore and let the program continue
            if id in job:
                #now that we got the info, we can store it in a csv file with the following
                with open('LinkedIn.csv','a') as iWannaWorkcsv:
                    if showDetails:
                        ic(list(details.keys()))    
                    csv_writer = csv.DictWriter(iWannaWorkcsv, fieldnames = list(details.keys()) )
                    
                    
                    csv_writer.writerow(job[id])
            blank()
            print('ID',id, 'of',pageMax*25,'stored')
            num+=1
            id+=1
            
            #iteration to the next id number and job from the request of 25 made earlier
            
        # writing the python file is a different in that we are not writing in one line at a time like csv 
        #instead, after every 25 jobs or page completion, we update the file with the changes and a timestamp
        with open('LinkedIn_jobs.py','w') as iWannaWork:
            iWannaWork.write('Jobs='+str(job)+'\n'+'timeStamp="'+str(datetime.now())+'"')
        if showSave:
            ic(iWannaWork)
            print()
            ic(iWannaWorkcsv)
except KeyboardInterrupt:
    restart_file()
except Exception as error:
    crayon(error,'red')
    restart_file()
restart_file()
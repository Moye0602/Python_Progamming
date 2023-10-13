import csv,json
import sys,subprocess
from Admin import*
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
#origin_source='https://www.linkedin.com/jobs/search/?currentJobId=3446845024&distance=25.0&geoId=103644278&keywords=cyber%20security&origin=HISTORY'

#origin_source='https://www.linkedin.com/jobs/view/cyber-security-analyst-at-experfy-3646115215?refId=jqecaA576yTWX0d5TKepkQ%3D%3D&trackingId=fqzb%2B26mnHInp%2BgcBQbb%2Fg%3D%3D&position=25&pageNum=0&trk=public_jobs_jserp-result_search-card'
#origin_source='https://www.linkedin.com/jobs/search/?currentJobId=3736023585&keywords=cybersecurity&origin=BLENDED_SEARCH_RESULT_CARD_NAVIGATION'
fileName='LinkedIn'
origin_source=  'https://www.linkedin.com/jobs/cyber-security-jobs'

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
try:
    job={}
    jobs = page_request(origin_source)
    #print(jobs)
    for num in jobs:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(requests.get(jobs[num]['Link']).content, "html.parser")
        #print(soup.find_all())
        elements= soup.find_all('script', type='application/ld+json')[0].text
        num=1
#        temp=dict()
        elements.split('":')
        elements=json.loads(elements)
        
            #json used to convert the string output to a dictionary
        #pprint(elements)
        job[num]={ 'Role':elements['title'],
                    'Link':jobs[num]['Link'],
                    'Salary':{'max': elements['baseSalary']['value']['maxValue'],'min': elements['baseSalary']['value']['minValue']},
                   'datePosted':elements['datePosted'],
                   'postExperiation':elements['validThrough'],
                    'educationReqs':elements['educationRequirements']['credentialCategory'],
                    'experienceReqs':elements['experienceRequirements']['monthsOfExperience'],
                    'skillReqs':elements['skills'],
                    'employemenType':elements['employmentType'],
                    
                    'Industry':elements['industry'],
                    'Location':{'State':elements['jobLocation']['address']['addressRegion'],'City':elements['jobLocation']['address']['addressLocality']},
        }
        #print(job)
        #timeout(1000)
#except ConnectionAbortedError:#
except Exception as error:
    crayon(error,'red')
    timeout(9000)
    restart_file()
finally: 
    restart_file()
restart_file()
page=0
reqs=0
id=0
prev_link=None
with open(fileName+'.csv', 'w') as Redfin:
    csv_writer = csv.DictWriter(Redfin, fieldnames = jobs.keys() )
    csv_writer.writeheader()

checks=2000
if 0:
    while checks>0:
        print('\n','Page:',page,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        try:
    #list of all homes by page number
            response = requests.get(source)
            soup = BeautifulSoup(response.content, "html.parser")
            link_elements = soup.find_all('a')
            for link in link_elements:
    #link to the individual page        
                link_url = link.get('href')
                if prev_link!=link_url and link_url and '/home/' in link_url:  # Check if the link has an href attribute
                    id+=1
                    print(id,link_url)
                    url=link_url
                    home=page_request(url)
                    allHomes[home['Address']]=home

                    #allHomes[id]=home #alternate that uses the id number rather than home address
                    #print(allHomes) 
                    print('>'*4,home['Address'],home)
                    print('///')
                    prev_link=link_url
                    with open('Redfin_VA.csv','a') as Redfin:
                        csv_writer = csv.DictWriter(Redfin, fieldnames = fieldnames )
                        try:
                            price=int(home['HomeFacts']['List Price'].replace("$", "").replace(",", ""))
                        except:
                            print(home['HomeFacts'])
                            user=input('push a key to continue')
                        sqft=0
                        try:
                            sqft=int(home['Sq Ft'].replace(",", ""))
                        except:
                            pass
                        store['id']=id
                        store['Property Type']=home['HomeFacts']['Property Type']
                        store['Address']=home['Address']
                        store['City']=home['City']
                        store['State']=home['State']
                        store['Zip Code']=home['Zip Code']
                        store['Price']=price
                        store['Beds']=home['Beds']
                        store['Baths']=home['Baths']
                        store['Sq Ft']=sqft
                        try:
                            store['Location']=home['HomeFacts']['Community']
                        except KeyError:
                            store['Location']=None
                        try:                    
                            store['Lot Size']=int(home['HomeFacts']['Lot Size'].replace(",", "").replace(" Sq. Ft.", ""))
                        except ValueError:
                            store['Lot Size']=home['HomeFacts']['Lot Size']
                        except:
                            store['Lot Size']=0
                        store['Year Built']=home['HomeFacts']['Year Built']
                        if 'hour' in home['HomeFacts']['Time on Redfin']:
                            store['Days on Market']=0
                        else:
                            store['Days on Market']=home['HomeFacts']['Time on Redfin'].replace('days',"")
                        store['$/Square Feet']=round(price/sqft,2)
                        try:
                            store['HOA / Month']=home['HomeFacts']['HOA Dues'].replace('$',"").replace('/month','')
                        except:
                            store['HOA / Month']=0
                        store['URL']=url
                        #parsedHomes[store['Address']]=store
                        
                        print(store)
                        print()
                        csv_writer.writerow(store)
                    checks=2000
                else:
                    checks-=1
                    print('checks remaining:',checks,end='\r')

            page+=1
            source=origin_source+'/page-'+str(page)
            
                        
                
            
        except KeyboardInterrupt:# to be changed upon hitting an error
            print('User stopped process')
            break
        print('checks remaining:',checks)
if 0:
    parsedHomes={}
    for title in allHomes[list(allHomes.keys())[0]]:
        if title!='HomeFacts':
            try:
                parsedHomes[title]=[allHomes[address][title] for address in allHomes]
            except:
                parsedHomes[title]=[address for address in allHomes]
    for address in allHomes:
        title='HomeFacts'
        for subtitle in allHomes[address][title]:
            parsedHomes[subtitle]=[allHomes[address][title][subtitle] if subtitle in allHomes[address][title] else 0  for address in allHomes ]
        
            
    dataframe=pd.DataFrame(parsedHomes)
    print(dataframe)
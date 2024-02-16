import csv
import sys,subprocess
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
origin_source='https://www.redfin.com/city/10201/NV/Las-Vegas/filter/property-type=house+multifamily,min-price=300k,max-price=350k,min-beds=2,min-baths=1.5,status=active,viewport=36.30994:35.89273:-114.82616:-115.61786'

def page_request(url):
    """ takes the first page from a redfin url and cycles through each home based on search criteria and returns a dictionary of information for each"""
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup

    soup = BeautifulSoup(response.content, "html.parser")
    elements= soup.find_all("div",class_="statsValue")#[0].get_text(),
    tablelab=(soup.find_all("span",class_="table-label"))
    tableval=(soup.find_all("div",class_="table-value"))
    # Find all article titles using the appropriate HTML tags and classes
    fullAddress=soup.find_all("h1", class_="full-address")[0].get_text().split(',')
    Home={
    'Address': fullAddress[0],
    'City': fullAddress[1],
    'State': fullAddress[2][1:].split(' ')[0],
    'Zip Code':fullAddress[2][1:].split(' ')[1],
    'Price':elements[0].get_text(),
    'Beds':elements[1].get_text(),
    'Baths':elements[2].get_text(),
    'Sq Ft':soup.find_all("div",class_="stat-block sqft-section")[0].get_text().split('Sq Ft')[0]
    #'next':soup.find_all("div",class_="statsValue")[0][1]
    }    
    Homefacts={}
    for sub in range(len(tablelab)):
        Homefacts[tablelab[sub].get_text()]=tableval[sub].get_text()
    #print(Homefacts)
    Home['HomeFacts']=Homefacts
    #for item in homefacts:
    #    Home['HomeFacts'][item]=None
        #Home['HomeFacts'][span[sub].get_text()]=0
    #Time on Redfin <span class="bp-DefinitionFlyout bp-DefinitionFlyout__underline" tabindex="0" role="link">Time on Redfin</span>
    
    #<div class="stat-block sqft-section" data-rf-test-id="abp-sqFt"><span class="statsValue">1,406</span><div class="statsLabel">Sq Ft</div></div>
    
    
    return Home

source=origin_source
page=0
reqs=0
id=0
prev_link=None
allHomes={}
fieldnames=   [ 'id',
        'Address',
        'City',
        'State',
        'Zip Code',
        'Price',
        'Beds',
        'Baths',
        'Sq Ft',
    ]

x_range=0


#csv_writer = csv.DictWriter('Redfin.csv','a', fieldnames = fieldnames)


with open('Redfin.csv', 'w') as Redfin:
    csv_writer = csv.DictWriter(Redfin, fieldnames = fieldnames )
    csv_writer.writeheader()
store={}
while 1:
    print('Page:',page,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    try:
        response = requests.get(source)
        soup = BeautifulSoup(response.content, "html.parser")
        link_elements = soup.find_all('a')
        
        for link in link_elements:
                
            link_url = link.get('href')
            
            if prev_link!=link_url and link_url and '/home/' in link_url:  # Check if the link has an href attribute
                id+=1
                
                print(id,link_url)
                url='https://www.redfin.com'+link_url
                home=page_request(url)
                allHomes[home['Address']]=home
                #allHomes[id]=home #alternate that uses the id number rather than home address
# prints the dictionary of homes
                #print(allHomes) 

                print(home['Address'],home)
                print()
                prev_link=link_url
                with open('Redfin.csv','a') as Redfin:
                    csv_writer = csv.DictWriter(Redfin, fieldnames = fieldnames )
                        #info[dayNum]=profit_dict['$ sum gain'][datesM.index(dayNum)]
                        #except IndexError:
                        #    info[dayNum]=0
                        #    pass
                        #IndexError: list index out of range on new day/ restart program
                    #info["x_value"] = x_value
                    store['id']=id
                    store['Address']=home['Address']
                    store['City']=home['City']
                    store['State']=home['State']
                    store['Zip Code']=home['Zip Code']
                    store['Price']=int(home['Price'].replace("$", "").replace(",", ""))
                    store['Beds']=home['Beds']
                    store['Baths']=home['Baths']
                    store['Sq Ft']=int(home['Sq Ft'].replace(",", ""))
                    print('>>>>>')
                    print(store)
                    csv_writer.writerow(store)
        page+=1
        source=origin_source+'/page-'+str(page)

                    
            
        
    except KeyboardInterrupt:# to be changed upon hitting an error
        print('User stopped process')
        break
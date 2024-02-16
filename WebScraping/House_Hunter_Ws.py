import csv
import sys,subprocess
from icecream import ic
from pprint import *
from Admin import *

### this is a stand alone script with only normal imports
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
#origin_source='https://www.redfin.com/city/12839/DC/Washington-DC/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted'
#area='_DC_Area2'
origin_source='https://www.redfin.com/city/16657/TX/San-Antonio/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted'
area='TX_San_Antonio'
#origin_source='https://www.redfin.com/city/3104/AZ/Chandler/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted'
#area='AZ_Chandler'
#origin_source='https://www.redfin.com/city/23010/VA/Fort-Belvoir/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted,viewport=39.50773:38.47884:-76.11495:-77.9634'
#area='DC_Area'
#origin_source='https://www.redfin.com/city/14153/FL/Panama-City/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted'
#area='FL_Pensacola'
#origin_source='https://www.redfin.com/city/4249/CA/Corona/filter/property-type=house,max-price=500k,min-beds=2,min-baths=1.5,exclude-age-restricted,viewport=34.44004:33.36408:-116.95788:-117.85327'
#area='CA_Corona'
#origin_source='https://www.redfin.com/city/16657/TX/San-Antonio/filter/property-type=house,min-price=125k,max-price=500k,min-beds=2,min-baths=1.5,min-parking=1,status=active,exclude-age-restricted,viewport=29.7348:29.17038:-98.09509:-98.94104,no-outline,financing-type=VA'
def page_request(url):
    """ takes the first page from a redfin url and cycles through each home based on search criteria and returns a dictionary of information for each"""
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
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
    
    
    return Home

source=origin_source
page=0
reqs=0
id=0
prev_link=None
allHomes={}

fieldnames=   [ 'id',
                'Property Type',
                'Address',
                'City',
                'State',
                'Zip Code',
                'Price',
                'Beds',
                'Baths',
                'Sq Ft',
                'Location',
                'Lot Size',
                'Year Built',
                'Days on Market',
                '$/Square Feet',
                'HOA / Month',
                'URL'
            ]

with open('Redfin'+area+'.csv', 'w') as Redfin:
    csv_writer = csv.DictWriter(Redfin, fieldnames = fieldnames )
    csv_writer.writeheader()
store={}
checks=2000
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
            crayon(link_url)
            if prev_link!=link_url and link_url and '/home/' in link_url:  # Check if the link has an href attribute
                id+=1
                print(id,link_url)#keep
                url='https://www.redfin.com'+link_url
                home=page_request(url)
                allHomes[home['Address']]=home

                #allHomes[id]=home #alternate that uses the id number rather than home address
                #print(allHomes) 
                print('>'*4,home['Address'],home)#keep
                print('///')
                prev_link=link_url
                with open('Redfin'+area+'.csv','a') as Redfin:
                    
                    #try:
                    
                    if 'List Price' in home['HomeFacts']:
                        price=int(home['HomeFacts']['List Price'].replace("$", "").replace(",", ""))
                    #except Exception as error:
                    #    ic(error)
                    #    print(home['HomeFacts'])
                    #    user=input('push a key to continue')
                        sqft=0
                        try:
                            sqft=int(home['Sq Ft'].replace(",", ""))
                        except:
                            pass
                        
                        try:
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
                            #ic(store)
                            csv_writer = csv.DictWriter(Redfin, fieldnames = fieldnames )
                            csv_writer.writerow(store)
                        except Exception as error: 
                            ic(error)
                            pprint(home['HomeFacts'])
                            pass
                checks=2000
            else:
                checks-=1
                print('checks remaining:',checks,end='\r')

        page+=1
        source=origin_source+'/page-'+str(page)
        
                    
            
        
    except KeyboardInterrupt:# to be changed upon hitting an error
        print('<'*5,'User stopped process','>'*5)
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

'''
Austin, Texas: Known for its tech boom, job growth, and a young population, Austin has a high demand for rentals.

Raleigh-Durham, North Carolina: The Research Triangle Park area is a hub for technology and research companies, attracting renters.

Orlando, Florida: With its tourism industry and a growing population, Orlando offers opportunities for vacation and long-term rentals.

Nashville, Tennessee: Nashville's vibrant music scene and job market make it appealing for renters.

Phoenix, Arizona: A thriving economy and population growth have increased the demand for rental properties in Phoenix.

Atlanta, Georgia: Atlanta's diverse economy and cultural attractions attract renters.

Denver, Colorado: A strong job market and quality of life make Denver a rental market to consider.

Seattle, Washington: The tech industry's presence in Seattle drives rental demand.

Tampa, Florida: Tampa's affordable housing market and growing job opportunities make it attractive for renters.

Boise, Idaho: Boise's population growth and quality of life have led to increased demand for rental properties.


##
Identifying Areas with High ROI:

Market Research: Study market reports, vacancy rates, and job growth data for different cities and neighborhoods.

Rental Yield Analysis: Calculate rental yields by dividing the annual rental income by the property's purchase price. Look for areas with higher yields.

Property Appreciation: Research historical property value trends and consider areas with expected appreciation.

Local Economy: Assess the strength of the local job market and industries.

Population Growth: Areas with growing populations often have higher rental demand.

Property Management: Consider the cost and logistics of property management, as this can affect ROI.

Regarding your condo in San Diego, the decision to sell or rent depends on your financial goals and circumstances. Here are some factors to consider:

Calculate the potential rental income and compare it to your monthly costs, including the mortgage, property taxes, insurance, and HOA fees.
Evaluate your long-term investment goals. Are you looking for ongoing rental income, or do you prefer to cash out with a sale?
Consider your willingness and ability to manage the property, including tenant screening, maintenance, and repairs.
Research the current real estate market in San Diego to understand property values and rental demand.
If renting the condo generates positive cash flow and aligns with your investment objectives, it may make sense to keep it as a rental property. However, if you need the funds for other investments or if the condo doesn't offer a favorable return, selling it could be a better option. Consulting with a real estate professional can provide valuable insights tailored to your specific situation.





'''
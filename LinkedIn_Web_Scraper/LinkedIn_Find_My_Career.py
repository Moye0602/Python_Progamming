from LinkedIn_jobs import Jobs
from Admin import*
from icecream import*
from pprint import*
from datetime import datetime,timedelta
degree='bachelor'
myLocation={'State':'CA','City':'San Diego'}
currentDate,dayrange=datetime.today(),30
payWanted,range=90000,.15#done
employmentType=['full_time','intern','remote']# done
testmodeOFF,delay=1,.0

print('\n','>>>>Total Jobs Found:',len(Jobs),'<<<<','\n')
whatCanIdo={'roles':[],'locations':[],'pay':[],'employment type':[]}

for id in Jobs:
    career=Jobs[id]
    whatCanIdo['roles'].append(career['Role'])
    if career['Location']['State']:
        whatCanIdo['locations'].append(career['Location']['State'])
    if career['Salary']!=None:
        print(career['Salary'])
        whatCanIdo['pay'].append((career['Salary']['max']+career['Salary']['min'])/2)
    whatCanIdo['employment type'].append(career['employemenType'])

print(whatCanIdo)
metrics={name:{} for name in list(whatCanIdo.keys())}
for name in metrics:
    print(name)
    if name=='employment type' or name=='locations' :
        crayon(name)
        print()
        
        for subname in whatCanIdo[name]:
            print(name,subname)
            try:
                metrics[name][subname]+=1
            except:
                metrics[name][subname]=1
            print(metrics)

print(metrics)
timeout(30)
try:
    for id in Jobs:
        eduMatch,payMatch,employmentMatch=0,0,0
        dateMatch=0
        career=Jobs[id]
        #print(id,career,'\n')
        for role in employmentType:
            if testmodeOFF and  role in career['Role'].lower():
                crayon(['Employment Type Match:',role],'green')
                eduMatch=1
                #timeout(delay)
        if testmodeOFF and career['Salary']!=None  and career['Salary']['min']>payWanted*(1-range):
            crayon(['Salary Match:',career['Salary']],'green')
            payMatch=1
            #timeout(delay)
        #print((datetime.fromisoformat(Jobs[id]['datePosted'][:10])-(datetime.today()-timedelta(days=dayrange))).days)
        #print(datetime.fromisoformat(Jobs[id]['datePosted'][:10]),(datetime.today()))
        if any([eduMatch, payMatch]) and  (datetime.fromisoformat(Jobs[id]['datePosted'][:10])-(datetime.today()-timedelta(days=dayrange))).days>0:
            crayon(['DateRange Match:',datetime.fromisoformat(Jobs[id]['datePosted'][:10])-(datetime.today())],'green')
            crayon(['>>Post is within',dayrange],'green')
            dateMatch=1
        if eduMatch and payMatch:# and dayrange:
            crayon(['Apply for:',career['Role'],'#',id],'green')
            crayon(career,'cyan')
            timeout(delay*5)
        elif any([eduMatch, payMatch]):#,dayrange
            crayon(['Apply for:',career['Role'],'#',id],'magenta')
            #crayon(career,'magenta')
            pprint(career)
            timeout(delay*5)
        
        if any([eduMatch, payMatch]):
            print()
except KeyboardInterrupt:
    blank()
    crayon('User Interuption')
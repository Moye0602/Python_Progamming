'''import trasncript as a word doc
parse line for line and identify the following categories
1.program
2. sessions/semesters
    for each semester identify
        course (classifier and number)
        description
        points ( 3 points=1 credit hour)
        grade (derived from points)\
        for GPA
        Term GPA
        Cumulative GPA


 the class name,class number, credits, gpa, grade assigned
'''
from collections import defaultdict
from LinkedIn_jobs import *
roleCounter={}
roles=[]
#roles=[Jobs[id]['Role'] for id in range(0,len(Jobs))]
for id in range(0,len(Jobs)):
    print(Jobs[id]['Role'])
    print()
    #roles.append(Jobs[id])
print(roles)
#roleCounter=defaultdict(0)
for id in Jobs:
    roleCounter[Jobs[id]['Role']]+=1
    print(roleCounter)

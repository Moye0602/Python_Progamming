import Course_Keywords as keywords
from my_transcript_inPy import my_transcript
import pandas as pd
from collections import defaultdict

def transcript_focus_area():
    import Course_Keywords as keywords
    from my_transcript_inPy import my_transcript
    focus_area=defaultdict(int)
    for mycourse in my_transcript['Courses']:
        for program in keywords.Courses:
            for course in keywords.Courses[program]:
                    if mycourse ==course:
                        print(course.split(' ')[0])
                        focus_area[course.split(' ')[0]]+=my_transcript['Courses'][mycourse]['Profficiency']
    print(focus_area)
#transcript_focus_area()

def my_transcript_df():
    import Course_Keywords as keywords
    from my_transcript_inPy import my_transcript
    out={'Course':[],
        'Profficiency':[],
        'Skills':[]
        
    }
    for mycourse in my_transcript['Courses']:
            for program in keywords.Courses:
                for course in keywords.Courses[program]:
                    if mycourse ==course:
                        out ['Course'].append(mycourse)
                        out['Profficiency'].append(my_transcript['Courses'][mycourse]['Profficiency'])
                        out['Skills'].append(keywords.Courses[program][mycourse])
                        if 1: #show course id , skill level and keywords
                            print(mycourse,
                                '\nProfficiency: ',my_transcript['Courses'][mycourse]['Profficiency'],'|'
                                ,mycourse,keywords.Courses[program][mycourse])
            #print(mycourse)#show course id and number
    pd.set_option('display.max_colwidth', 100)

    #print(pd.DataFrame(out))
    #print(pd.DataFrame(out).sort_values(by='Course', ascending=True))
my_transcript_df()
#for course in my_transcript['Courses']:
#    for info in my_transcript['Courses'][course]:
#        print(course,info,my_transcript['Courses'][course][info],'\n')
#    print('-'*10)
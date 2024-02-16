import fitz,time
from icecream import ic
from pprint import *
from collections import defaultdict
import pandas as pd
from termcolor import colored
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
    
    print(' '*110,end='\r')
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

class Convert:
    def __int__(self):
        pass
    def extract_text_from_pdf(self,pdf_file):
        text = ""
        pdf = fitz.open(pdf_file)
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            #print
            text += page.get_text()
            #print(page)
            #print(text)
        #print(pdf.load_page(0))
        pdf.close()
        return text

    def transcript_to_py (self,pdf_source_file=None):
        path=('\\').join(__file__.split('\\')[:-1])+'\\'
        pdf_file=path+pdf_source_file
        extracted_text = self.extract_text_from_pdf(pdf_file)
        #print(extracted_text)
        with open('transcripttext.txt','w') as  savetext:
            savetext.write(extracted_text)
        stored_text= open('transcripttext.txt','r') 
        #print(stored_text.read())
        transcript={'Courses':{}}#defaultdict(dict)
        #print(transcript)
        text=stored_text.readlines()
        textout=''
        majors=[]
        for i in range(1,len(text)):
            if 'END OF TRANSCRIPT' in text[i][:-1]:
                break
            if ':' in text[i][:-1]:
                textout=text[i][:-1]+' '+text[i+1][:-1]
                if 'of' in textout :
                #collect the concentration(s)/major(s)
                    textout +=' '+text[i+2][:-1]
                    textout=textout.split(':  ')[1].replace('  ',' ')
                    majors.append(textout)
                    transcript['Majors']=set(majors)
#debugging   #ic(text[i][:-1])
                # identify what info is on the current line being read
            if 'Institution Info' in text[i]:#collect insitution information
                transcript['Institution Info']={text[line][:-1] for line in range(i+1,i+4)}
            #collect program info
            if 'Program:' in text[i]:
                transcript['Program']={text[i+1][:-1]} 
            if text[i][:-1].isdigit() :
                r=i+1
                a=r+1
                coursename=text[r][:-1]
                coursename+= ' '+str(text[r+1][:-1]) if text[r+1][:-1][0].isdigit()==False else ''
                #collect course name and normalize title
                coursecredit=text[i+2][:-1] if text[i+2][:-1][0].isdigit() else text[i+3][:-1]
                #collect course credit
    #debugging
    #            print('?',text[a][:-1].isalpha())
                while text[a][:-1].isalpha() :
                    a+=1
                    if '0' not in text[a][:-1] and text[a][:-1].isdecimal()==False and text[a][:-1].isdigit()==False :
                        coursename+=' '+text[a][:-1] 
#debugging
                #print('><',text[r:r+2])#[:-1])
                #print('coursename',coursename)
                skip=False
                while text[r][:-1].isdecimal()==False  and text[r][:2].isdigit()==False and skip==False:
                    r+=1
                    try:
                        if '.' in text[r][:2]:
    #debugging              print('@',text[r][:-1])
    #debugging              print(r,(text[r][:-1]),(text[r+1][:-1]))
                            break
                    except IndexError:
                        r-=1
                        skip=True
                        pass
    #debuging   ic()
    #debuging   ic(text[r][:-1],text[r+1][:-1], text[r+1][:-1].split('.')[0].isdecimal(),len(text[r+1][:-1]))
                if text[r][:-1].split('.')[0].isdecimal() and text[r+1][:-1].split('.')[0].isdecimal() and float(text[r][:-1])*float(text[r+1][:-1])!=0:# and text[r+3][:-1].isdecimal():
    #debuging       ic()
                    score=float(text[r][:-1])/float(text[r+1][:-1])
                    Profficiency=round(100*(float(text[r+3][:-1]))/12,2)
                    Profficiency=score*100 if Profficiency==0 else Profficiency
                else:
                    Profficiency=score=0
    #debugging
    #            pprint([text[i+2][:-1],
    #            text[r][:-1],
    #            text[a][:-1]])
                course_info={
                        'Course Name':coursename.replace('_',' ').replace('  ',' '),#need to rearrange this because it cuts off part of the course title  
                        'Credits':coursecredit,#text[i+2][:-1],
                        'Score':100*score,
                        'Profficiency':Profficiency,}
                        #'Course Description':None
                transcript['Courses'][text[i-1][:-1]+' '+text[i][:-1]]=course_info
    #debugging            
    #            ic()
        #initially courses are arranged by order taken
        transcript['Courses']=dict(sorted(transcript['Courses'].items()))
        #this line will sort by name and number
        for item in transcript:
            if 'Courses' in item:
                for classes in transcript['Courses']:
                    print(classes,transcript['Courses'][classes],'\n')
            else:
                print(item,transcript[item],'\n')

        with open(path+'my_transcript_inPy.py','w') as transcript_filehandler:
            transcript_filehandler.write('my_transcript='+str(transcript))
            print('Transcript saved\n','-'*100,'\n')


class Transcript_output:
    pd.set_option('display.max_colwidth', 100)
    
    def __init__(self):
        pass
        from my_transcript_inPy import my_transcript
        import Course_Keywords as keywords
        self.transcript=my_transcript
        self.keywords=keywords
    def my_transcript_df(self):
        crayon('-'*100)
        transcript_df={'Course':[],
            'Profficiency':[],
            'Skills':[]}
        for mycourse in self.transcript['Courses']:
                for program in self.keywords.Courses:
                    for course in self.keywords.Courses[program]:
                        if mycourse ==course:
                            transcript_df ['Course'].append(mycourse)
                            transcript_df['Profficiency'].append(self.transcript['Courses'][mycourse]['Profficiency'])
                            transcript_df['Skills'].append(self.keywords.Courses[program][mycourse])
                            if 0: #show course id , skill level and self.keywords
                                print(mycourse,':Profficiency: ',self.transcript['Courses'][mycourse]['Profficiency'],'|'
                                    ,mycourse,self.keywords.Courses[program][mycourse],'\n')
                #print(mycourse)#show course id and number
        crayon('my_transcript_df complete')
        return pd.DataFrame(transcript_df)
    def transcript_focus_area(self):
        crayon('-'*100)
        focus_area=defaultdict(int)
        for mycourse in self.transcript['Courses']:
            for program in self.keywords.Courses:
                for course in self.keywords.Courses[program]:
                        if mycourse ==course:
                            #print(course.split(' ')[0])
                            focus_area[course.split(' ')[0]]+=self.transcript['Courses'][mycourse]['Profficiency']
        crayon('transcript_focus_area complete')                
        return focus_area
#usmc="MOYE_KRISTOPHER_ComboTranscript.pdf"
#emu="EMU_Transcript.pdf"
pdf_source_file="CSU_SB_2024_Spring_Unofficial Transcripts.pdf"
#Convert().transcript_to_py(pdf_source_file)
#print(Transcript_output().my_transcript_df())
print(Transcript_output().transcript_focus_area())

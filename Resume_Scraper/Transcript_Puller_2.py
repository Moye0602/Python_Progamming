import fitz,time
from icecream import ic
from pprint import *
import numpy as np
def extract_text_from_pdf(pdf_file):
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

from collections import defaultdict
if __name__ == "__main__":
    #pdf_file = "C://Users//kmoye//OneDrive//Desktop//Python_Projects//Python_Lab//Projects//Resume_Scraper//CSU_SB_2023_Summer_Unofficial Transcripts.pdf"  # Replace with the path to your PDF file
    pdf_file = "C://Users//kmoye//OneDrive//Desktop//Python_Projects//Python_Lab//Projects//Resume_Scraper//"
    csu="CSU_SB_2024_Spring_Unofficial Transcripts.pdf"
    usmc="MOYE_KRISTOPHER_ComboTranscript.pdf"
    emu="EMU_Transcript.pdf"
    pdf_file+=csu
    extracted_text = extract_text_from_pdf(pdf_file)
    #print(extracted_text)
    with open('transcripttext.txt','w') as  savetext:
        savetext.write(extracted_text)
    stored_text= open('transcripttext.txt','r') 
    #print(stored_text.read())
    transcript={'Courses':{}}#defaultdict(dict)
    #print(transcript)
    text=stored_text.readlines()
    lastline=''
    textout=''
    major_count=1
    majors=[]
    
    for i in range(1,len(text)):
        #print(i)
        #print(text[i][:-1])
        if 'END OF TRANSCRIPT' in text[i][:-1]:
            break
        if ':' in text[i][:-1]:
        #if lastline!='' and lastline!=text[i][:-1]:
            textout=text[i][:-1]+' '+text[i+1][:-1]
            if 'Master of Business Administration' in textout:
                textout +=text[i+2][:-1]
            lastline=text[i+1][:-1]
            #i+=1
            #print(textout)
        
        #else:
#debugging #ic(text[i][:-1])
            # identify what info is on the current line being read
        if 'Institution Info' in text[i]:#collect insitution information
            transcript['Institution Info']={text[line][:-1] for line in range(i+1,i+4)}
            
        if 'Program:' in text[i]:#collect program info
            transcript['Program']={text[i+1][:-1]}
        
        if 'Master of' in text[i]:#collect major(s)
            majors.append(text[i][:-1]+' '+text[i+1][:-1])
            transcript['Majors']=set(majors)
        if text[i][:-1].isdigit() :
            r=i+1
            a=r+1
            coursenum=0
            coursename=text[r][:-1]
            coursename+= ' '+str(text[r+1][:-1]) if text[r+1][:-1][0].isdigit()==False else ''
            #collect course name and normalize title
            coursecredit=text[i+2][:-1] if text[i+2][:-1][0].isdigit() else text[i+3][:-1]
            #collect course credit
#debugging
#            print('?',text[a][:-1].isalpha())
            while text[a][:-1].isalpha() :
                a+=1
                if '0' not in text[a][:-1] and text[a][:-1].isdecimal()==False and text[a][:-1].isdigit()==False:
                    coursename+=' '+text[a][:-1]
            
#debugging
            #print('><',text[r:r+2])#[:-1])
            #print('coursename',coursename)
            skip=False
            while text[r][:-1].isdecimal()==False  and '6' not in text[r][:2] and skip==False:
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
                score=0#np.nan
                Profficiency=score
#debugging
#            pprint([text[i+2][:-1],
#            text[r][:-1],
#            text[a][:-1]])

            course_info={
                    'Course Name':coursename.replace('_',' ').replace('  ',' '),#need to rearrange this because it cuts off part of the course title  
                    'Credits':coursecredit,#text[i+2][:-1],
                    'Score':100*score,
                    'Profficiency':Profficiency,
                    'Course Description':None

                }
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
path=__file__.split('\\')
path=('\\').join(path[:-1])+'\\'
with open(path+'my_transcript_inPy.py','w') as transcript_filehandler:
    transcript_filehandler.write('my_transcript='+str(transcript))
    print('saved')
print('end')

print(transcript)
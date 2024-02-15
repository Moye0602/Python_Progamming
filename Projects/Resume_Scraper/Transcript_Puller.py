import fitz

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf = fitz.open(pdf_file)
    for page_num in range(pdf.page_count):
        page = pdf.load_page(page_num)
        print
        text += page.get_text()
        print(page)
        #print(text)
    print(pdf.load_page(0))
    pdf.close()
    return text

from collections import defaultdict
if __name__ == "__main__":
    pdf_file = "C://Users//kmoye//OneDrive//Desktop//Python_Projects//Python_Lab//Projects//Resume_Scraper//CSU_SB_2023_Summer_Unofficial Transcripts.pdf"  # Replace with the path to your PDF file
    extracted_text = extract_text_from_pdf(pdf_file)
    #print(extracted_text)
    with open('transcripttext.txt','w') as  savetext:
        savetext.write(extracted_text)
    stored_text= open('transcripttext.txt','r') 
    #print(stored_text.read())
    transcript=defaultdict(dict)
    #print(transcript)
    text=stored_text.readlines()
    lastline=''
    for i in range(1,100):
        #print(i)
        #print(text[i][:-1])
        
        if ':' in text[i][:-1]:
        #if lastline!='' and lastline!=text[i][:-1]:
            textout=text[i][:-1]+' '+text[i+1][:-1]
            lastline=text[i+1][:-1]
            i+=1
        elif lastline!=text[i][:-1]:
            if lastline!='':
                print('>',lastline)
            textout=text[i][:-1]
            print(textout)
            lastline=''
        if  textout in ['ADMN','MGMT']:
            counter=17
            
        #print(stored_text.readlines()[i])
    
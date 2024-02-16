import openai
import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import os
from Admin import *
from icecream import *
# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get

#ip = get('https://api.ipify.org').text
#print('My public IP address is: {}'.format(ip))
#from dotenv import load_dotenv
#load_dotenv()
#OPENAI_KEY=os.getenv('OPENAI_KEY')

openai.api_key=None# use your own API key from Chat GPT

assistant_name='Jarvis'


#print(assistant_name,'is online, lets take over the world')

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
r=sr.Recognizer()
def record_text():
    #while 1:
        #while loop will cause inifite loop of request to chatgpt if programmed wrong
        #run as a single request till response is correct
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)
                print('Listening...')
                #audio2=r.listen(source2)
                #MyText = r.recognize_google(audio2)
                MyText='tell me a joke'
                #print('did you say?',user_input)
                return MyText
        except sr.RequestError  as err:
            print("cound not request a result; {0}".format(err)) 
        except sr.UnknownValueError as err:
             print('Unknown error occured',err)
def send_to_chatGPT(messages,model="gpt-3.5-turbo"):
    #timeout(30)
    ic()
    response =openai.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=100,
            n=1,
            stop=None,#causes api to stop generating further tokens
            temperature=0.5 #range is 0-1
            #prompt=f'User:{user_input}\n{ assistant_name}',
            )
    ic()
    message=response.choices[0].text.strip()
    message.append(response.choices[0].message)
    ic()
    timeout(20)
    return message
messages=[{"role":"user","content":'please act like Jarvis from Iron Man'}]

text=record_text()
    #record audi informtation
messages.append({"role":"user","content":text})
    #used to keep track of the whole conversation by adding each new statement
    #GPT records infor mation as a pair of dictionaries, user and GPT
#timeout
response=send_to_chatGPT(messages)
#SpeakText(messages)
SpeakText(response)
print(response)

import time, helper

def main():
    print(__name__)
from icecream import ic # install

###
from pprint import pprint

###
import pyttsx3 # install
txt2speech=pyttsx3.init()
statement='hello world, I am a python program'
print(statement)
#txt2speech.say(statement)
#txt2speech.runAndWait()

import keyboard # install

### #For loop vs while loop using termcolor
import random
from termcolor import colored # install
color='blue'
print(colored('and now I am '+color,color))
helper.timeout(5)

######################
colors=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
        'light_grey', 'dark_grey', 'light_red', 'light_green', 'light_yellow', 'light_blue',
        'light_magenta', 'light_cyan']
for color in colors:
    print(colored('and now I am '+color,color))
helper.timeout(5)

######################
counter=10
while counter>0:
    color=colors[random.randrange(0,len(colors))]
    print(colored(str(counter)+' counters remaining and now I am '+color,color))
    time.sleep(1)
    counter-=1

######################
import schedule # install
import datetime
def hello():
    
    print("poof I'm here")
        #schedule.every().day.at("00:00").do(hello)
schedule.every().second.do(hello)
schedule.every().second.do(hello)
schedule.every().second.do(hello)
from datetime import datetime

while 1:
    print(datetime.now())
    schedule.run_pending()
    time.sleep(1)
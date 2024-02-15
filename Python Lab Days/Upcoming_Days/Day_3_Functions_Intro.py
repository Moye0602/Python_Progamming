import time
def my_function():
    print('do all the things')
    for i in range(11):
        print(i)
    attempts=10
    #time.sleep(1)

    time.sleep(10)
    
    while attempts >0:
        print('remaining attempts:',attempts)
        attempts-=1
        #time.sleep(1)
    print('done')
my_function()
#the while loop  we have the ability to either run indefinitely or until a condition is met
#lets make a countdown timer

##################

#################

def my_other_function(attempts=10):
    while attempts >0:
        print('remaining attempts:',attempts)
        attempts-=1
    print('done')
#################
my_other_function()
time.sleep(1)
my_other_function(attempts=100)
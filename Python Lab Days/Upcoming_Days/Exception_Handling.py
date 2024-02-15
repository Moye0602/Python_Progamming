print('start')
try:
    print('it works')
    
    print(box[1])

except NameError:
    print('something was not given a name')

except ConnectionError:
    print('something broke')


print('done')
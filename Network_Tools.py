from Admin import *
options={
    'network divsions':1,
    'IP address class':'D',
    'host req':2,



}


for option in options:
    options[option]=input('new value for',option,':')
print(options)
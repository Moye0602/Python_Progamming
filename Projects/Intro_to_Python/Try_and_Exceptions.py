from icecream import *
from datetime import datetime
from Admin import restart_file
lines=1
vals=1
while True == 1:
    print('running',datetime.now(),end='\033[F'*(lines))
    try:
        #print(vals)
        
#my work space of errors        
        mylist=[1,2,3,4]
        mylist[7]
        mylist=[i for i in range(0,len(mylist)+100)]
        #import something_i_dont_have
        #from Admin import something_i_dont_have
        mydictionary={'stuff':'not here'}
        #mydictionary['does not exist']
        val1,val2=42,'fourtytwo'
        #val1+val2
        #val1+mydictionary
        #val1+mylist
        vals+=1
        #vals=vals**vals
        num1,num2=int(3),float(10.5)
        num1/num2
    except ModuleNotFoundError as err:#(ImportError): ...
        ic()
        print(err)
        print('Error name: ModuleNotFoundError')
        lines=4
    except ImportError as err:
        ic()
        print(err)
        print('Error name: ImportError')
        from Admin import crayon
        crayon('success')
        lines=5
    except KeyError as err:
        ic()
        print(err)
        print(mydictionary['stuff'])
        lines=4
    #except TypeError as err:
    #    ic()
    #    print(err)
    #    print('Error name: TypeError')
        lines=4
    except SyntaxError as err:# something is not formatted correctly
        ic()
        print(err)
        print('Error name: SyntaxError')
        lines=4
#except Exception as err:
    #except SystemError as err:#(Exception): ...
#    except TypeError as err:#(Exception): ...
    except ValueError as err:#(Exception): ...
        ic()
        print(err)
        print('Error name: value error')
        lines=4
    except FloatingPointError as err:#(ArithmeticError): ...
        ic()
        print(err)
        print('Error name: float error')
        lines=4
#    except OverflowError as err:#(ArithmeticError): ...
#    except ZeroDivisionError as err:#(ArithmeticError): ...

    except IndexError as err:#(LookupError): ...
        ic()
        print(err)
        print('Error name: index error')
        lines=4
#    except KeyError as err:#(LookupError): ...
#    except UnboundLocalError as err:#(NameError):

        print('Wild card exception',err)
    except:# non explicit exception and will catch everything
        #pass
        #break
        #continue
        ic()
        print(err)
        print('Error name: undefined exception')
        lines=4
        print('undefined exception')
    finally:
        print('last attempt at a resolution')
        try:
            1
        except KeyboardInterrupt:
            restart_file()
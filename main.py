import sys


def Hello(name):
    if name == 'Alice':
        print 'Alert: Alice Mode'
        name = name + '????'
   else:
       DossNotExist()
        
    name = name + '1111'
    print 'Hello', name

def main(): 
   Hello()

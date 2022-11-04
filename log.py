"""
Koe Myint
CMPE 131
HW2a Python Q7
"""

import time

def timestamp(func):
    def currTime():
        print(time.ctime())
        func()
    return currTime
    
@timestamp
def greet(): 
    print('Hello!')

def main():
    greet()
main()

 
    

    

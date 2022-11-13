"""
Koe Myint
CMPE 131
HW2a Python Q6
"""

import time

#decorator timeme
def timeme(func):
    
    def innerTime():
        start_time = time.time()
        func()
        end_time = time.time()
        totalTime = end_time - start_time
        print("Total time", totalTime)
    return innerTime
    


    



    



    


    

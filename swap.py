"""
Koe Myint
CMPE 131
HW2a Python Q2
"""

def swap_list(my_list):
    middleIndex = (len(my_list)-1) // 2
    my_list[-1], my_list[middleIndex] = my_list[middleIndex], my_list[-1]
    return my_list
  

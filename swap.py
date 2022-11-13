"""
Koe Myint
CMPE 131
HW2a Python Q2
"""

def swapList(my_list):
  if len(my_list) % 2 == 0:
    middleIndex = (len(my_list)-1) // 2
    my_list[-1], my_list[middleIndex] = my_list[middleIndex], my_list[-1]
    return my_list
  else:
    middleIndex = (len(my_list)) // 2
    my_list[-1], my_list[middleIndex] = my_list[middleIndex], my_list[-1]
    return my_list

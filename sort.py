"""
Koe Myint
CMPE 131
HW2a Python Q3
"""

def sort_dictionary(inputDict):
    dictByAge = {}
    result = []
    # to create a new dictionary, age is the key, (name , phone) is the value
    for key in inputDict:
        name = key
        phoneNumber = inputDict[key][0]
        age = inputDict[key][1]
        if age not in dictByAge:
            dictByAge[age] = [(name, phoneNumber)]
        else:
            dictByAge[age].append((name, phoneNumber))
            
    #get the value after sorted the dictionary by key (age)
    for a in sorted(dictByAge.keys()) :
        result += dictByAge[a]
    return result
 
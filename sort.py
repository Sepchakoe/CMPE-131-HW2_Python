"""
Koe Myint
CMPE 131
HW2a Python Q3
"""

def sort_dictionary(inputDict):
    i = 0
    ageArr = []
    nameArr = []
    phNumArr = []
    
    for key in inputDict:
        name = key
        phoneNumber = inputDict[key][0]
        age = inputDict[key][1]
        
        #adding into separte arraylist
        ageArr.append(age)
        nameArr.append(name)
        phNumArr.append(phoneNumber)
        
    #start soring the arraylist by age
    i = 0
    while i < len(inputDict):
        k = 0
        while k < i:
            if (ageArr[i] < ageArr[k]):
                ageArr[k], ageArr[i] = ageArr[i], ageArr[k]
                nameArr[k], nameArr[i] = nameArr[i], nameArr[k]
                phNumArr[k], phNumArr[i] = phNumArr[i], phNumArr[k]
            k += 1
        i += 1
        
    tupleList = [(nameArr[i], phNumArr[i]) for i in range(0, len(inputDict))]
    return tupleList

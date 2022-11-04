"""
Koe Myint
CMPE 131
HW2a Python Q8
"""
def evaluate(op):
    if op == '**':
        return 3
    elif op == '/' or op == '//' or op == '*':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return -1

def infixToPostfix(s):
    lis = []
    result = []
    counter = 0
    
    for i in range(len(s)):
        if counter:
            counter -= 1
            continue
        if s[i] == ' ':
            continue
        
        mCal = s[i]
        
        if mCal == '/' and s[i + 1] == '/':
            mCal = '//'
            counter = 1
        elif mCal == '*' and s[i + 1] == '*':
            mCal = '**'
            counter = 1
        elif (mCal.isdigit() and i < len(s) - 1) and s[i + 1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                mCal += s[j]
                counter += 1
                j += 1
        
        if mCal.isdigit():
            result.append(mCal)
        elif mCal == '(':
            lis.append(mCal)
        elif mCal == ')':
            while lis[-1] != '(':
                result.append(lis.pop())
            lis.pop()
        else:
            while lis and evaluate(mCal) <= evaluate(lis[-1]):
                result.append(lis.pop())
            lis.append(mCal)
    
    while lis:
        result.append(lis.pop())
    
    return result
    
def calculator(s):
    eq = infixToPostfix(s)
    lis = []
    
    for i in eq:
        if i.isdigit():
            lis.append(i)
        else:
            num1 = float(lis.pop())
            num2 = float(lis.pop())
            
            if i == '+':
                lis.append(num1 + num2)
            elif i == '-':
                lis.append(num2 - num1)
            elif i == '*':
                lis.append(num2 * num1)
            elif i == '/':
                lis.append(num2 / num1)
            elif i == '**':
                lis.append(num2 ** num1)
            elif i == '//':
                lis.append(num2 // num1)
                
    return lis[-1]


    

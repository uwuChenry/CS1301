"""
Georgia Institute of Technology - CS1301
Homework 3 - Iteration
"""

#########################################

"""
Function Name: employeeData()
Parameters: employeeName (str), employeeData (str), dataType (str)
Returns: cleanData (str)
"""

def employeeData(a, b, c):
    out = ""
    if c == "Phone":
        for char in b:
            if char in "@%&":
                continue
            else:
                out+=char
    else:
        for char in b:
            if char in "-$#":
                continue
            else:
                out += char
    return (f"{a}, {c}: {out}")
    pass


#########################################

"""
Function Name: dwightsBeets()
Parameters: beetDiameter (str)
Returns: message (str)
"""

def dwightsBeets(a):
    sum = 0
    count = 0
    high = 0
    for char in a:
        if char in ",":
            continue
        else:
            sum += int(char)
            count += 1
            if int(char) > high:
                high = int(char)
    if (sum / count > 5):
        print("Wowee, what a haul!")
    if (sum / count < 2):
        print("Better luck next year!")
    return f"Avg diameter of this harvest is {sum/count} inches and biggest beet is {high} inches"
    pass


#########################################

"""
Function Name: findBudget()
Parameters: totalPrice (int), discountIndicies (str)
Returns: discountedPrice (str)
"""

def findBudget(a, b):
    out = ""
    a = str(a)
    for char in b:
        if int(char) >= len(a):
            continue
        else:
            out += a[int(char)]
    return f"${out}"
    pass


#########################################

"""
Function Name: datePlanner()
Parameters: budget (int)
Returns: dates (str)
"""

def datePlanner(a):
    out = ""
    first = True
    yes = False
    while (a >= 10):
        yes = True
        if a >= 100:
            if first == False:
                out += ", "
            out += "Travel"
            a -= 100
            first = False
            continue
        if a >= 50:
            if first == False:
                out += ", "
            out += "Dinner"
            a -= 50
            first = False
            continue
        else:
            if first == False:
                out += ", "
            out += "Stay In"
            a -= 10
            first = False
            continue
    if a != 0:
        print(f"You have {a} dollars left over!")
    if yes == False:
        return "No Dates"
    else:
        return out
    pass


#########################################

"""
Function Name: palindromeParser()
Parameters: recieptCodes (str)
Returns: palindromes (str)
"""

def palindromeParser(a):
    out = ""
    count = int(len(a)/5)
    for i in range(count):
        temp = a[i*5:(i+1)*5]
        print(temp)
        if temp[0] == temp[4] and temp[1] == temp[3]:
            out+=temp
    if out == "":
        return "None found!"
    else:
        return out
    pass

print(palindromeParser("123451232154321"))
#########################################

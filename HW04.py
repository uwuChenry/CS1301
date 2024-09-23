"""
Georgia Institute of Technology - CS1301
Homework 4 - Strings and Lists
"""

#########################################
"""
Function Name: snackMaker()
Parameters: orders (list), snacks (list), drinks (list)
Returns: moviegoers (list)
"""
import math

def snackMaker(a, b, c):
    out = []
    for thing in a:
        snack = False;
        drink = False;
        for stuff in b:
            if stuff == thing[1]:
                snack = True
                break
        for drinks in c:
            if drinks == thing[2]:
                drink = True
                break
        if snack and drink:
            out.append(thing[0])
    out.sort()
    return out
    pass

#########################################

"""
Function Name: gravityEquation()
Parameters: calculations (str)
Returns: correctResults (list)
"""

def gravityEquation(a):
    arr = []
    a = str(a)
    arr = a.split("_")
    out = []
    for thing in arr:
        lcount = 0
        dcount = 0
        outnum = ""
        for ch in thing:
            if ch.isdigit():
                dcount += 1
                outnum += ch
            if ch.isalpha():
                lcount += 1
        if lcount == dcount:
            out.append(int(outnum))
    out.sort()
    return out
    pass

#########################################

"""
Function Name: findReference()
Parameters: message (str)
Returns: decryptedMessage (str)
"""

def findReference(a):
    a = a[::-1]
    templ = ""
    tempu = ""
    for ch in a:
        if ch.isalpha() or ch == " ":
            if ch.islower() or ch == " ":
                templ += ch
            if ch.isupper() or ch == " ":
                tempu += ch
    out = templ + tempu
    out = out.rstrip()
    return out
    pass


#########################################

"""
Function Name: getNextCoordinate()
Parameters: wormholeCoordinates (list), currentLocation (list)
Returns: nextCoordinate (string)
"""

def getNextCoordinate(a, b):
    shortest = 2 ** 64
    index = 0
    for i in range(len(a)):
        dist = math.sqrt((a[i][0]-b[0]) ** 2 + (a[i][1]-b[1]) ** 2 + (a[i][2]-b[2]) ** 2)
        if dist <= shortest:
            shortest = dist
            index = i
    if shortest <= 50:
        out = [a[index][0], a[index][1], a[index][2]]
        return (f"The next coordinate is {out}, we can go!")
    else:
        return (f"Oops..., not enough fuel to make it to {a[index][3]}!")
    pass

#########################################

"""
Function Name: timeDilationCalculator()
Parameters: planetNames (list), planetDetails (list)
Returns: dilationCalculations (list)
"""

def timeDilationCalculator(a, b):
    lowest = 2**63
    index = 0
    tooStrong = False
    out = []
    needpop = []
    for i in range(len(a)):
        if b[i][1] >= 20:
            print(f"{a[i]}'s gravitational force is too strong.")
            needpop.append(int(i))
            tooStrong = True
    needpop.sort()
    needpop.reverse()
    for i in needpop:
        a.pop(i)
        b.pop(i)
    for i in range(len(a)):
        dilation = float((b[i][0]/(b[i][1] ** 3)))
        if dilation <= lowest:
            lowest = dilation
            index = i
        dilation = round(dilation, 2)
        out.append(str(a[i]) + ": " + str(dilation))
    if tooStrong:
        print (f"The lowest dilation is {a[index]}.")
    out.sort()
    return out
    pass


print(timeDilationCalculator(['Asgard', 'Sakaar', 'Vormir', 'Jotunheim', 'Titan'], [[12378912673, 21], [632411, 11], [389542, 8], [46723, 26], [59263847, 14]])   )
#########################################

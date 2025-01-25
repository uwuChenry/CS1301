"""
Georgia Institute of Technology - CS1301
Homework 5 - Tuples and Modules
"""

#########################################
"""
Function Name: chiliChampion()
Parameters: nameList ( list ), scoreList ( list )
Returns: winner ( str ) 
"""

def chiliChampion(a, b):
    arr = []
    for i in range(len(a)):
        sum = 0
        for scores in b[i]:
            sum += scores
        avg = sum / len(b[i])
        temp = (avg, a[i])
        print(f"{temp[1]}: {round(avg, 2)}")
        arr.append(temp)
    arr.sort()
    arr.reverse()
    return f"{arr[0][1]} wins with a whopping {round(arr[0][0],2)} points!"
    pass

#########################################

"""
Function Name: autumnBucketList()
Parameters: allActivities ( list )
Returns: chosenActivities ( list )
"""

def autumnBucketList(a):
    copy = []
    for thing in a:
        if thing[1] == 0:
            continue
        else:
            copy.append(thing)
    if copy == []:
        print("Is it summertime yet?")
        return []
    copy.sort(key=lambda x:x[1])
    copy.reverse()
    out = []
    for things in copy:
        out.append(things[0])
    if copy != []:
        print(f"With {copy[0][1]} votes, {copy[0][0]} wins!")
    return out
    pass

#########################################

"""
Function Name: applePicker()
Parameters: schedule ( list )
Returns: dates ( list )
"""
import calendar
def applePicker(a):
    out = []
    months = calendar.month_name
    for things in a:
        b = []
        b = things.split('-')
        for i in range (len(b)):
            b[i] = int(b[i])
        if calendar.isleap(b[2]):
            continue
        if calendar.weekday(b[2], b[0], b[1]) == 5 or calendar.weekday(b[2], b[0], b[1]) == 6:
            out.append(f"{months[b[0]]} {b[1]}, {b[2]}")
    if out == []:
        return "Sorry, we cannot pick any apples :("
    else:
        return out
    pass

#########################################

"""
Function Name: hayrideHero()
Parameters: coordinateList ( list )
Returns: distanceStr ( str )
"""
import math
def hayrideHero(a):
    total = 0
    lastx = 0
    lasty = 0
    for things in a:
        dist = math.sqrt((things[1] - lastx)**2 + (things[2] - lasty)**2)
        total += dist
        lastx = things[1]
        lasty = things[2]
    return f"This hayride is {round(total, 2)} miles long!"
    pass


#########################################

"""
Function Name: jumpKing()
Parameters: personList ( list )
Returns: winnerAndLoser ( str )
"""

from leafTally import *

def jumpKing(a):
    out = []
    if len(a) < 2:
        return "Please enter 2 TAs!"
    else:
        for things in a:
            leafletter = []
            for l in things[1]:
                leafletter.append(l[0])
            out.append((things[0], leafTally(leafletter)))
        out.sort(key=lambda x:x[1])
        out.reverse()
        return f"{out[0][0]} wins with {out[0][1]} points! {out[len(out)-1][0]} lost with only {out[len(out)-1][1]} points..."
    pass


#########################################

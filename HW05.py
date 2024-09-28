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
    
    pass


#########################################

"""
Function Name: applePicker()
Parameters: schedule ( list )
Returns: dates ( list )
"""

def applePicker():
    pass


#########################################

"""
Function Name: hayrideHero()
Parameters: coordinateList ( list )
Returns: distanceStr ( str )
"""

def hayrideHero():
    pass


#########################################

"""
Function Name: jumpKing()
Parameters: personList ( list )
Returns: winnerAndLoser ( str )
"""

def jumpKing():
    pass


#########################################

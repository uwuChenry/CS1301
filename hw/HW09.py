"""
Georgia Institute of Technology - CS1301
Homework 9 -  Recursion
"""

#########################################

"""
Function Name: eaglesVsJags()
Parameters: scores (list)
Returns: phillyPoints (int)
"""

# def eaglesVsJags(l):
#     out = 0
#     for t, s in l:
#         if t == "E":
#             out +=s
#     return out

def eaglesVsJags(l):
    if not l:
        return 0
    t, s = l[0]
    if t == "E":
        return s + eaglesVsJags(l[1:])
    else:
        return eaglesVsJags(l[1:])

#print(eaglesVsJags([("E", 7), ("E", 3), ("J", 3), ("E", 7), ("E", 3)]))

#########################################

"""
Function Name: nextDestination()
Parameters: hiddenDestination (str)
Returns: wheresNext (str)
"""

def nextDestination(s):
    if not s:
        return ""
    a = str(s[0])
    if a.isalpha():
        return a + nextDestination(s[1:])
    else:
        return nextDestination(s[1:])
    pass

#print(nextDestination("S!p!a2023i!n!"))
#########################################

"""
Function Name: canCrash()
Parameters: peopleAndThings (list)
Returns: notSafe (list)
"""
def insertInOrder(item, sorted_list):
    # Base case: Insert item at the correct position in the sorted list
    if not sorted_list or item <= sorted_list[0]:
        return [item] + sorted_list
    else:
        # Recursively find the right position for the item
        return [sorted_list[0]] + insertInOrder(item, sorted_list[1:])
    
def canCrash(l):
    if not l:
        return []
    # print(l[0])
    if len(l[0]) % 2 == 1:
        return insertInOrder(l[0], canCrash(l[1:]))
        # return [l[0]] + canCrash(l[1:])
    else:
        return canCrash(l[1:])
    pass

print(canCrash(['Ziyan', 'Krish', 'Phil', 'Noah', 'John', 'Rohan']))
# def canCrash(l):
#     out = []
#     for things in l:
#         if len(things) % 2 == 1:
#             out.append(things)
#     return out

# print(canCrash(['Pedestrians', 'Car', 'GT Stinger', 'Cone']))
####################################

"""
Function Name: travelLog()
Parameters: cityList (list)
Returns: visitedDict (dict)
"""

def travelLog(l):
    if not l:
        return {}
    s, c, v = l[0]
    out = travelLog(l[1:])
    if v:
        if s not in out.keys():
            out[s] = []
        out[s].append(c)
        out[s].sort()
    return out

# print(travelLog([('FL', 'Tampa', True), ('FL', 'Miami', True),        ('NC', 'Raleigh', False), ('NC', 'Charlotte', True),               ('TN', 'Chattanooga', False)]))
    


#########################################

"""
Function Name: bobaBuilder()
Parameters: menuItems (list)
Returns: finalItem (str)
"""

def bobaBuilder(l):
    if not l:
        return ""
    thing = l[0]
    if type(thing) == str:
        return thing + bobaBuilder(l[1:])
    else:
        return bobaBuilder(thing) + bobaBuilder(l[1:])

print(bobaBuilder(["Mango ", "Green ", "Tea"]))

#########################################

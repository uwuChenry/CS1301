"""
Georgia Institute of Technology - CS1301
Homework 6 - Dictionaries
"""

#########################################
"""
Function Name: tacoBuilder()
Parameters: shoppingList (list), inventory (list), tacoIngredients (list)
Returns: tacoDict (dict)
"""

def tacoBuilder(a, b, c):
    d = dict()
    for thing in a:
        # if thing[1] == 0:
        #     continue
        d.update({thing[0]: thing[1]})
    # print(d)
    # print("first d")
    for thing in b:
        if thing[0] in d.keys():
            d[thing[0]] += thing[1]
        else:
            # if thing[1] == 0:
            #     continue
            d.update({thing[0]: thing[1]})
    #     print(thing)
    #     print(d)
    # print(d)
    # print("second d")
    dout = dict()
    # print(dout)
    for thing in c:
        if thing in d.keys():
            dout.update({thing: d[thing]})
        else:
            dout.update({thing: 0})
    return dout 
    pass

print(tacoBuilder([('chicken', 1), ('olives', 0), ('jalapenos', 10)], [('jalapenos', 1000), ('olives', 0)], ['jalapenos', 'olives', 'taco shells']) )
#########################################



def goodDeeds(a):
    out = {}

    maxDay = ""
    maxCount = 0

    for day, deed_list in a.items():
        day_deed_count = 0  

        # Iterate over each deed and quantity in the list
        for deed, quantity in deed_list:
            # Add to the total count of the deed in the out dictionary
            if deed in out:
                out[deed] += quantity
            else:
                out[deed] = quantity

            # Count deeds for this day
            day_deed_count += quantity

        # Check if this day has the most deeds so far
        if day_deed_count > maxCount:
            maxCount = day_deed_count
            maxDay = day

    # Print the day with the most good deeds
    print(maxDay)

    # Return the dictionary of total deeds for the week
    return out
    pass

#########################################

"""
Function Name: equivalentRatios()
Parameters: efficiency (int), bulbCandidates (dict)
Returns: betterBulbs (dict)
"""

def equivalentRatios(a, b):
    out = {}
    for bulb, tu in b.items():
        eff = tu[1] / tu[0]
        if eff > a:
            eff = round(eff, 2)
            out.update({bulb: eff})
    if out == {}:
        return "I must've upgraded them last international LED light day!"
    else:
        return out
    pass

#########################################

"""
Function Name: makePierogi()
Parameters: pierogiTypes (dict)
Returns: pierogiIngredients (dict)
"""

def makePierogi(a):
    out = {}
    for ty, it in a.items():
        for i in it:
            if i in out:
                out[i].append(ty)
            else: 
                out.update({i:[ty]})
    for i in out:
        out[i].sort()
    return out
    pass

#########################################

"""
Function Name: canMake()
Parameters: recipes (dict), ingredients (dict)
Returns: canMakeCake (bool)
"""

def canMake(a, b):
    totalin = {}
    for re, stuff in a.items():
        for things in stuff:
            if things[0] in totalin.keys():
                totalin[things[0]] += things[1]
            else:
                totalin.update({things[0]: things[1]})
    # print(totalin)
    # print(b)
    for key, item in totalin.items():
        # print(key)
        if key not in b.keys():
            return False
        elif item > b[key]:
            return False
        
    return True
    pass

# print(canMake({'Strawberry Jam': [('Strawberries', 100), ('Sugar', 2)], 'Hot Fudge': [('Chocolate', 7)]}, {'Strawberries': 200, 'Chocolate': 20}))
# #########################################

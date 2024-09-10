"""
Georgia Institute of Technology - CS1301
Homework 2 - Conditionals
"""

#########################################

"""
Function Name: auroraFate()
Parameters: age (int), isSunset (bool)
Returns: birthdayFate (str)
"""

def auroraFate(a, b):
    if (a == 16 and b == True):
        return "Oh no! We must find Prince Phillip."
    if (a > 16):
        return "Aurora is safe from the evil fairy!"
    else:
        return "It is too early to tell!"
    pass

#########################################

"""
Function Name: identifyObjects()
Parameters: material (str), weight (float)
Returns: objectName (str)
"""

def identifyObjects(a, b):
    if (a == "Metal" and b == 0.5):
        return "Dinglehopper"
    if (a == "Metal" and b == 1.0):
        return "Snarfblatt"
    if (a == "Glass" and b == 5.0):
        return "Thingamabob"
    if (a == "Leather" and b == 2.0):
        return "Whosits"
    else:
        return "Well then it must be a whatsits!"
    pass


#########################################

"""
Function Name: cinderellaSearch()
Parameters: candidateName (str), shoeSize (int)
Returns: suitableStr (str)
"""

def cinderellaSearch(a, b):
    if (a == "Jaq" or a == "Gus"):
        return "This isn't Cinderella!"
    if (b >= 3 and b <=6):
        print(a)
        out = "Cinderella may have a shoe size of " + str(b) + "."
        return out
    else:
        out = a + " is not a suitable fit!"
        return out
    pass



#########################################

"""
Function Name: voyageDecision()
Parameters: weatherType (str), timeOfDay (str)
Returns: None (NoneType)
"""

def voyageDecision(a, b):
    if (a == "sunny" and b == "night"):
        print("We'll leave first thing in the morning!")
        return
    if (a == "sunny"):
        print("Time to set sail!")
        return
    if (a == "rainy" and b == "morning"):
        print("Time to set sail!")
        return
    if (a == "rainy"):
        print("Let's wait for better weather.")
        return
    if (a == "stormy"):
        print("Uh oh, we need to cancel the voyage.")
        return
    pass


#########################################

"""
Function Name: aWholeNewWorld()
Parameters: numOfGuards (int), isAsleep (bool)
Returns: response (str)
"""

def aWholeNewWorld(a, b):
    c = False
    if (a == 0 and b == True):
        c = True
        print("Let's go!")
        return "A dazzling place I never knew!"
    if (a == 0 and b == False):
        c = True
        print("I'll need to be back by midnight.")
        return "A dazzling place I never knew!"
    if (a <= 3 and b == True):
        c = True
        print("I can sneak around the guards.")
        return "A dazzling place I never knew!"
    if (c == False):
        return "Where's a genie when you need them?"
    pass

def main():
    aWholeNewWorld(4, False)

if __name__ == '__main__':
    main()
#########################################
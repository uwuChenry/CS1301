"""
Georgia Institute of Technology - CS1301
Homework 7 - File I/O and CSV Files
"""

#########################################

"""
Function Name: findGreenestFlight()
Parameters: start (str), end (str)
Returns: totalCarbonEmissions (float)
"""

def getRoutes(filename):
    routes = {}
    with open(filename, 'r') as file:
        count = 0
        tempname = ""
        for a in file:
            count +=1
            if count %5 == 1:
                tempname = a.strip()
            if count %5 == 4:
                thing = a.strip()
                thing2 = ""
                for letters in thing:
                    if letters.isdigit():
                        thing2 += letters
                routes.update({tempname:float(thing2)})
            if count %5 == 2 or count %5 == 3 or count %5 == 5:
                continue
    return routes

def findGreenestFlight(start, end):
    routes = getRoutes('emissions.txt')
    minEmission = float('inf')
    for key, item in routes.items():
        if key[:3] == start and key[-3:] == end:
            if float(item) < minEmission:
                minEmission = item
    if minEmission == float('inf') or minEmission > 2.0:
        print("Who left the engine running?")
    else:
        print("Ready for takeoff!")
        return minEmission
    pass

print(findGreenestFlight("NYC", "LAX"))

#########################################

"""
Function Name: lowestEmissions()
Parameters: flights (dict)
Returns: None (NoneType)
"""

def getModels(filename):
    outDict = {}
    with open(filename, 'r') as file:
        arr = []
        for stuff in file:
            if stuff.strip() == "":
                continue
            arr.append(stuff.strip())
    for i in range(int(len(arr)/4)):
        index = i * 4
        outDict [arr[index]] = (arr[index+1], arr[index+2], arr[index+3])
    return outDict      

getModels('fleetData.txt')

def lowestEmissions(inflights):
    models = getModels('fleetData.txt')
    out = {}
    for key, value in inflights.items():
        dist, p = value
        for key, value in models:
            


    pass


#########################################

"""
Function Name: csvToList()
Parameters: fileName (str)
Returns: flightsList (list)
"""

def csvToList():
    pass


#########################################

"""
Function Name: csvToDict()
Parameters: fileName (str)
Returns: flightsDict (dict)
"""

def csvToDict():
    pass


#########################################

"""
Function Name: worstRoutes_list()
Parameters: originCountry (str), destCountry (str), flightsList (list)
Returns: message (str)
"""

def worstRoutes_list():
    pass


#########################################

"""
Function Name: worstRoutes_dict()
Parameters: originCountry (str), destCountry (str), flightsDict (dict)
Returns: message (str)
"""

def worstRoutes_dict():
    pass


#########################################

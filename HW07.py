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

# print(findGreenestFlight("NYC", "LAX"))

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
    import csv
    models = getModels('fleetData.txt')
    out = {}
    for key, value in inflights.items():
        dist, p = value
        temp = []
        for mkey, mvalue in models.items():
            if dist <= int(mvalue[1]) and p <= int(mvalue[0]):
                temp.append((mvalue[2], mkey))
        out[key] = temp
        temp = []
    out2 = []


    with open("output.csv", mode="w", newline="") as file:

        for key, value in out.items():
            value.sort()
            out2.append([f"{key}: {value[0][1]}"])
        writer = csv.writer(file)
        writer.writerow(["The planes to be used for today's flights:"])
        writer.writerow([])
        writer.writerows(out2)
    print(out2)
    pass


flights = {"ATL-JFK" : (900,120),"ATL-LAX": (1500,90),"ATL-ORD": (850,160),"ATL-SFO": (1200,80),"ATL-BOS": (700,130)}
lowestEmissions(flights)

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

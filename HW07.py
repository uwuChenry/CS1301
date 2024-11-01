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
                    if letters.isdigit() or letters in ".":
                        thing2 += letters
                routes.update({tempname:float(thing2)})
            if count %5 == 2 or count %5 == 3 or count %5 == 5:
                continue
    return routes

def findGreenestFlight(start, end):
    routes = getRoutes('emissions.txt')
    # print(routes)
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
    import csv
    #import pandas
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
    for key, value in out.items():
        value.sort()
        if value == []:
            out2.append([f"{key}:"])
            continue
        out2.append([f"{key}:{value[0][1]}"])
    with open("todaysFleet.txt", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["The planes to be used for today's flights:"])
        writer.writerow([])
        writer.writerows(out2[:-1])
        file.write(str(out2[-1][0]))
    # out2.insert(0, "The planes to be used for today's flights:")
    # out2.insert(1, None)
    # df = pandas.DataFrame(out2)
    # df.to_csv("testing.txt", index=False, header=False)
f2 = {'ATL-JFK': (900, 120), 'ATL-LAX': (1500, 90), 'ATL-ORD': (1100, 200), 'ATL-MIA': (400, 80), 'ATL-SFO': (1200, 110)}
flights = {"ATL-JFK" : (900,120),"ATL-LAX": (1500,90),"ATL-ORD": (850,160),"ATL-SFO": (1200,80),"ATL-BOS": (700,130)}
lowestEmissions(f2)

#########################################

"""
Function Name: csvToList()
Parameters: fileName (str)
Returns: flightsList (list)
"""

def csvToList(filename):
    import csv
    import time
    time.sleep(5)
    out = []
    try:
        with open(filename, 'r') as file:
            first = True
            reader = csv.reader(file)
            for row in reader:
                if first:
                    first = False
                    continue
                out.append((row[0], row[1], int(row[2])))
        return out
    except Exception as e:
        # print(e)
        return []

print(csvToList("flight_emissions_data_short.csv"))
#########################################

"""
Function Name: csvToDict()
Parameters: fileName (str)
Returns: flightsDict (dict)
"""

def csvToDict(filename):
    arr = csvToList(filename)
    out = {}
    for thing in arr:
        if (thing[0], thing[1]) in out.keys():
            out[(thing[0], thing[1])].append(int(thing[2]))
        else:
            out[(thing[0], thing[1])] = [int(thing[2])]
    return out
    # import csv
    # try:
    #     first = True
    #     out = {}
    #     with open(filename, 'r') as file:
    #         reader = csv.reader(file)
    #         for row in reader:
    #             if first:
    #                 first = False
    #                 continue
    #             key = (row['rom_country'], row['dest_country'])
    #             out

    # except:
    #     return {}
    pass
#print(csvToDict("flight_emissions_data_short.csv"))

#########################################

"""
Function Name: worstRoutes_list()
Parameters: originCountry (str), destCountry (str), flightsList (list)
Returns: message (str)
"""
flist = csvToList("flight_emissions_data_short.csv")


def worstRoutes_list(start, end, flist):
    temp = []
    for things in flist:
        if things[0] == start and things[1] == end:
            temp.append(int(things[2]))
    temp.sort()
    #print(temp)
    return(f"{start} to {end}: {temp[-1]} carbon emissions.")
    pass

#print(worstRoutes_list("India","Australia", flist))

#########################################

"""
Function Name: worstRoutes_dict()
Parameters: originCountry (str), destCountry (str), flightsDict (dict)
Returns: message (str)
"""
dictflights = csvToDict("flight_emissions_data_short.csv")
    
def worstRoutes_dict(start, end, flist):
    for value in flist.values():
        value.sort()
    return (f"{start} to {end}: {flist[(start, end)][-1]} carbon emissions.")
    pass

#print(worstRoutes_dict("India","Australia", dictflights))
#########################################

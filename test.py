def parse_emissions_file(filename):
    flights = {}
    print("hi")
    file = open(filename, 'r')
    thing = file.readlines()
    print(thing)
    # for stuff in thing:
    #     flights
    thing2 = sum(1 for line in file)
    print(thing2)
    return flights

#print(parse_emissions_file('emissions.txt'))


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
                routes.update({tempname:a.strip()})
            if count %5 == 2 or count %5 == 3 or count %5 == 5:
                continue
    return routes
print(getRoutes('emissions.txt'))
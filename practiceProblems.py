
def rockRambleRoll():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    out = float(a * 9 + b*5.5 + c*8 + d * 2.25)
    print(f"You need to spend ${out} at Rock, Ramble, and Roll.")
    pass

def houseParty():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    totalMin = a * 10 + b * 20 + c * 45 + d * 15
    hours = int(totalMin / 60)
    minOut = totalMin % 60
    print(f"You will spend {hours} hour(s) and {minOut} minutes at the house party.")
    pass

def enterTheCave(a, b):
    if a == "Open Sesame":
        if b >= 0 and b <= 25:
            print("You have opened the door")
            return
    if a == "Hello World":
        if b >= 75 and b <= 100:
            print("You have opened the door")
            return
    if a == "Python Enjoyer" and b == 50:
        print("You have closed the door")
        return
    print("INTRUDER ALERT")
    pass


def dinnerTime(a):
    a = int(a)
    distance = [250, 460, 820, 870, 940]
    shortest = abs(a-250) #placeholder
    b = 0;
    for i in range(1, 5):
        temp = abs(distance[i] - a)
        if temp <= shortest:
            shortest = temp
            b = i
    match b:
        case 0:
            return "Sun, Sand, and Seafood"
        case 1:
            return "The Beachcomber's Bistro"
        case 2:
            return "Coastal Catch"
        case 3:
            return "Beachside Bonanza"
        case 4:
            return "Tidal Wave Tavern"
    pass


def lightCommunicator(a):
    arr = []
    out = ""
    for char in a:
        if char == "T":
            arr.append("S")
        elif char == "S":
            arr.append("T")
        elif char == "t":
            arr.append("s")
        elif char == "s":
            arr.append("t")
        else:
            arr.append(char)
    arr.reverse()
    for thing in arr:
        out += thing
    return out

def totalTime(a):
    arr = []
    arr = a.split()
    s = 0
    for thing in arr:
        s += int(thing)
    h = int(s/60)
    m = s%60
    return(f"{h} hour(s) and {m} minute(s)")
pass

def meatlessMonday(d):
    a = d.split("-")
    b = []
    out = []
    for line in a:
        temp = ""
        for letter in line:
            if letter.isalpha():
                temp+=letter.lower()
        b.append(temp)
    for things in b:
        if things and things[0].lower() == "v":
            c = things[1:]
            out.append(c)
    out.sort()
    return out

# print(meatlessMonday('t!a0cos-vpi!zz#a-ChiC!ke#@n-vcAu!li$flo!wer'))

def eatingOut(l1, l2):
    out = []
    for things in l1:
        if things in l2:
            out.append(things)
    if out == []:
        return "Whatever, we'll go to Nave."
    return sorted(out)

def organizeTimes(l):
    out = []
    for things in l:
        temp = sorted(things[0])
        temp.pop()
        out.append((things[1], temp))
    return sorted(out)


import gymBroTools
def findPlates(i):
    d = {45:0, 35:0, 25:0, 10:0, 5:0}
    out = []
    t = gymBroTools.plateCalculator(i)
    if t == ():
        return []
    for things in t:
        d[int(things)] +=1
    for key, value in d.items():
        out.append((key, value))
    out.sort()
    out.reverse()
    return out

# print(findPlates(680))


def lunchSpots(d):
    out = {}
    for key, value in d.items():
        for thing in value:
            if thing not in out.keys():
                out[thing] = []
            out[thing].append(key)
    for a in out:
        out[a].sort()
    return out

def creditHours(d1, d2):
    out = 0
    for key, value in d2.items():
        for c in value:
            out += d1[key][c]
    return out


def foreignFilms(a):
    outdict = {}
    movieToCountryDict = {}
    with open("movies.txt") as m:
        lines = m.readlines()
    for i in range(2, len(lines), 5):
        mTitle = lines[i].strip()
        mCountry = lines[i+1].strip()
        if mCountry not in movieToCountryDict.keys():
            movieToCountryDict[mCountry] = []
        movieToCountryDict[mCountry].append(mTitle)
        movieToCountryDict[mCountry].sort()
    for key, value in a:
        outdict[key] = movieToCountryDict.get(value, [])
    return outdict

def inSeason(favdrinkL, curM):
    lines = []
    out = []
    with open ("summerDrinks.csv") as s:
        for l in s:
            lines.append(l.strip().split(","))
    print(lines)
    for thing in lines:
        print(thing)
        if thing[2] == "uncaffeinated" and thing[3] == curM and thing[0] in favdrinkL:
            out.append(thing[0])
    if out != []:
        return out
    return "Nothing is in season :("

import requests as r
def shareBorder(c1, c2):
    res = r.get("https://restcountries.com/v3.1/name/"+c1)
    e = res.json()
    b = e[0]["borders"]
    # print(b)
    res2 = r.get("https://restcountries.com/v3.1/name/"+c2)
    d = res2.json()[0]["cca3"]
    # print(d)
    if d in b:
        return True
    return False

def numCoffees(i):
    if i == 0:
        print("No more coffee!")
        return
    print (f"Coffees left: {i}")
    numCoffees(i-1)

def currencyRatio(c1, c2):
    a = r.get("https://restcountries.com/v3.1/all").json()
    c1count = 0
    c2count = 0
    for thing in a:
        for stuff in thing["continents"]:
            if stuff == c1:
                c1count +=1
        # if thing["continents"][0] == c1:
        #     c1count +=1
            # print(thing['name']["common"])
            # print(c1count)
            # for d in thing["currencies"]:
            #     print("c---" + thing["currencies"][d]["name"])
            #     if thing["currencies"][d]["name"] == c2:
            #         c2count +=1
            #         print("c---" + str(c2count))
    b = r.get("https://restcountries.com/v3.1/currency/"+c2.lower()).json()
    for thing in b:
        if thing["continents"][0] == c1:
            c2count +=1
    # print(c2count)
    return round(float(c2count/c1count),2)

# print(currencyRatio("Europe","Euro"))

def atlCoffee(l):
    if l == []:
        return {}
    n, a, r = l[0]
    v = atlCoffee(l[1:])
    if r > 5:
        if a not in v.keys():
            v[a] = []
        v[a].append(n)
        v[a].sort()
    return v

class Friend:
    def __init__(self, iname, iage, food = None, rsvp = True):
        self.name = iname
        self.age = iage
        self.foodItem = food
        self.rsvpStatus = rsvp
    
    def __str__(self):
        if self.rsvpStatus:
            return f"My name is {self.name}. I am {self.age} years old, and I am bringing {self.foodItem}!"
        return f"My name is {self.name}. Unfortunately, I cannot go to the potluck :("
    
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age and self.foodItem == other.foodItem:
            return True
        return False
    
class Potluck:
    def __init__(self, h, gl = None):
        self.host = h
        if gl:
            self.guestList = gl
        else:
            self.guestList = []
    
    def __str__(self):
        return f"My name is {self.host.name}, and I am hosting a potluck. There are {len(self.guestList)} people coming."
    
    def invite(self, f):
        if f.rsvpStatus:
            self.guestList.append((f.name, f.foodItem))
    def checkFood(self):
        good = True
        for g in self.guestList:
            if g == None or g[1] == None:
                good = False
                print(f"Uh oh! {g[0]} forgot to bring food!")
        if good:
            print("Nice! Everyone brought something!")
# teghpreet = Friend('Teghpreet', 19, None, True)
# avinash = Friend('Avinash', 20, "cookies")
# chris = Friend('Chris', 20, 'apple juice')
# shayan = Friend('Shayan', 19, None, False)
# potluck = Potluck(teghpreet)

# potluck.invite(avinash)
# potluck.invite(chris)
# potluck.invite(shayan)
# potluck.checkFood()
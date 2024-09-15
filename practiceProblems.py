
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
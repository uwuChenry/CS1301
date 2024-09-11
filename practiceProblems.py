
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
    distance = [250, 460, 820, 870, 940]
    shortest = 10000000 #placeholder
    for i in distance:
        temp = abs(a - i)
        
    pass
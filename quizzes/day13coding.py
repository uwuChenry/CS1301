def everyOtherItemStr(a):
    outlist = []
    lastString = False
    for thing in a:
        if type(thing) == type("abc") and lastString == False:
            outlist.append(thing)
            lastString = True
            continue
        if type(thing) == type("abc") and lastString == True:
            lastString = False
            continue
    return outlist

print(everyOtherItemStr([3,5,1,4,"aa","ab"]))  # should print ["aa"]
print(everyOtherItemStr(["cat", "dog", 34]))   # should print ["cat"]
print(everyOtherItemStr([1, 5, 2, 6.4]))       # should print []
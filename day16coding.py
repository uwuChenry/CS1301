def petChoices(a, b):
    outlist = []
    petlist = a
    for things in petlist:
        if things[1] <= b:
            outlist.append(things[0])
    outlist.sort()
    return outlist

maxWeight = 5
listPets = [("goat", 50),("turtle",2),("chicken",5),("cat",10),("dog",20)]
print(petChoices(listPets, maxWeight)) # should print ["chicken","turtle"]

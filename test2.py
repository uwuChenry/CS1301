# def pandaAllies(poList):
#     oogwayList = poList
#     # taiLungList = poList[:]
#     # print(oogwayList)
#     # print(taiLungList)
#     # oogwayList[1].append("general kai")
#     # taiLungList[1].append("tset")
#     # print(oogwayList)
#     # print(taiLungList)
#     # print(poList[1][-1])
#     # print(taiLungList[-1])
#     # taiLungList.remove("viper")
#     # print(oogwayList[0])
#     # poList[1] = "mantis"
#     # print(taiLungList[0])
#     # oogwayList.append(["jack black"])
#     # print(poList)

# poList = ["viper", ["crane", "monkey"]]
# pandaAllies(poList)



# def noodleShop(supplyList, ordersDict):
#     count = 0
#     for x, y in enumerate(supplyList):
#         print(x)
#         print(y)
#         # if y != "Noodles":
#         #     count += x
#         # if x not in ordersDict:
#         #     print("Not a bad job")
#         # else:
#         #     if ordersDict[x] != "Po":
#         #         print("Dragon warrior?")
#         #     else:
#         #         print("Quit, don't quit. Noodles!")
#     return count

# supplyList = ["Noodles", "Dumplings", "Noodles", "Noodles"]
# ordersDict = {1: "Po", 0: "Crane", 2: "Mantis"}
# print(noodleShop(supplyList, ordersDict))

# print(len({"Miami": 1, "Bahamas": 2, "Cuba": 3, "Miami": 4}))


# thing = ["Lake Como", "Lake Saimaa"].append("Lake Geneva")
# print(thing)


# vDict = {"Vermont": ("North America", 0),
# "Peru": ("South America", 6),
# "New Zealand": ("Oceana", 7)}

# vDict["Peru"] = ("South America", 7)
# vDict["Peru"] = (vDict["Peru"][0], vDict["Peru"][1] + 1)
# vDict["Peru"] = "South America", + 7,

# whereTo = "\ny or bos\to\n".strip()
# print(len(whereTo))
# print(len("a"))
# print(whereTo)


# alist = ["I", "Love", "Spring", "Break"]
# astr = ""
# for v,i in enumerate(alist):
#     print(v)
#     print(i)


# def toDo(aList):
#     x = aList[2][1]
#     print(x)
#     y = aList[0][1]
#     print(y)
#     z = y[:]

#     y.append("MIT")
#     print(z)
#     print(y)
#     z.append("test")
#     z = z[::-1]
#     print(z)
#     # print((x.sort(), z[0]))
#     # print(aList[0])
#     # print(aList[2])

# aList = [('BOS', ['BU']), ('HOU', ['NASA']),
# ('NYC', ['WTC', 'Soho'])]
# toDo(aList)

# a = {("PSL",): "Paige", ("Pumpkin CB",): "Lasya"}
# print ("i am scary" or True)

def halloweenMovies(aList):
    bList = aList
    cList = bList[:]
    aList[2].append("Coraline")
    bList[2].sort()
    aList[2] = "Halloweentown"
    print(aList)
    print(bList)
    print(cList)
    aList = ["Halloween", "Tricks"]
    print(aList)
    print(bList)
    print(cList)
halloweenMovies(["Knives Out", "Coco", ["Hocus Pocus"]])
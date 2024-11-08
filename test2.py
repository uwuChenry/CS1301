# # def pandaAllies(poList):
# #     oogwayList = poList
# #     # taiLungList = poList[:]
# #     # print(oogwayList)
# #     # print(taiLungList)
# #     # oogwayList[1].append("general kai")
# #     # taiLungList[1].append("tset")
# #     # print(oogwayList)
# #     # print(taiLungList)
# #     # print(poList[1][-1])
# #     # print(taiLungList[-1])
# #     # taiLungList.remove("viper")
# #     # print(oogwayList[0])
# #     # poList[1] = "mantis"
# #     # print(taiLungList[0])
# #     # oogwayList.append(["jack black"])
# #     # print(poList)

# # poList = ["viper", ["crane", "monkey"]]
# # pandaAllies(poList)



# # def noodleShop(supplyList, ordersDict):
# #     count = 0
# #     for x, y in enumerate(supplyList):
# #         print(x)
# #         print(y)
# #         # if y != "Noodles":
# #         #     count += x
# #         # if x not in ordersDict:
# #         #     print("Not a bad job")
# #         # else:
# #         #     if ordersDict[x] != "Po":
# #         #         print("Dragon warrior?")
# #         #     else:
# #         #         print("Quit, don't quit. Noodles!")
# #     return count

# # supplyList = ["Noodles", "Dumplings", "Noodles", "Noodles"]
# # ordersDict = {1: "Po", 0: "Crane", 2: "Mantis"}
# # print(noodleShop(supplyList, ordersDict))

# # print(len({"Miami": 1, "Bahamas": 2, "Cuba": 3, "Miami": 4}))


# # thing = ["Lake Como", "Lake Saimaa"].append("Lake Geneva")
# # print(thing)


# # vDict = {"Vermont": ("North America", 0),
# # "Peru": ("South America", 6),
# # "New Zealand": ("Oceana", 7)}

# # vDict["Peru"] = ("South America", 7)
# # vDict["Peru"] = (vDict["Peru"][0], vDict["Peru"][1] + 1)
# # vDict["Peru"] = "South America", + 7,

# # whereTo = "\ny or bos\to\n".strip()
# # print(len(whereTo))
# # print(len("a"))
# # print(whereTo)


# # alist = ["I", "Love", "Spring", "Break"]
# # astr = ""
# # for v,i in enumerate(alist):
# #     print(v)
# #     print(i)


# # def toDo(aList):
# #     x = aList[2][1]
# #     print(x)
# #     y = aList[0][1]
# #     print(y)
# #     z = y[:]

# #     y.append("MIT")
# #     print(z)
# #     print(y)
# #     z.append("test")
# #     z = z[::-1]
# #     print(z)
# #     # print((x.sort(), z[0]))
# #     # print(aList[0])
# #     # print(aList[2])

# # aList = [('BOS', ['BU']), ('HOU', ['NASA']),
# # ('NYC', ['WTC', 'Soho'])]
# # toDo(aList)

# # a = {("PSL",): "Paige", ("Pumpkin CB",): "Lasya"}
# # print ("i am scary" or True)

# # def halloweenMovies(aList):
# #     bList = aList
# #     cList = bList[:]
# #     aList[2].append("Coraline")
# #     bList[2].sort()
# #     aList[2] = "Halloweentown"
# #     print(aList)
# #     print(bList)
# #     print(cList)
# #     aList = ["Halloween", "Tricks"]
# #     print(aList)
# #     print(bList)
# #     print(cList)
# # halloweenMovies(["Knives Out", "Coco", ["Hocus Pocus"]])

# # def rec1(num):
# #     if num==3:
# #         print(num)
# #     else:
# #         print(num)
# #         rec1(num-1)
# # rec1(6)


# # def rec1(num):
# #     if num>0:
# #         print(num)
# #         rec1(num-2)
# # rec1(6)


# # def rec1(num):
# #     if num>0:
# #         print(num)
# #         rec1(num-2)
# #         print(num)
# # rec1(6)


# def rec1(num):
#     if num<0:
#         print(num)
#         rec1(num-2)
# rec1(6)

# def f1(astr):
#     print(astr[0])
#     if len(astr) > 2:
#         f1(astr[2:])
# f1("abcdef")

# def f2(astr):
#     print(astr[0])
#     if len(astr) > 2:
#         f2(astr[2:])
# f2("abcd")

# def f3(num):
#     if num <= 0:
#         return ""
#     else:
#         return str(num) + f3(num-2)
# print (f3(5))


#Note that by mf I always mean magic find/100 and by pl I mean pet luck/100
def pet_odds(mf,pl,eyes,alpha=0.02,beta=0.0006):
    #calculates the odds at a pet with alpha being the base odds at claw and beta the base odds at a pet
    return (1-alpha*(1+mf)*eyes)*beta*eyes*(1+mf+pl)
def max_magic_find(p,e,alpha): #calculates the amount of magic find that maximizes the drop rate
    return 1/(2*alpha*e)-1-p/2
def pmin(m,p,e,alpha=0.02,beta=0.0006): #Like pet_odds but caps your mf with max_magic_find
    return pet_odds(min(m,max_magic_find(p,e,alpha)),p,e,alpha,beta)
def modified_alpha(m,e,amount=1): #calculates the base odds at claw as described in the third section
    m=m.copy()
    e=e.copy()
    if(len(m)==0):
        return 0.02/amount
    odds=0.02*(1+m.pop())*e.pop()
    return (1-odds)*(modified_alpha(m,e,amount))+odds*(modified_alpha(m,e,amount+1))
def eyes_per_pet(myMf,myPl,myEyes,othersMf,othersEyes): #Calculates the AEP
    #othersMf is supposed to be a list of the magic find/100 of the other players for example othersMf=[2.9,2.9]
    #othersEyes is supposed to be a list of the eyes placed by the other players for example if you place 2 eyes and the others 3: othersEyes=[3,3]
    alpha=modified_alpha(othersMf,othersEyes)
    myOdds=pmin(myMf,myPl,myEyes,alpha,0.0006)
    return myEyes/myOdds
def calc_mf_and_pl(mf,pl,gdrag,endermite,edrag,superior,clover,renowned,sorrowAmount):
    #Assuming 9 digits on gold collection this calculates the magic find and pet luck of the setups described in section 2
    return ((mf+1.12*gdrag+0.05*sorrowAmount)*(1+renowned*0.0406)*(1+superior*0.05)*(1+clover*0.05)*(1+edrag*0.1),(pl+0.4*endermite)*(1+renowned*0.0406)*(1+superior*0.05)*(1+edrag*0.1)*(1-clover*0.05))
def calculate_all_possibilities(base_magic_find,base_pet_luck,alpha):
    #goes through all the possibilities described in section 2 and calculates the AEP in these situations
    for e in (2,3,4,8):
        print("For "+str(e)+" eyes")
        for s in ("superior","clover","sorrow","nothing"):
            if(s=="clover"):
                print("Wearing 3/4 sorrow armor and a clover helmet")
            elif(s=="nothing"):
                print("Wearing nothing magic find or pet luck increasing")
            else:
                print("Wearing full "+s+" armor")
            for s2 in ("gdrag","endermite","edrag","no pet"):
                mf, pl=calc_mf_and_pl(base_magic_find,base_pet_luck,s2=="gdrag",s2=="endermite",s2=="edrag",s=="superior",s=="clover",True,(s=="clover")*3+(s=="sorrow")*4)
                print(s2+" yields "+str(e/pmin(mf,pl,e,alpha))+" eyes to get a pet on average")
        print("")

calculate_all_possibilities(201/100, 126/100, 0.02)
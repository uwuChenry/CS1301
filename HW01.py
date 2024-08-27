"""
Georgia Institute of Technology - CS1301
Homework 1 - Functions & Expressions
"""

#########################################

"""
Function Name: personalizedMessage()
Parameters: N/A
Returns: None (NoneType)
"""

def personalizedMessage():
    iname = input("enter your name: ")
    iyear = input("enter year: ")
    ihome = input("enter hometown: ")
    imajor = input("enter major: ")
    idate = input("enter the date today: ")
    print("%s is a %s year from %s majoring in %s. We met on %s." % (iname, iyear, ihome, imajor, idate))
    pass




#########################################

"""
Function Name: gradeCalculator()
Parameters: N/A
Returns: None (NoneType)


"""

def gradeCalculator():
    p = float(input("participation avg: "))
    hw = float(input("hw avg: "))
    exam = float(input("exam avg: "))
    lab = float(input("lab avg: "))
    final = float(input("final exam score: "))
    out = p * 0.05 + hw * 0.2 + exam * 0.45 + lab * 0.1 + final * 0.2
    out = round(out, 2)
    print ("Your final score: " + str(out) + "%")
    pass


#########################################

"""
Function Name: lunchTime()
Parameters: N/A
Returns: None (NoneType)
"""

def lunchTime():
    iclass = str(input("what is your next class? "))
    idistance = float(input("how far is it from Brittain? "))
    itime = float(input("how long do you have until class starts? "))
    timeleft = itime - idistance * 10
    timeleft = int(timeleft)
    print("You have %d minutes to eat lunch before you have to run to %s!" % (timeleft, iclass))
    pass


#########################################

"""
Function Name: snackBudget()
Parameters: N/A
Returns: None (NoneType)
"""

def snackBudget():
    budget = float(input("what is you budget this month? "))
    num = float(input("how many midterms will u have this month? "))
    coffee = round(budget * 0.2, 2)
    left = round(budget - coffee - 5*num - budget * 0.45, 2)
    outc = str(coffee)
    outl = str(left)
    print("You will spend $%s on coffee and have $%s left after the month is over!" % (outc, outl))

    pass


#########################################

"""
Function Name: freeTime()
Parameters: N/A
Returns: None
"""

def freeTime():
    c = int (input("how many credit hours are you taking? "))
    s = float (input ("how many hours of sleep do you need each night? "))
    f = float (24- s - c/2)
    m = int(f%1 * 60)
    out = int(f)
    print("Relax for %d hours and %d minutes before bed." % (out, m))
    pass


#########################################

def main():
    freeTime()

if __name__ == '__main__':
    main()
""" FILE NAME: 01code.py
    STUDENT: 
    DESCRIPTION: Let's consider an example in which we want to compute
    the total cost of an ice cream cone. We can store the number of scoops
    ordered in the variable called numberOfScoops. We can store the cost of
    each scoop in a variable called costofScoops. We can store the
    calculated total cost in a variable called totalCost.
"""

costOfScoops = 3


def main():
    print("how many scoop?")
    numOfScoops = int(input())
    total = costOfScoops * numOfScoops
    total = str(total)
    print("ur total is: " + total)
    pass

if __name__ == '__main__':
    main()















#CS1301- Day4 Functions

# === Function Basics
# syntax - def functionName(parameters):

'''
Example 1
# write a function that will print the value of a number divided by 6, display
# should be a percision of 2, use f-string formatting
# input: 2
# output: 0.33
# functions can call other functions

'''
##def divideby2(num):
##    pass
##
##def divideby3(num):
##    pass
##
##def divideby6(num):
##    return divideby2(num) - divideby3(num)
##
### testing code
##print(divideby6(18))
##print(divideby6(2))

'''
Example 2
# write a function greeting that diplays Hello along with the student
# first and last name, use input() to gather the user data,
# use f-string formatting
# input:
    What is your first name? Ahmad
    Ahmad what is your last name? Williams
# output:
    Hello Ahmad Williams.
'''
##def greeting(): 
##    pass
##
### testing code
##greeting()

'''
Example 3
# write a function square_area that returns the area of a square (int), Area =(side) × (side)
# use f-string formatting
# input: 8
# output: The area of a 8 x 8 square is 64.
'''
##def square_area(side):
##    pass
##
### testing code
##side = 12

'''
Example 4
# write a function triplename that takes as input a name <str> and
# returns the name three times added together with a "!" at the end
# use string multiplicaton and f-string formatting
# input: Janine
# output: JanineJanineJanine!
'''
##def triplename(name):
##    pass
##
### testing code
##print(triplename("Audrey"))
##print(triplename("Cynthia"))

'''
Example 5
Write a program that will ask the user to enter the amount of a purchase.
The program should then compute the state and county sales tax.
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
The program should display the amount of the purchase, the state sales tax,
the county sales tax, the total sales tax, and the total of the
sale (which is the sum of the amount of purchase plus the total sales tax).
Create a function to display the sale information using the calculated values. 

Hint: Use 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
'''
# Global constants for the state and county tax rates


# maindef
def main():
    # Local variables

    # Get the amount of the purchase
    
    # Calculate the state tax

    # Calculate the county tax

    # Call the function to print information about the sale
    pass

def showSale ():
    """ The showSale function accepts purchase, stateTax,
    countyTax as arguments and prints the equivalent
    total sale information."""
    # local variables
    #totalTax
    #totalSale

    # display the purchase information, use f-string formatting percision of 2
    #Purchase amount
    #State tax
    #County tax
    #Total tax
    #Sale total
    pass


# Call the main function.
if __name__ == '__main__':
    main()


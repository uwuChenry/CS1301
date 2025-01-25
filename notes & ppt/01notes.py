"""
Day 1 - Intro

What we're doing this time
1. IDLE
2. Comments
3. Variables
4. Intro to operators
5. First program
"""

# === Comments: begin every program with comments

# Single line comments: all text following a # sign (hash sign) is ignored.
#   It's good practice to have as many comments in your script as possible.
#   This help you remember why you wrote something in a specific way.
## Alt-3 (add)  Alt-4 (remove)

"""
Multi-line comments: all text between triple double-quotes is ignored.
"""

# === Variables

# We can store values for things (numbers, names, true and false) in what are
# called "variables". Variable names should be meaningful, and are case sensitive (Num is not num)​
# the first character must be a letter or an underscore​, and CANNOT be a digit
# can contain both letters, digits, and underscores​
# cannot be a Python keywords: sum, if, for, and, or, not, def, class, True, False
# VALID variaable names:
##my_variable
##userAge
##total_sum_2024
##_temp_value
##MAX_LIMIT

# === Standard functions

# We can have the Python Shell display what is stored inside the variable using the
# function "print".
greeting = "Hello World"
print(greeting) # the value in greeting will be displayed

# We can have the Python Shell display what the data type of the value inside the variable is
# using the function "type" inside the "print" function.
print(type(greeting)) # the data type of someName will be displayed

# === Operations

# Python utilizes the following symbols to represent different operatorions:
## = represents asignment
##(the variable is on the left of the equal sign and the value being assigned is on the right)
num1 = 15 # the integer value 15 will be stored as num1
print(num1)

## + represents summation or concatenation:
thisSum = 5 + 10 # the value 15 will be stored
print(thisSum)

thisConcat = "hello, " + "students!" # "hello, students!" will be stored
print(thisConcat)

## - represents subtraction
thisSubtraction = 9 - 2 # the value 7 will be stored
print(thisSubtraction)

## * represents multiplication
thisMult = 56 * 3 # the value 168 will be stored
print(thisMult)

## ** represents exponentiation
thisExp = 3**5 # the value 243 will be stored
print(thisExp)

## / represents floor division
thisDiv = 8/2 # the value 4 will be stored
print(thisDiv)

## // represents floor (integer) division
##(It divides the first number by another and rounds down the result to the nearest whole number)
thisFloorDiv = 9//2 # the value stored will be 4
print(thisFloorDiv)

## % represents the modulo operation
##(It returns the remainder after one number is divided by another)
thisMod = 5%2 # the value 1 will be stored
print(thisMod)

# === Example
# open the file you downloaded to your CS1315 folder named 01code.py.
# Use this standard script format to begin coding your solutions in the default function "main".
# Begin the file with documentation with the file name, your name, and the problem description.
""" FILE NAME: *.py
    STUDENT: 
    DESCRIPTION: 
"""
# Next use the following basic main function template.
def main():
    """ function documentation: input, output, purpose """
    pass

if __name__ == '__main__':
    main()




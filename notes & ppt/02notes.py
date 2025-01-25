'''
Day 2 - The basics

What we're doing this time
1. Data types
    a. What are a few data types?
    b. str, int, float, bool
    c. How do I know what type a value is?
2. Expressions
    a. What are expressions?
    b. Operators (+ - * / ** % //)
    c. Order of Operations
3. Grabbing Values from User Input
    a. What is input()?
    b. Caveats
4. Intro to Functions
    a. What are functions?
    b. Defining functions
    c. Calling functions
    d. Default function template
'''

# === Data types

# Different types of data (text, numbers, a true or false statement, etc) exist
# in the real world. For that reason, Python deals with them using different
# data types. These are the basics:

# str (string): used to store data as text, or convert another data type to str
# int (integer): used to store integers, or convert another data type to int
# float (float): used to store decimal points, or convert another data type to float
# bool (boolean): used to store True/False, or convert another data type to bool

aStr = 'this is a string! sentences are strings! anything in quotes!'
anotherStr = "it's easy to use double quotes as well"
yetAnotherStr = '2' # the string character 2
aStrtoInt = int(yetAnotherStr) # the string '2' is an integer 2

anInt = 20 # the integer 20
aInttoStr = str(20) # the integer 20 is a string '2'

aFloat = 20.05423524543253 # a decimal number
aFloattoInt = int(aFloat) # the float 20.05423524543253 is integer 20

aBool = False # True or False
aBooltoInt = int(False) # the bool False is integer 0

# To display the data type of a variable use the Python function called type
print(type(aFloat))


# === Expressions

# Expressions use operators and operands to produce a result.
# = assignment
# + sum or concatenation
# - subtraction
# * multiplication
# / division (will ALWAYS give back a float)
# ** exponentiation
# // floor division (will ALWAYS give back an integer)
# % modulo operation (remainder of integer division)

# Let's focus on the integer division expressions
print(-21 // 5) # this will print -5, since we will round to the smallest integer
                # resulting of the division between -21 and 5
    
    # Division: First, divide -21 by 5. Ignoring the signs for a moment, 21÷5 is 4.2.
    # Floor Division: usr integer (floor) division, to find the largest integer less
    # than or equal to the result of the division.
    # Adjust for Negative Numbers: When dealing with negative numbers, the floor
    # function rounds towards negative infinity.
    # For −21÷5, the result 4.2 would normally round down to 4, but
    # because we're working with negatives, it actually rounds down to −5.
    # To clarify: −21÷5 = −4.2. The largest integer less than or equal to -4.2 is -5.
    # Final Answer: Therefore,−21÷5 using integer division results in −5.
    
print(8%3)  # this will print 2, because that's the remainder of the integer division
            # between 8 and 3.

# The order of operations in Python is PEMDAS (parentheses, exponentiation,
# multiplication, division, addition, subtraction)

expEval = (8+3)**2/20   # the + will be first because it's between the parentheses,
                        # the result will then be **, and then that
                        # result will be finally / by 20
print(expEval) # this should print 11**2 divided by 20 -> 121/20 -> 6.05

# Expressions with mixed numeric types (i.e. integer and float) will take the most
# precise type will result in a float

print(2 + 6 / 2) # this should print (3.0 + 2) resulting in 5.0

# === Collecting user input

# We can gather user data by using the input function with a user prompt (str).

myInput = input('Hello! What is your name?')
print(myInput) # this will display what the user typed into the console (Shell prompt)
print(type(myInput)) # this will display the data type (willl always be a str)


# === Functions

# Functions provide for program flexibilty, by creating modularity. Meanig each task
# can be impelmented and/or modified with minimal impact on program functinality.

# In some computer programs, we have a series of steps that are executed multiple
# times accross a script. In order to avoid having to repeat these steps every
# time, we can encapsulate those steps into a subroutine, which we call a function.
# Everytime we call the function, it will execute all of those steps that are
# encapsulated in it. Let's consider the following example, where we want to
# implement a function that takes in the number of scoops of ice cream a customer
# wants and then prints out how much that is going to cost them.

# The first step is to type the Python keyword "def" and then the name we want to give
# the function (variable naming rules apply), followed by two parentheses and a :.
# You have done this when using the basic main function template.

def functionName():
    """ function documentation: input, output, purpose """
    pass

# To cause the function to execute use its function header without the keyword "def".
functionName() # unindented outside of the function

# Open the file you downloaded to your CS1315 folder named 02code.py.
# Use the standard script format to begin coding your solution and call  
# the function from inside "main".
# Begin with the standard script template.
""" FILE NAME: *.py
    STUDENT: 
    DESCRIPTION: 
"""

def main():
    """ function documentation: input, output, purpose """
    pass

if __name__ == '__main__':
    main()





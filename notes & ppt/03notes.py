'''
Day 3  - The basics+

What we did last time
1. Identifiers
2. Data types
3. Expressions
4. Grabbing Values from User Input
5. Intro to Functions

What we're doing this time
1. Data type review
    a. str, int, float, bool
    b. Converting/Casting to Different Types
2. More operator examples
    a. Order of operations
    b. Resulting data types
    c. // and %
3. Functions
    a. Declaring
    b. Calling
    c. Intro to Parameters
'''

# === Data type review

aString = 'hello' # str
aNum = -20 # int
aFloat = 20.0 # float
aBool = True # bool

# we can also store numbers as str, but then we cannot perform mathematical operations
# with them until we cast them as an integer or float as follows.
num1 = '20'
print(num1)
print(type(num1))
# here we are using the function int(num1) to convert the str of the number 20
# into an integer and using it to perform a calculation
print(int(num1) + 10)


# === Order of operations is going to be PE MD AS

print(36 ** (1/2)) # the parenthesis is calculated first and then the exponentiation
# so this will be 36**(0.5) = 6

print(2 + 2.0) # this will convert the integer 2 into a float 2.0 and sum the two
print(10 / 5) # the result of a division is always a float, so this will print 2.0
print(4 / 5) # same goes here, 0.2

print(54 // 12) # floor division will round the result to the smallest integer = 4
print(-54 // 12) # floor division will round the result to the smallest integer = -5

print(54 % 12) # This will return the remainder of the division of 54 by 12 = 6

# === Concatenation

# when we use the + sign between two strings, we concatenate them, meaning they
# form a bigger string containing the two strings.
print("Hello, " + "nice to meet you!")


# === Functions

# Functions enable us to encapsulate one or more instructions inside a subroutine
# such that we can use it along our script. They particularly useful when we are
# writing a script that requires repeating a set of instructions multiple times.
# In order to implement a function in Python we must obey the following syntax.

# We define the function name by calling the Python keyword "def" followed by the
# function name. We then open a parenthesis and put the parameters we want to include
# in the function separated by commas. We then close the parenthesis and add a colon.
# A parameter allows us to pass a value into the function as an input to be used
# as part of a set of instructions.
def sayHi(name):
    # We then use indentation to separate what statements are part of the function,
    # from those that belong to the script. The statements that are indented will
    # belong to the function and whenever we want to go back to the main script,
    # we remove the indentation.
    print('Hello! My name is '+ name) # The only instruction that I want this function
    # to execute is to print the phrase that results of the concatenation of the str
    # containing "Hello! My name is " and the name (str) that we pass into the function
    # when we call it in our main script.

""" After defining the function as we've done above, we can now call the function.
    Calling a function, means that we are actually telling our script to execute the
    function with the arguments we pass into it."""
sayHi("Rod") # by calling the function as such, it will execute the instructions
    # defined as part of this function. In this case, calling the function should simply
    # print "Hello! My name is Rod" to the terminal.

""" If we don't have any input to the function (i.e. we are not planning
    on passing on any values into the function), after the function name, you open
    and close parenthesis, followed by a colon. """
def done():
    print('Thanks for ordering!')

done()

# As long as we define functions in the appropriate order, we can call a function
# inside the body (implementation) of another function as in the following example.
# Here we will use the two previously defined functions to implement a very simple
# ordering system.
def pizzaPrice():
    # Here I am calling the function sayHi(name), passing my own name as the argument
    sayHi("Kearse") # this means that when the pizzaPrice function is executed, and
    # this line is called with "Kearse", it will execute the function sayHi and print
    # Hello! My name is Kearse to the console. Note that when a string is printed to
    # the console, it will NOT have the quotes.
    slices = int(input("How many slices would you like? ")) # this line will ask
    # for user input with the question "How many slices would you like? " and wait
    # until the user types a value. It also converts the input which is collected
    # as a str into an integer (int), so that we can perform mathematical operations
    # with it.
    slicePrice = 1.29 # this variable contains the price of a single slice as a float
    total = slices * slicePrice # we calculate the total cost of the order by multiplying
    # the integer of the number of slices by the individual price.
    print("Awesome, your total will be $" + str(total)) # we then print the total
    # to the client, along with a phrase. Note that in order to concatenate the
    # total cost to the string, we must first cast that number as a str using the
    # function str() in Python.
    done() # we then call the function done that we implemented before to print
    # Thanks for ordering!

""" We can then call the pizzaPrice() function here so that it executes all of the
    instructions we implemented as part of it. """
pizzaPrice()


# In this case, the function simply calculates values and prints them to the shell.
# However, we can also have a function return a value, so that we can assign that
# value to a variable as follows.
def totalCost(slices, slicePrice): # note that our function has two parameters that
    # we need to populate when we are calling the function
    total = slices * slicePrice # we calculate the total cost of an order here
    return total # we return the total using the return statement. This is different
        # from what was done before, where we could not access the value of the total
        # cost, because it was calculated as part of the function, but not returned to
        # the main script

""" We can then get the total cost by calling the function and assigning it to a
    variable as follows. """
orderTotal = totalCost(3, 1.50) # we are considering 3 slices costing $1.50 each
print(f"Your toal pizza order is ${orderTotal:.2f}.")

'''
C1301 - Day 4 - Functions

What we did last time
1. Data type review
2. More operator examples
3. Functions

What we're doing this time
1. Parameters
    a. Input review
    b. Parameters
    c. Arguments
    d. Miniquiz
2. Return
    a. What is return?
    b. Print vs return
    c. Return exits the function!
    d. Miniquiz
3. Functions you may have worked with
'''

# === Recap: Input

# We can use the builtin input() function to collect user input in order to perform
# an operation. In the following example, we implement a function that takes in
# a value from the user, adds five to it and prints the result.

def add5(): # we define the function without any parameters
    valueAsStr = input('Enter a value: ') # the input will always be stored as str
    value = int(valueAsStr) # in order to perform a math operation we cast it as an int
    print(value + 5) # add 5 to it and print the result

add5() # we call the function to test it out


# === Functions: Parameters

# Instead of collecting user data we can also set up functions such as to take in
# a value as input in our script. To achieve that we make use of parameters. They
# are placed in between paratheses and are used as a variable in the scope of the
# function. Consider the following example, where we have a parameter called number
# to which we will add 10 and print the result.

def add10(number): # we put the parameter in between parentheses in the function definition
    print(number + 10) # we use the parameter as a variable inside our function

add10(5) # we can then call the function passing on a value to the parameter.
# The value that we pass into our parameter when we are calling the function is
# called an argument. In this case our argument is 5. When the function is executed
# the parameter number takes on the value 5 and the function is executed with that
# variable value. So this function call should print 15 on the Python shell

add10(10) # here number will be equal to 10, and this will print 20 to the shell

# We can have more than one parameter by separating them by commas as shown in
# the following function with parameters x and y

def addTwoNums(x, y): # define the function with two params separated by a comma
    print(x + y) # prints the sum of the two parameters

# We pass the arguments in the same order as we defined the parameters. In the
# function call the arguments are x = 2 and y = 7.
addTwoNums(2, 7)

addTwoNums(19, 1) # x = 19 and y = 1

# Don't forget parameters are variables, arguments are values.
'''
f(x) = x + 10
f(5) -> 5 + 10
'''

# It's also important to note that the parameter names exist in the context of the
# function. If we picked variables with the same names as those selected for the
# parameters, the variables will operate as arguments if they are passed into the
# function when they are called as follows.
x = 10
y = 5
addTwoNums(y, x)

# === Functions: Return

# So far, our functions have only displayed values on the shell. This means that
# effectively they did not output any values. Whenever we want a function to output
# a value such that we can collect it inside a variable we use the return statement

# Consider the following example where we define a function that performs a simple
# sum between two numbers.
def addTwoNumsReturn(x, y): # our function is defined with two parameters
    return x + y # in order to output the sum instead of simply printing, we use return

# Let's now call the function with different arguments
first = addTwoNumsReturn(2, 3) # we assign the value returned by the function to
# the variable first. We can print the variable now to see the result.
print(first)
second = addTwoNumsReturn(5, 5) # we assign the value returned by the function to
# the variable second. We can print the variable now to see the result.
print(first + second) # we can use the values now stored in different variables
# to perform operations, for example.

addTwoNums(22, 14) # if we don't assign the function call to a variable, the function
# still outputs the value returned, however, it is not stored anywhere and it also
# will not show on the Python shell.
example_return = addTwoNumsReturn(22, 14)
print(example_return)

# We could create a function to calculate the area of a square that takes as a single
# parameter the side and returns the area
def squareArea(side):
    return side * side

sideLength = 5
area = squareArea(sideLength) # calling the function with the variable sideLength
# as the argument and storing the returned value in the variable area
print(area) # which we can then print

# If a function does not have a return statement in its definition that function
# will return None (of the class NoneType)

# returned value -> None, type (class) -> NoneType

# Notice in this example instead of having a return statement we simply print the
# area as we have done before.
def anotherSquareArea(side):
    print(side*side)

anotherArea = anotherSquareArea(7) # if we assign the function call to our variable
# anotherArea, it will return None (since we did not specify the return statement
# in the function definition)
print(anotherArea)
print(type(anotherArea))

# Another important aspect relating to the return statement is that it will exit
# the function as soon as it is executed. Consider the following example.

def test():
    print('This comes before the return statement!') # we print something
    return 'hello' # we return the string 'hello'
    print('This comes after the return statement!') # we try to print something
    # after the return statement

test() # when we call the function, we notice that the statement before the return
# will show on the shell, but as soon as the function outputs the string 'hello'
# it exits, and whatever other statement comes after that does not get executed

# Some of the Python functions return values while others simply return None.
# let us take a look at some of them.
a = print('test') # this function call will print test on the shell and return None
b = int('2') # this will return the integer corresponding to the string
c = float('2.0') # this will return the float corresponding to the string
d = bool(2) # this will return a boolean
e = type(2.0) # the type function returns the class of the object

# Sometimes we call functions that return a value other than None, "fruitful functions"

# Finally, we can use calls to other functions inside our function definition.
# Consider the following example where we want to calculate the total area of a
# snowmam's body in a drawing. The snowman is composed of three circles of different
# radii.

# We first define a function that computes the area of a circle as follows
def calculateArea(r): # our only parameter will be the radius
    return 3.14 * r ** 2 # note that we are returning the area here

# We then write our function for the snowman, with three different radii as the
# parameters for the function
def snowmanArea(smallRadius, medRadius, bigRadius):
    # we calculate the area for each circle, by calling our previously defined
    # calculateArea function passing the parameters from snowmanArea as arguments
    # to the calculateArea function calls as follows
    smallArea = calculateArea(smallRadius)
    medArea = calculateArea(medRadius)
    bigArea = calculateArea(bigRadius)
    return smallArea + medArea + bigArea # we return the total area

totalArea = snowmanArea(2, 5, 10)
print(totalArea * 2)


""" FILE NAME: 03code.py
    STUDENT:
    DESCRIPTION: Call the two listed functions Example 1 then Example 2.
    Use the Python Debuffer to fix the errors.
    1. Run your program
    2. Run the Shell, select the Debug menu, then click Debugger. The Debug Contrrol window will open.
    3. In the Editer set breakpoints you might have
    
"""
"""
DESCRIPTION: Example 1
    This program runs with out errors
    output:
    inner: 2 2
    outer: 1
"""
def outer(): # function definition outer
    x = 1
    def inner(): # function definition inner
        x = 2  
        y = x
        print("inner:", x, y)
    inner() # function call inner
    print("outer:", x)

##outer() # function call outer

    
def main():
    """ function documentation: input, output, purpose """
    # call to the solution functions
    outer()

if __name__ == '__main__':
    main()
    


"""
DESCRIPTION: Example 2
    Create a function with the listed statemensts.
    Correct all errors all errors to
    display to correct output.
    output:
        Hello, Buzz and Uga!
"""
##greeting = "Hello,"
##
##name1 = input("Enter your name: ")
##
##name2 = input("Enter another name: ")
##
##phrase = f"{greeting} {name1} and {nam2}.'
##print(res)


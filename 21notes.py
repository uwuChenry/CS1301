"""
# Day 21 notes - File I/O (Chapter 13)

=== What we are doing today ===
1. opening and closing a file
2. reading from files - 3 ways
    a) reading the entire file into a single large string using myfile.read()
    b) reading only one line from the file into a string myfile.readline()
    c) reading the entire file into a list of strings myfile.readlines()

"""

 # === Opening, reading and closing a file
# The first step in being able to read data from a text file is to create an IO
# wrapper object by opening the file using the function open(). Note that to be
# able to read it, we need to pass both the file name as the first parameter, as
# well as the "r" as the second parameter. The string with the "r" indicates that
# we are opening the file in read mode (input) as opposed to writing mode (output)

myfile = open("day21limerick.txt","r")
print(myfile) # this line will not print the text inside the file, it will print
# the name of the IO wrapper object
print(type(myfile)) # this will reveal that the variable type returned by the open
# function is an IO wrapper
text = myfile.read() # to read the entirety of the text contained in myfile into
# a single string, we call the method .read() on the file IO wrapper object.
myfile.close() # it is very important that we close the file as soon as we have
# extracted the information we want from it my calling the .close() method. That
# is because the file cannot be accessed by others while it is open, so we want
# to close it as soon as we no longer need to have it open so that others can
# use it if they need to.
print(text) # this will print the actual text that was inside of the file as a
# single string
print(len(text)) # this should give us the number of characters in the string.
# notice that the escape sequence that we use to skip to the next line "\n" is
# counted as a single character.

print("\n")

# === Reading the file one line at a time
# In the above example, we read the contents of "day21limerick.txt" into a single
# string, using the .read() method. That is one way you may decide to read the
# data from a file. You may however, prefer to read the file line by line instead
# perhaps because the file is too large and you are only concerned with a specific
# portion of it. For that we can use the method .readline(). Let's look at some
# examples with it's usage

# first we open the file using the open function. Don't forget to add the "r" as
# the second parameter to indicate we want to READ our file, not write on it.
myfile = open("day21limerick.txt","r")
# we can read the first line by using .readline() as follows
aline = myfile.readline() # aline will be a string containing the text of the 1st
# line in your text file.
bline = myfile.readline() # bline will be a string containing the text of the 2nd
# line in your text file. This is possible because our IO wrapper has a builtin
# cursor. This cursor keeps track of what it has already read and what is the next
# line in our text file. We will explore this further in the next examples
myfile.close() # let's not forget to close the file!
# let us now print what we read from the file
print(aline) # this should print the first line
print(bline) # this should print the second line

print("\n")

# === Understanding how the cursor works
# Let's consider another example to explore how the cursor works. Here we will
# use a for-loop to read three times out of our file
myfile = open("day21limerick.txt","r") # we open the file in read mode
for i in range(3): # we have our for-loop
    someline = myfile.readline() # we read someline using .readline(). Since the
    # wrapper keeps track of where we are on the text file, for every time we call
    # myfile.readline() we get a string for the following line. Let's verify that
    # this is true by adding a print statement in the following.
    print(someline)
myfile.close() # don't forget to close the file!!
print(someline) # this will print the last line that we read
print(len(aline)) # and this will print the number of characters counting "\n" as 1

# The above example shows that as long as you keep the file open, the cursor will
# stay active and we will keep track of what line we are on the file. However, as
# soon as we close the file, it forgets where the cursor was, and if you reopen
# the file, we will be back to the very top again. Let's see if this is true with
# the following example.

print("\n")
# we are going to execute this three times
for i in range(3):
    myfile = open("day21limerick.txt","r") # open the file in read mode
    aline = myfile.readline() # read a line from the file using .readline()
    myfile.close() # close the file
print(aline) # this will print the first line. That's because in our loop we open
# and close the file everytime we use the .readline(). This means that the cursor
# is reset every time.

print("\n")
# === Reading the file as a list of strings
# One other way that you may consider reading a file is using the method
# .readlines() (note the "s" at the end, that differentiates it from .readline())
# This method will read each line in the file into a string and store this
# collection of strings into a list, such that you have ["1st line", "2nd line", ...]

myfile = open("day21limerick.txt","r") # open the file in read mode with "r"
all_lines = myfile.readlines() # this will return a list of strings in which each
# line will be a string.
myfile.close() # since we read the data out, we can close the file
print(all_lines) # we can print this list of strings
print(all_lines[0]) # or since the lines are stored sequentially on the list, you
# could print the line that you want using list indexing. Here we are printing
# only the first line.

print("\n")
# === Application example
# Let's write a function to search for the first time that a word occurs in a file
# and return what line that word is on. Let's try it with the Alice in Wonderland
# book and let's search for the word rabbit.

def search_word(filename, word):
    # we first open the file in readmode
    myfile = open(filename,"r")
    # because we don't know how many lines we are going to have in our file, it
    # is best to use a while loop, instead of a for loop. That's because if we
    # use a for-loop we would have to know when to stop executing, but here we
    # can have a boolean variable that we store whether we have found the word
    # or not.
    not_found = True # we haven't searched for the word yet so it is not found
    # since we want to return what line the word appears for the first time, we
    # also need a counter.
    counter = 0
    # our while loop that is going to go through the file. We use .readline() here
    # The reason for that is threefold: (1) if we use .read(), we'd have a single
    # string and would have to split it on "\n" and then parse through the list
    # until we get to the first appearance of the word. (2) if we use .readlines()
    # we will not need to split anything, since we will get a list of lines already
    # but we will have read the entire file into memory, while all we really want
    # is the first time something shows up, so it would be a waste to read the
    # entire file into memory, if the word showed up of the first few lines of text
    while not_found:
        aline = myfile.readline() # reading a single line
        if word in aline: # we check if the word that we are looking for is in
        # the string containing the line
            not_found = False # if we found the word, we change our boolean variable
            # so that the while loop is stopped
        else:
            counter +=1 # if we have not found the word just yet, we add 1 to the
            # line counter.
    myfile.close() # we close our file when we are done with our search loop
    return counter # we return the line number

# let's see if it works!
line_w_rabbit = search_word("day21alice.txt", "rabbit") # execute function
print(line_w_rabbit) # print the number of the line containing "rabbit"

# just to check whether we are correct, let's read all of the lines into a list
# using .readlines() and print the line that we found
myfile = open("day21alice.txt","r") # open the file in read mode
all_lines = myfile.readlines() # get list of strings containing each line
myfile.close() # close the file!
print(all_lines[line_w_rabbit]) # see if that line contains the word rabbit

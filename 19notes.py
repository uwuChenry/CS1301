"""
# Day 19 - more dictionary practice

=== What we are doing today ===
1. using len to get the length of the items
2. more dictionary practice

"""

# === Refresher on dictionaries
# in this example we want to sum up all of the streams the
# pop musician Doja Cat has for her songs
doja_dict = {'Say So':3000000000,'Kiss me more': 4000000000}
print(doja_dict['Say So']) # we use the name of the song, as
# the key of the dictionary and access the number of streams
# by calling the dictionary[key] to get the value

total_streams = 0 # initialize a total streams = 0
# since we are only interested in the number of streams we can
# loop through dictionary.values()
for val in doja_dict.values(): 
    total_streams += val # add the value from the dict to total
print(total_streams) # print the total number of streams

# another way of looping through dictionaries is the following
for song in doja_dict: # this will always loop through the keys
    print(song)  # song is the key in our dictionary where {song: number_of_streams,...}
print(len(doja_dict)) # this will print the number of items (key:value pair) in the dictionary

# we can also use functions as our key or value in the dictionary
import math
# the following gives us a dictionary in which one of the keys is the sqrt(23) and
# its corresponding value is int(sin(pi)), and another item, where the key is "CATS" and
# corresponding value 57.
function_dict = {math.sqrt(23): int(math.sin(math.pi)), "cats".upper():57}
print(function_dict)

# in the following case, since the print function returns None, and the
# dictionary stores only the last assignment when you use the same key
# multiple times, you will only have two items {None:57, "dogs":237}
function_dict = {print('Hello'):23,print('Goodbye'):57, "DOGS".lower():237}
print(function_dict)


# === Extracting information from dictionaries
import string

# Example 1: given a string, let us build a dictionary in which the letter is
# the key and the corresponding value is the position of the last occurrence
# of that letter in the string
phrase = "Y'all are great students!".lower() # our phrase, which we put in lowercase
# to make our life easier
letter_dict = {} # we initialize an empty dictionary in which we will store things
# since we want to store the position of the letter, we take advantage of enumerate
# because it gives us a pair containing both the index in the string and the char
for index, char in enumerate(phrase):
    if char in string.ascii_letters: # we only want the letters, ignoring the special characters
        letter_dict[char] = index # add to dict by calling dict[key] = value
# notice that here we took advantage of the fact that the dictionary stores only the
# last value assignment if the key is already in the dictionary
print(letter_dict)


# Example 2: given a string, let us build a dictionary in which the letter is
# the key and the corresponding value is the number of times the letter shows
# up on that string (i.e. the absolute frequency)
phrase = "Y'all are great students!".lower()
freq_dict = {}
# since we don't care about the position of the letters anymore, we don't need
# to enumerate, and can loop directly over the string
for char in phrase:
    if char in string.ascii_letters: # again, we only want letters no special chars
        if not char in freq_dict: # if the char is NOT in the dict, we need to add it with a value of 1
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1 # if it's already in the dict, we just add 1 to it
print(freq_dict)

# Example 3: given a dictionary of products that contain a key = product name and
# value = (quantity, price). Put together a list of items that need to be reordered
prod_dict = {"gloves":(0, 20.0),"masks":(0, 30.0),"gauze":(300, 2.0)}
reorder_list = [] # list for the products that need to be reordered
# looping through the keys in the product dictionary, which in this case are the
# product names
for key in prod_dict:
    # we use tuple unpacking, by getting the value associated with the key, using dict[key]    
    (qty, price) = prod_dict[key]
    if qty == 0: # we are going to reorder only products that are out of stock
        reorder_list.append(key) # add them to our reordering list
print(reorder_list)

# Example 4: we want to get the total number of countries that can produce semiconductors
# we start out with a dictionary where the key is a product code and the value are lists
# of countries that can produce that prod
elec_countries = {"sc23":["USA","ITA","FRA"], "sc56": ["CAN", "CHN"], "jk78":["BRA"]}
sc_world = 0 # number of countries that can produce products that start with "sc"
for key in elec_countries: # loop through the keys in the dictionary
    if "sc" in key: # check if the product name contains "sc"
        sc_world += len(elec_countries[key]) # store the size of the list of countries
print(sc_world)

# Example 5: we want to put together a list of tasks that need to be completed today
# and the total amount of hours that need to be spent completing those tasks. We start
# with a dictionary in which the key is a tuple containing the task and how many days
# until the deadline. Items that are past due (negative days until deadline) need to be
# completed today. The value associated withe the key is the required number of hours
# to complete it.
todo_dict = {("poster",-2):4.0,("email",3):0.50,("paper",-1):10.0}
total_hrs = 0 # number of hours we will need to work today
list_task = [] # list of tasks that need to be completed
for key in todo_dict: # loop through the keys
    (task, days_to_dealine) = key # unpack the key, using tuple assignment
    if days_to_dealine < 0: # only consider tasks that are past due
        list_task.append(task) # add the task to the list
        total_hrs += todo_dict[key] # sum up the hours to the total number of hours
print(list_task)
print(total_hrs)

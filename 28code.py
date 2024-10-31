"""
# Day 28 - using web APIs
"""

"""
What does the code snipet do?

"""
###
##import requests
##
##r = requests.get("https://restcountries.com/v2/regionalbloc/eu")
###
##data = r.json()
###
##if type(apiData) == list:  
##    apiDatadict = apiData[0]    # 
##elif type(apiData) == dict:
##    apiDatadict = apiData       # 
###
##print(type(data))
###
##pprint(data[0])   
###
##print(type(data[0]))
###
##print(data[0].keys())
###
##print(data[0]["population"])
###
##for num in range(len(data)):
##    print(data[num]["population"])
##

# === Sending multiple requests
# We can also use the idea of the base_url+something_specific to send multiple requests
# to a web API to collect information we know is stored in a sequence.
"""
baseUrl = 'https://pokeapi.co/api/v2/pokemon/'
"""

'''
# Example: Write a function that takes as input a base url
# and finds the name and weight of the heaviest Pokemon out
# of the first 100 available in the api.
'''
def heavyPoke(baseUrl):
    try:
        import requests
        from pprint import pprint
    except:
        print(f"Failed get request: {ur}")
    else:
        maxWeight = 0
        maxName = ""
        # make requests for first 100 Pokemon by {id} number
        for index in range(1,101):
            # need to build a full url every request
            url = baseUrl + str(index)
            r = requests.get(url)
            
            # unpack the data to Python data structure
            if type(r.json()) == list:
                data = r.json()[0]
            else:
                data = r.json()
            name = data["name"]
            weight = data["weight"]
            
            # keep track of the heaviest poke I've seen so far and their weight
            if weight > maxWeight:
                maxWeight = weight
                maxName = name
                
        return (maxName,maxWeight)
##    
##baseUrl = "https://pokeapi.co/api/v2/pokemon/"
##name,weight = heavyPoke(baseUrl)
##print(f"The heavy Poke {name} weights {weight} hectograms.") # weight measurement from Pokemon (type) documentation


'''
# Example: Write a function to print
# the name, weight and height for the first 20 Pokemon in the PokeAPI
'''
def pokeStats():
    try:
        import requests
        from pprint import pprint
    except:
        print(f"Failed get request: {ur}")
    else:
        print("name\tweight\theight") # printing a tab separated header just so it looks pretty

        baseUrl = "https://pokeapi.co/api/v2/pokemon/" # our base url
        for index in range(1,21):   # the range function generates id numbers between 1 and 20.
            full_url = baseUrl + str(index) # we add on the str(number) to our base url
            r = requests.get(full_url)       # and make a request using the .get(url) method
            data = r.json()                  # unpack the response into a python data structure using .json()
            # In this case, we know that the data will be a dictionary with the Pokemon
            # attributes as keys and their corresponding values. If you are not sure for a
            # different web API, you should read their documentation or print type(data) so
            # you know whether you are working with a list of dicts or a dict or a dict of dicts
            
            # accessing the attributes by the keys and printing them
            print(data["name"]+"\t"+str(data["weight"])+"\t"+str(data["height"]))

##    
##pokeStats()

'''
# Example: OpenCV to display images
# Get Random Images API for free from Lorem Picsum (https://picsum.photos)
# Just add your desired image size (width & height) after our URL, and you'll get a random image.

'''
import requests
## For a square image, just add the size:
image_url = 'https://picsum.photos/200'
response = requests.get(image_url, stream=True)
image_filename = image_url.split('/')[-1]
if response.status_code:
   with open(image_filename, 'wb') as image:
       image.write(response.content)

import cv2
img_path = cv2.imread(image_filename, cv2.IMREAD_COLOR) 
cv2.imshow(image_url, img_path)
cv2.waitKey(0)
cv2.destroyAllWindows()

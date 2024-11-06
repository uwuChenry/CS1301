"""
Georgia Institute of Technology - CS1301
Homework 8 -  APIs
"""

#########################################

"""
Function Name: findReleaseDate()
Parameters: song (`str`)
Returns: releaseDate (`str`)
"""
import requests as r


def findReleaseDate(song):
    url = "https://taylor-swift-api.sarbo.workers.dev/songs"
    url2 = "https://taylor-swift-api.sarbo.workers.dev/albums"
    response = r.get(url)
    albumID = 0
    if response.status_code == 200:
        data = response.json()
        # print(data)
    # else:
    #     # print("req failed")
    #     return "Still writing our song..."
    if type(data) == type([]):
        for thing in data:
            if thing["title"] == song:
                albumID = thing["album_id"]
    else:
        return "Still writing our song..."
    response2 = r.get(url2)
    if response2.status_code == 200:
        data2 = response2.json()
    # else:
    #     return "Still writing our song..."
    if type(data2) == type([]):
        for thing in data2:
            if thing["album_id"] == albumID:
                # print(thing["release_date"])
                return thing["release_date"]
    return "Still writing our song..."
    pass


# print(findReleaseDate("Red Wine Supernova"))

#########################################

"""
Function Name: longestSong()
Parameters: albumID (int)
Returns: longest (str)
"""

def longestSong(aid):
    url = "https://taylor-swift-api.sarbo.workers.dev/albums/" + str(aid)
    response = r.get(url)
    temp = []
    if aid <= 0 or aid >= 12:
        return "Let's listen to something else."
    if response.status_code == 200:
        data = response.json()
    else:
        return "Let's listen to something else."
    
    for thing in data:
        url2 = "https://taylor-swift-api.sarbo.workers.dev/lyrics/" + str(thing["song_id"])
        response2 = r.get(url2)
        lyrics = response2.json()
        words = lyrics["lyrics"]
        a = words.split(" ")
        if len(a) * 1.5 >= 600:
            temp.append((len(a)*1.5, thing["title"]))
    for thing in temp:
        print(f"{thing[1]} would be a good choice...")
    temp.sort()
    # print(temp)
    if temp == []:
        return "Let's listen to something else."
    return f"{temp[-1][1]}, {round((temp[-1][0]//60), 2)} mins and {round((temp[-1][0]%60), 2)} secs"
    pass

# for i in range (1, 12):
#     print(i)
#     print(longestSong(i))
# print(longestSong(11))

#########################################

"""
Function Name: lyricFinder()
Parameters: lyricList (list), album (str)
Returns: songList (str)
"""

def lyricFinder(llist, astr):
    url = "https://taylor-swift-api.sarbo.workers.dev/albums"
    response = r.get(url)
    aid = -1
    temp = []
    data = response.json()
    for thing in data:
        if thing["title"] == astr:
            aid = thing["album_id"]
    if aid == -1:
        return "That's not a Taylor album!"
    url2 = "https://taylor-swift-api.sarbo.workers.dev/albums/" + str(aid)
    re = r.get(url2)
    data2 = re.json()
    for thing in data2:
        a = ("https://taylor-swift-api.sarbo.workers.dev/lyrics/" + str(thing["song_id"]))
        re3 = r.get(a)
        lyrics = re3.json()
        count = 0
        for things in llist:
            #print(lyrics["lyrics"].count(things))
            if lyrics["lyrics"].lower().count(things.lower()) >= 1:
                count += 1
        if count != 0:
            temp.append((count, lyrics["song_title"]))

    temp.sort()
    temp.reverse()
    print(temp)
    return temp
    pass

# lyricFinder(['America', 'darling', 'street', 'heartbreak'], 'Lover')
# lyricFinder(["perfectly fine", "in the rain"], "Fearless")

# lyricFinder(["your eyes", "reputation", "I know"], "Reputation")

#########################################

"""
Function Name: playlistOrganizer()
Parameters: albumList (list), leastFavoriteSongs (list)
Returns: playlistDict (dict)
"""

def playlistOrganizer(alist, lflist):
    url = "https://taylor-swift-api.sarbo.workers.dev/albums"
    response = r.get(url)
    ids = []
    temp = []
    out = {}
    if response.status_code == 200:
        data = response.json()
    # else:
    #     print("nima")
    for thing in data:
        if thing["title"] in alist:
            ids.append((thing["album_id"], thing["title"]))
    for i, t in ids:
        a = ("https://taylor-swift-api.sarbo.workers.dev/albums/" + str(i))
        re = r.get(a)
        count = 0
        for songs in re.json():
            if songs["title"] in lflist:
                count += 1
        liked = len(re.json()) - count
        temp.append((liked, t)) 
    # print(temp)
    for num, name in temp:
        if num in out.keys():
            out[num].append(name)
        else:
            out[num] = [name]
    for things in out.values():
        things.sort()
    print (out)
    return out
    pass
playlistOrganizer(['Folklore', '1989', 'Speak Now', 'Lover', 'Fearless'], ['Innocent', 'Mean', 'The Man'])
# albumList = ["1989", "Red", "Evermore"]
# leastFavoriteSongs = ["happiness", "Blank Space", "right where you left me",  "evermore", "coney island", "gold rush", "ivy"]
# playlistOrganizer(albumList, leastFavoriteSongs)

#########################################

"""
Function Name: favAlbum()
Parameters: album (str)
Returns: None (NoneType)
"""
# import csv

def favAlbum(astr):
    url = "https://taylor-swift-api.sarbo.workers.dev/albums"
    response = r.get(url)
    aid = -1
    temp = []
    temp.append(("Song ID", "Song Name", "# Song Title Mentions"))
    if response.status_code == 200:
        data = response.json()
    for thing in data:
        if thing["title"] == astr:
            aid = thing["album_id"]
    if aid == -1:
        return
    url= "https://taylor-swift-api.sarbo.workers.dev/albums/" + str(aid)
    re = r.get(url)

    for thing in re.json():
        count = 0
        a = "https://taylor-swift-api.sarbo.workers.dev/lyrics/" + str(thing["song_id"])
        re2 = r.get(a)
        words = re2.json()["lyrics"].lower()
        title = thing["title"].replace(",", "")
        count = words.count(title.lower())
        # print(thing["title"].replace(",", "").replace("\'", "").replace("\\","").replace("…","").replace("?","").lower())
        # print(words)
        temp.append((thing["song_id"], title, count))

    with open("album.csv", "w", newline='') as file:
        first = True
        for i in range(len(temp)):
            if not first:
                file.write(f"\n")
            if first:
                first = False
            file.write(f"{temp[i][0]}, {temp[i][1]}, {temp[i][2]}")


# favAlbum("Midnights")
#########################################

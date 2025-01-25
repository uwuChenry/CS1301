import requests


def countPlanets():
    baseUrl = "https://swapi.dev/api/planets/"
    count = 0
    for i in range(1, 11):
        realUrl = baseUrl + str(i)
        r = requests.get(realUrl)
        if int(r.json()["diameter"]) > 10000:
            count += 1
    #     print(r.json())
    # print(count)
    return count

# countPlanets()
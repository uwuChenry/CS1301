

def fancyGrid(a):
    r = []
    c = [0, 0, 0]
    for things in a:
        r.append(things[0]+things[1]+things[2])
        c[0]+= things[0]
        c[1]+= things[1]
        c[2]+= things[2]
    
    print(r)
    print(c)
    if r != c or r[0]!=r[1] or r[0]!=r[2]:
        return False
    else:
        return True
pass


# grid1 = [ [4, 9, 2],
#               [3, 5, 7],
#               [8, 1, 6] ]
# print(fancyGrid(grid1))
#                  # All rows and columns add up to 15

# grid2 = [ [4, 9, 2],
#               [3, 4, 7],
#               [8, 1, 6] ]

# print(fancyGrid(grid2))

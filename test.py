import re

def sentenceFixer(a):
    out = ""
    for ch in a:
        if ch.isdigit():
            continue
        out += ch
    arr = []
    arr = re.split('#| $ |%', out)
    for thing in arr:
        if thing == "":
            continue
        print(thing+".")
pass


sentenceFixer("I wil3l th2ing as234df dfs a sd f#i shoul4d not h5ave s23omething%bla bla bal$")



t1 = (1,2)

t2 = t1 + (5,6)

t3 =( t1 + t2) * 2

print(len(t3))

t1 = (1,2)

t2 = t1 + (5,6)

t3 = t2 + t1

print(t3.count(1))
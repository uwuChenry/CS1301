def updatePrices(a, b):
    for things in b:
        if things[0] in a.keys():
            a[things[0]] -= things[1]
            a[things[0]] = round(a[things[0]], 2)
    return a

bakeryDict = {'muffin': 3.99, 'roll': 1.99, 'croissant': 4.99, 'bagel': 2.99}
discounts = [('muffin', 3.99), ('bagel', 1.00)]
print(updatePrices(bakeryDict, discounts)) # should print {'muffin':0.0, 'roll':1.99, 'croissant':4.99, 'bagel':1.99}

chicFilADict = {'fries': 3.99, 'Spcy Chkn': 7.99, 'MlkShk CnC': 4.99}
discounts = [('Spicy Chicken', 8.99), ('fries', 0.99)]
print(updatePrices(chicFilADict, discounts)) # should print {'fries' : 3.0, 'Spcy Chkn': 7.99, 'MlkShk CnC': 4.99}

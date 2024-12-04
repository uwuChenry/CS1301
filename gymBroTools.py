def plateCalculator(weight):
    ret = []
    if weight > 645:
        print("bro you really trying to lift this much weight??")
        return ()
    if weight % 5 != 0:
        print("good luck finding those weights.")
        return ()
    weight -= 45
    if weight > 0:
        
        count = 0
        num45 = (weight // 45)
        for i in range(num45):
            count += 1
            ret.append("45")
            if count == 5:
                break
            
        weight -= 45 * count

        count = 0
        num35 = (weight // 35)
        for i in range(num35):
            count += 1
            ret.append("35")
            if count == 5:
                break
            
        weight -= 35 * count

        count = 0
        num25 = (weight // 25)
        for i in range(num25):
            count += 1
            ret.append("25")
            if count == 5:
                break
            
        weight -= 25 * count

        count = 0
        num10 = (weight // 10)
        for i in range(num10):
            count += 1
            ret.append("10")
            if count == 5:
                break
            
        weight -= 10 * count

        count = 0
        num5 = (weight // 5)
        for i in range(num5):
            count += 1
            ret.append("5")
            if count == 5:
                break
            
        weight -= 5 * count
    ret = tuple(ret)
    return ret


    

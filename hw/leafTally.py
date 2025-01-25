def leafTally(leaflist):
    score = 0
    for leaf in leaflist:
        if leaf in "rR":
            score += 50
        if leaf in "yY":
            score += 25
        if leaf in "Oo":
            score += 10
    return score

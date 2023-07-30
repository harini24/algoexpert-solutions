def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    indOne=0
    indTwo=0
    smallestDiff=float("inf")
    currDiff=float("inf")
    pair=[]
    while  indOne<len(arrayOne) and indTwo<len(arrayTwo):
        one=arrayOne[indOne]
        two=arrayTwo[indTwo]
        if one < two:
            currDiff = two - one
            indOne+=1
        elif one > two:
            currDiff =  one - two
            indTwo+=1
        else:
            return [one,two]

        if currDiff<smallestDiff:
            smallestDiff=currDiff
            pair=[one,two]

    return pair
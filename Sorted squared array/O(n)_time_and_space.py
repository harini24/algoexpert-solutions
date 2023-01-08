def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]
    smallerInd = 0
    largerInd = len(array)-1
    for ind in reversed(range(len(array))):
        smallerVal = array[smallerInd]
        largerVal = array[largerInd]
        if abs(smallerVal) > abs(largerVal):
            sortedSquares[ind] = smallerVal*smallerVal
            smallerInd+=1
        else:
            sortedSquares[ind] = largerVal*largerVal
            largerInd-=1
    return sortedSquares

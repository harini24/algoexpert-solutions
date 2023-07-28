def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return helper(arrayOne,arrayTwo,0,0,float("-inf"),float("inf"))


def helper(arrayOne,arrayTwo,rootOne,rootTwo,minVal,maxVal):
    if rootOne==-1 or rootTwo==-1:
        return rootOne == rootTwo
    if arrayOne[rootOne] != arrayTwo[rootTwo]:
        return False

    arrayOneSmaller = getSmallerInd(arrayOne,rootOne,minVal,maxVal)
    arrayTwoSmaller = getSmallerInd(arrayTwo,rootTwo,minVal,maxVal)
    arrayOneGreater = getgreaterInd(arrayOne,rootOne,minVal,maxVal)
    arrayTwoGreater = getgreaterInd(arrayTwo,rootTwo,minVal,maxVal)

    leftAreSame = helper(arrayOne,arrayTwo,arrayOneSmaller,arrayTwoSmaller,minVal,arrayOne[rootOne])
    rightAreSame = helper(arrayOne,arrayTwo,arrayOneGreater,arrayTwoGreater,arrayOne[rootOne],maxVal)

    return leftAreSame and rightAreSame
def getSmallerInd(array,start,minVal,maxVal):
    for i in range(start+1,len(array)):
        if array[i]<array[start] and array[i] >=minVal:
            return i
    return -1

def getgreaterInd(array,start,minVal,maxVal):
    for i in range(start+1,len(array)):
        if array[i]>=array[start] and array[i]<maxVal:
            return i
    return -1
    
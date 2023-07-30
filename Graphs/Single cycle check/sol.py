# O(n) time and O(1)space

def hasSingleCycle(array):
    # Write your code here.
    currInd=0
    visited=0
    while visited<len(array):
        print(currInd)
        if visited>0 and currInd==0: return False
        visited+=1
        currInd = calculateCurrInd(currInd,array)

    return currInd==0

def calculateCurrInd(currInd,array):
    jump=array[currInd]
    newInd=(currInd+jump)% len(array)
    return newInd if newInd>=0 else newInd+len(array)
    
def binarySearch(array, target):
    # Write your code here.
    return findTerm(array,target,0,len(array)-1)

def findTerm(array,target,start,end):
    if end<start: return -1
    midInd=(start+end)//2
    if array[midInd] == target: return midInd
    elif array[midInd] > target: return findTerm(array,target,start,midInd-1)
    else: return findTerm(array,target,midInd+1,end)
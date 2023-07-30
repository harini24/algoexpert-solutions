def subarraySort(array):
    # Write your code here.
    maxOutOfRange=float("-inf")
    minOutOfRange=float("inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i,num,array):
            minOutOfRange=min(minOutOfRange,num)
            maxOutOfRange=max(maxOutOfRange,num)
    if minOutOfRange==float("inf"): return [-1,-1]

    leftInd=0
    while minOutOfRange >= array[leftInd]:
        leftInd+=1
    rightInd=len(array)-1
    while maxOutOfRange <= array[rightInd]:
        rightInd-=1
    return [leftInd,rightInd]
def isOutOfOrder(ind,val,array):
    if ind==0:
        return val > array[ind+1]
    if ind == len(array)-1:
        return val<array[ind-1]
    return val>array[ind+1] or val<array[ind-1]
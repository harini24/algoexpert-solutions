def binarySearch(array, target):
    start=0
    end=len(array)-1
    while end>=start: 
        midInd=(start+end)//2
        if array[midInd] == target: 
            return midInd
        elif array[midInd] > target: 
            end=midInd-1
        else: 
            start=midInd+1
        print(start,end)
    return -1
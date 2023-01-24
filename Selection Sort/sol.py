# O(n*n) time and O(1) space

def selectionSort(array):
    # Write your code here.
    startInd=0
    while startInd<len(array)-1:
        minInd=startInd
        for i in range(startInd+1,len(array)):
            if array[minInd]>array[i]:
                minInd=i

        array[minInd],array[startInd]=array[startInd],array[minInd]

        startInd+=1
    return array

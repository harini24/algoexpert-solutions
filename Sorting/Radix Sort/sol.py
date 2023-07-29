# O(d*(n+b)) time and O(n+b) space
# n - length of input array
# b - base
# d - number of digit in max val
def radixSort(array):
    # Write your code here.
    if len(array) <2: return array
    maxNumber = max(array)
    digit = 0
    
    while maxNumber//(10**digit) >0:
        countSortBasedonDigit(array,digit)
        digit += 1
    return array

def countSortBasedonDigit(array,digit):
    countArr=[0]*10
    sortedArr = [0]*len(array)
    
    digitCol=10**digit
    for val in array:
        ind = (val//digitCol)%10
        countArr[ind]+=1

    for i in range(1,10):
        countArr[i]+= countArr[i-1]

    for i in range(len(array)-1,-1,-1):
        val = (array[i]//digitCol)%10        
        countArr[val]-=1
        sortedInd = countArr[val]
        sortedArr[countArr[val]] = array[i]

    for i in range(len(array)):
        array[i]=sortedArr[i]
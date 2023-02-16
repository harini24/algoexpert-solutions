def isMonotonic(array):
    # Write your code here.
    nonIncreasing=True
    nonDecreasing=True
    for  i in range(len(array)-1):
        if array[i] < array[i+1]:
            nonIncreasing=False
        if array[i] > array[i+1]:
            nonDecreasing=False
        
    return nonDecreasing or nonIncreasing
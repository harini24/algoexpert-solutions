def firstDuplicateValue(array):
    # Write your code here.
    for val in array:
        absVal= abs(val)
        if array[absVal-1] < 0: return absVal
        array[absVal-1] *= -1
    return -1
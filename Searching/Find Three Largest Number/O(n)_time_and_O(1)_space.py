def findThreeLargestNumbers(array):
    # Write your code here.
    max = secMax = thirdMax = float('-inf')
    for val in array:
        if val>max:
            thirdMax=secMax
            secMax=max
            max=val
        elif val>secMax:
            thirdMax=secMax
            secMax=val
        elif val>thirdMax:
            thirdMax=val
    return[thirdMax,secMax,max]
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left =0
    right = len(array) - 1
    while left<right:
        currentSum = array[left]+array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum<targetSum:
            left+=1
        else:
            right-=1
    return []
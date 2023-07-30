def twoNumberSum(array, targetSum):
    # Write your code here.
    nums={}
    for i in array:
        potentialSum = targetSum-i
        if potentialSum in nums:
            return [i,potentialSum]
        else:
            nums[i]=True
    return []
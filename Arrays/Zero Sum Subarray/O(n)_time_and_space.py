def zeroSumSubarray(nums):
    # Write your code here.
    sums=set([0])
    currSum=0
    for val in nums:
        currSum+=val
        if currSum in sums: return True
        sums.add(currSum)
    return False

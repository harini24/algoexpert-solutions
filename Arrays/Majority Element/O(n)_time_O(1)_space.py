def majorityElement(array):
    # Write your code here.
    majorityEle=None
    majorityEleCount=0
    for val in array:
        if majorityEleCount == 0:
            majorityEle=val
            majorityEleCount += 1
        elif val == majorityEle:
            majorityEleCount += 1
        else:
            majorityEleCount -= 1
    # c=0
    # for val in array:
    #     if majorityEle == val:
    #         c+=1
    return majorityEle
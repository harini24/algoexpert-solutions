def longestPeak(array):
    # Write your code here.
    ans=0
    for i in range(1,len(array)-1):
        isPeak = array[i]>array[i-1] and array[i]>array[i+1]
        if not isPeak:
            continue
        left=i-2
        right=i+2
        while left>=0 and  array[left]<array[left+1]:
            left-=1
        while right<len(array) and array[right]<array[right-1]:
            right+=1

        # print(array[i],)
        currLength=right-left-1
        if currLength>ans:
            ans=currLength
        i=right
    return ans
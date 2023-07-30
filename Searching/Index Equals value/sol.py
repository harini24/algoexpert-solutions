def indexEqualsValue(array):
    # Write your code here.
    start=0
    end=len(array)-1
    ans=-1
    while start<=end:
        mid=(start+end)//2
        if array[mid]==mid:
            ans=mid
            end=mid-1
        elif array[mid] <mid:
            start=mid+1
        else:
            end=mid-1
    return ans
        

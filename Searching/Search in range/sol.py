def searchForRange(array, target):
    # Write your code here.
    fo=-1
    lo=-1
    start=0
    end =len(array)-1
    while start <=end:
        mid=(start+end)//2
        if array[mid] == target:
            fo=mid
            end=mid-1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    start=0
    end =len(array)-1
    while start <=end:
        mid=(start+end)//2
        if array[mid] == target:
            lo=mid
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return [fo,lo]
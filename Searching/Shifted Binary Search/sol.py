def shiftedBinarySearch(array, target):
    # Write your code here.
    start=0
    end= len(array)-1
    while start<=end:
        print(start,end)
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[start]>array[mid]:
            if target>=array[mid] and target<=array[end]:
                start=mid+1
            else:
                end=mid-1
        else:
            print("here")
            if target<=array[mid] and target>=array[start]:
                end=mid-1
            else:
                start=mid+1
    return -1
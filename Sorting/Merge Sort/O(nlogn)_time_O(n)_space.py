def mergeSort(array):
    # Write your code here.
    mergeSortHelper(array,0,len(array)-1)
    return array

def mergeSortHelper(array,start,end):
    if start == end: return
    mid = (start+end) // 2
    mergeSortHelper(array,start,mid)
    mergeSortHelper(array,mid+1,end)
    merge2Arr(array,start,end,mid+1)
    return

def merge2Arr(arr,start,end,mid):
    i=start
    j=mid
    ret=[]
    while i<mid and j<=end:
        if arr[i]<arr[j]:
            ret.append(arr[i])
            i+=1
        else:
            ret.append(arr[j])
            j+=1
    while i<mid:
        ret.append(arr[i])
        i+=1
    while j<=end:
        ret.append(arr[j])
        j+=1
    ind=0
    for i in range(start,end+1):
        arr[i]=ret[ind]
        ind+=1
        
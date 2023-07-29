# best and average
# O(nlogn) time and space
# worst case
# O(n^2) time and O(nlogn) space
def quickSort(array):
    # Write your code here.
    quickSortHelper(array,0,len(array)-1)
    return array
    
def quickSortHelper(array,start,end):
    if start >=end: return
    pivot = partition(array,start,end)
    quickSortHelper(array,start,pivot-1)
    quickSortHelper(array,pivot+1,end)

def partition(arr,start,end):
    pivot = arr[end]
    j=start
    print(start,end)
    for i in range(start,end+1):
        if arr[i]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
            
    arr[j],arr[end]=arr[end],arr[j]
    return j
        
        
def threeNumberSort(array, order):
    # Write your code here.
    low=0
    mid=0
    high=len(array)-1

    while mid<=high:
        if array[mid] == order[0]:
            swap(array,mid,low)
            mid+=1
            low+=1
        elif array[mid] == order[1]:
            mid+=1
        else:
            swap(array,mid,high)
            high-=1

    return array
            
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
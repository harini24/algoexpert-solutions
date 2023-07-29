def heapSort(array):
    # Write your code here.
    n=len(array)
    for i in range((n//2)-1,-1,-1):
        heapify(array,i,n)
    for i in range(len(array)-1,0,-1):
        swap(array,0,i)
        heapify(array,0,i)

    return array

def heapify(heap,i,n):
    while ((2*i)+1) < n:
        leftVal = heap[(2*i)+1]
        rightVal = heap[(2*i)+2] if (2*i)+2 < n else float("-inf")
        rootVal = max(leftVal,rightVal,heap[i])
        if rootVal == heap[i]: break
        elif rootVal == heap[(2*i)+1]:
            swap(heap,i,(2*i)+1)
            i = (2*i)+1
        else:
            swap(heap,i,(2*i)+2)
            i = (2*i)+2
            
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
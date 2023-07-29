# Time - O(n) best O(n*n) avg and worst
# space - O(1)

def insertionSort(array):
    # Write your code here.
    for i in range(1,len(array)):
        j=i
        while j>0 and array[j]<array[j-1]:
            temp=array[j]
            array[j]=array[j-1]
            array[j-1] = temp
            j-=1
    return array
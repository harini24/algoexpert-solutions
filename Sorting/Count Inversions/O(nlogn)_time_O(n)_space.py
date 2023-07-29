def countInversions(array):
    # Write your code here.
    ans = mergeSort(array,0,len(array)-1)
    return ans

def mergeSort(arr,start,end):
    if start >= end: return 0
    mid = (start+end)//2
    leftInv = mergeSort(arr,start,mid)
    rightInv = mergeSort(arr,mid+1,end)
    totalInv = countInv(arr,start,end,mid+1)
    print(arr,start,end,mid, leftInv,rightInv,totalInv)
    merge2Arr(arr,start,end,mid+1)
    
    return leftInv + rightInv+ totalInv
    
def merge2Arr(arr,s,e,y):
    i=s 
    j=y
    ret=[]
    while i<y and j<=e:
        if arr[i]>arr[j]:
            ret.append(arr[j])
            j+=1
        else:
            ret.append(arr[i])
            i+=1
    while i<y:
        ret.append(arr[i])
        i+=1
    while j<=e:
        ret.append(arr[j])
        j+=1
    ind=0
    for i in range(s,e+1):
        arr[i]=ret[ind]
        ind+=1
        
            
def countInv(arr,s,e,y):
    i=s
    j=y
    ans=0
    while i<y and j<=e:
        if arr[i]<=arr[j]:
            i+=1
        else:
            ans += y-i
            j+=1
    return ans
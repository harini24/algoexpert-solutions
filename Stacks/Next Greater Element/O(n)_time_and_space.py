def nextGreaterElement(array):
    # Write your code here.
    ngr=[-1]*len(array)
    stack=[]
    for i in range(2*len(array)):
        ind=i%len(array)
        val=array[ind]
        while stack and array[stack[-1]]<val:
            popped=stack.pop()
            ngr[popped]=val
            
        stack.append(ind)

    return ngr


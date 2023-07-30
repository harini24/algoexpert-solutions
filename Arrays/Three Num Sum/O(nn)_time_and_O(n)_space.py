def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets=[]
    for ind in range(len(array)):
        remainingSum=targetSum-array[ind]
        left=ind+1
        right=len(array)-1
        while(left<right):
            if(array[left]+array[right] == remainingSum):
                triplets.append([array[ind],array[left],array[right]])
                left+=1
                right-=1
            elif(array[left]+array[right] > remainingSum):
                right-=1
            else:
                left+=1
    return triplets

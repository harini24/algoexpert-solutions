def sweetAndSavory(dishes, target):
    # Write your code here.
    sweet=sorted([dish for dish in dishes if dish<0])
    savory=sorted([dish for dish in dishes if dish>0])

    bestPair=[0,0]
    bestDiff=float("inf")
    sweetInd=0
    savoryInd=len(savory)-1
    print(sweet,savory)
    while sweetInd<len(sweet) and savoryInd>=0:
        currSum = sweet[sweetInd] + savory[savoryInd]
        if currSum <= target:
            if target-currSum < bestDiff:
                bestDiff = target - currSum
                bestPair = [sweet[sweetInd] , savory[savoryInd]]
            sweetInd+=1
        else:
            savoryInd-=1

    return bestPair
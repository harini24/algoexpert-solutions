# O(br) time and space
def apartmentHunting(blocks, reqs):
    # Write your code here.
    minDistFromBlocks = list(map(lambda req:getMinDistances(blocks,req),reqs))
    print(minDistFromBlocks)
    maxDistancesAtBlock = getMaxDistancesAtBlock(blocks,minDistFromBlocks)
    print(maxDistancesAtBlock)
    return getBlockwithMinMaxDistance(maxDistancesAtBlock)

def getMinDistances(blocks,req):
    minDistances = [0] * len(blocks)
    closestInd = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestInd = i
        minDistances[i] = abs(i-closestInd)
    for i in range(len(blocks)-1,-1,-1):
        if blocks[i][req]:
            closestInd = i
        minDistances[i] = min(minDistances[i],abs(i-closestInd))

    return minDistances

def getMaxDistancesAtBlock(blocks,minDistFromBlocks):
    maxDistancesAtBlock = [0]*len(blocks)
    # for i in range(len(blocks)):
    for i in range(len(blocks)):
        for minDist in minDistFromBlocks:
            maxDistancesAtBlock[i] = max(maxDistancesAtBlock[i],minDist[i])
    return maxDistancesAtBlock

def getBlockwithMinMaxDistance(distances):
    ind = -1
    dist = float("inf")
    for i in range(len(distances)):
        if distances[i] < dist:
            dist = distances[i]
            ind = i
    return ind            
    
        

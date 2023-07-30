# O(n) time and space
def waterArea(heights):
    # Write your code here.
    n=len(heights)
    if n==0: return 0
    leftMax=[0]*n
    rightMax=[0]*n
    lMax=heights[0]
    rMax=heights[n-1]
    for i in range(n):
        lMax=max(lMax,heights[i])
        leftMax[i]=lMax
    for i in range(n-1,-1,-1):
        rMax=max(rMax,heights[i])
        rightMax[i]=rMax

    print(leftMax,rightMax)
    count = 0
    for i in range(n):
        height = heights[i]
        count += (min(leftMax[i],rightMax[i]) - height)
    return count
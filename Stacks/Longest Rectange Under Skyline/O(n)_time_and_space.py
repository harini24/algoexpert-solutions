def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    nsl=[-1]*len(buildings)
    nsg=[len(buildings)]*len(buildings)
    stack=[]
    for i in range(len(buildings)):
        while stack and buildings[stack[-1]] >= buildings[i]:
            stack.pop()
        if stack:
            nsl[i] = stack[-1]
        stack.append(i)
    stack=[]
    for i in range(len(buildings)-1,-1,-1):
        while stack and buildings[stack[-1]] >= buildings[i]:
            stack.pop()
        if stack:
            nsg[i] = stack[-1]
        stack.append(i)
    ans=0
    for i in range(len(buildings)):
        ans = max(ans,buildings[i]*(nsg[i]-nsl[i]-1))
    return ans

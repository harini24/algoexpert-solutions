def sunsetViews(buildings, direction):
    # Write your code here.
    stack=[]
    if direction == "EAST":
        for i,val in enumerate(buildings):
            while stack and buildings[stack[-1]]<=val:
                stack.pop()
            stack.append(i)
    else:
        for i in range(len(buildings)-1 ,-1,-1):
            val=buildings[i]
            while stack and buildings[stack[-1]]<=val:
                stack.pop()
            stack.append(i)
        stack=stack[::-1]

    return stack
        
        

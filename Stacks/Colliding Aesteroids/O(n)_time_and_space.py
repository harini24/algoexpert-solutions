def collidingAsteroids(asteroids):
    # Write your code here.
    stack=[]
    for val in asteroids:
        if not stack or val >=0: 
            stack.append(val)
        else:
            flag=True
            while stack and stack[-1]>=0 and stack[-1]<=abs(val):
                popped = stack.pop()
                if popped==abs(val):
                    flag=False
                    break
            if flag and not stack:
                stack.append(val)
            elif flag and stack and stack[-1]<0:
                stack.append(val)
            
    return stack
    
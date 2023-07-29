def calculateLargestRectangle(land):
    # Write your code here.
    nsl=[-1]*len(land)
    nsg=[len(land)]*len(land)
    stack=[]
    for i in range(len(land)):
        while stack and land[stack[-1]] >= land[i]:
            stack.pop()
        if stack:
            nsl[i] = stack[-1]
        stack.append(i)
    stack=[]
    for i in range(len(land)-1,-1,-1):
        while stack and land[stack[-1]] >= land[i]:
            stack.pop()
        if stack:
            nsg[i] = stack[-1]
        stack.append(i)
    ans=0
    for i in range(len(land)):
        ans = max(ans,land[i]*(nsg[i]-nsl[i]-1))
    return ans

# O(n*m) time and O(m) space
# n - number of rows
# m - number of columns
def largestPark(land):
    # Write your code here.
    for i in range(len(land[0])):
        if not land[0][i]:
            land[0][i] = 1
        else:
            land[0][i] = 0
            
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            if not land[i][j]:
                land[i][j]= 1+ land[i-1][j]
            else:
                land[i][j] = 0
    ans = 0 
    for i in range(len(land)):
        ans = max(ans,calculateLargestRectangle(land[i]))
    return ans

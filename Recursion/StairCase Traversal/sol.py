
def helper(height,maxSteps,curr):
    if curr>height:
        return 0
    if curr==height:
        return 1
    ans=0
    for i in range(1,maxSteps+1):
        ans+=helper(height,maxSteps,curr+i)
    return ans

# O(k^n) time and O(n) space
# n - height
# k - number of steps allowed
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return helper(height,maxSteps,0)

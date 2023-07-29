def helper(cache,n):
    if n in cache:
        return cache[n]
    ans = 0
    for L in range(n):
        R=n-1-L
        lWays = helper(cache,L)
        rWays = helper(cache,R)
        ans += lWays * rWays
    cache[n]=ans
    return ans

def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    cache={0:1,1:1,2:2}
    return helper(cache,n)

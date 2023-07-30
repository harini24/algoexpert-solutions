# O(n^3 + m) time and O(n+m) space
def numbersInPi(pi, numbers):
    # Write your code here.
    numbersTable={number:True for number in numbers}
    if pi in numbers: return 0
    cache={}
    helper(pi,numbersTable,0,len(pi)-1,cache)
    print(cache)
    return cache[ 0]

def helper(pi,numTable,si,ei,cache):
    if si>ei:
        return -1
    if pi[si:ei+1] in numTable: return 0
    if si in cache:
        return cache[si]
    minpart=float("inf")
    for i in range(si,ei+1):
        if pi[si:i+1] in numTable:
            ret=helper(pi,numTable,i+1,ei,cache)
            if ret != -1:
                minpart=min(minpart,ret)
    cache[si] = minpart+1 if minpart!=float("inf") else -1
    return cache[si]
        
        
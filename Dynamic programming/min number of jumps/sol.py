# O(n) time and space
def minNumberOfJumps(array):
    # Write your code here.
    if len(array)==1:
        return 0
    steps=array[0]
    maxReach=array[0]
    jumps=0
    print(steps,maxReach,jumps)
    for i in range(1,len(array)-1):
        steps-=1
        maxReach=max(maxReach,i+array[i])
        if steps==0:
            jumps+=1
            steps=maxReach-i
        print(i,array[i],steps,maxReach,jumps)
    return jumps+1 
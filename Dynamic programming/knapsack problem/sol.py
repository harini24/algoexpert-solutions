# O(nc) time and space
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    dp=[[0 for J in range(capacity+1)] for i in range(len(items)+1)]
    for i in range(1,len(items)+1):
        # print(i)
        for j in range(capacity+1):
            dp[i][j] = dp[i-1][j]
            if j-items[i-1][1] >=0:
                dp[i][j] = max(dp[i][j] , items[i-1][0] + dp[i-1][j-items[i-1][1]])
    print(dp)
    return [dp[-1][-1],buildKnapsackItems(dp,items)]


def buildKnapsackItems(dp,items):
    seq=[]
    i=len(dp)-1
    j=len(dp[0])-1

    while i>0 and j>0:
        if dp[i][j] == dp[i-1][j]:
            i-=1
        else:
            print(i,j)
            seq.append(i-1)
            j-=items[i-1][1]
            i-=1
    return seq[::-1]
            
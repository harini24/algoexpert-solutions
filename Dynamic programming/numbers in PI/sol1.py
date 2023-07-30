# O(n^3 + m) time and O(n+m) space
def numbersInPi(pi, numbers):
    # Write your code here.
    numberTable={number:True for number in numbers}
    if pi in numberTable: return 0
    cache={}
    dp=[None]*len(pi)
    dp[-1]=0 if  pi[-1] in numberTable else -1

    for i in range(len(pi)-2,-1,-1):
        if pi[i:] in numberTable:
            dp[i]=0
            continue
        else:
            ans=float("inf")
            for j in range(i+1,len(dp)):
                if pi[i:j] in numberTable and dp[j] != -1:
                    ans=min(ans,dp[j])
            dp[i] = ans+1 if ans != float("inf") else -1
    return dp[0]
                    
                

        
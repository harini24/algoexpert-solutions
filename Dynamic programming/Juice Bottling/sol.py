#O(n*n) time and O(n) space
def juiceBottling(prices):
    # Write your code here.
    dp = [[i] for i in range(len(prices))]
    for i in range(2,len(prices)):
        l=0
        r=i
        while l<=r:
            val = prices[l]+prices[r]
            if val>prices[i]:
                prices[i] = val
                dp[i]=dp[l]+dp[r]
            l+=1
            r-=1
    dp[-1].sort()
    return dp[-1]
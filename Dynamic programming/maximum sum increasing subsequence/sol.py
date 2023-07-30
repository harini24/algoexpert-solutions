#O(n*n) time and O(n) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    dp=[val for val in array]
    dp[0]=array[0]
    seq=[None]*len(array)
    maxSumInd=0
    for i in range(1,len(array)):
        for j in range(i):
            if array[j]<array[i] and  dp[j]+array[i]>dp[i]:
                dp[i]=dp[j]+array[i]
                seq[i]=j
        if dp[i] > dp[maxSumInd]:
            maxSumInd=i
    return [dp[maxSumInd],generateSequence(array,seq,maxSumInd)]
    
                    
def generateSequence(array,seq,ind):
    ret=[]
    while ind != None:
        ret.append(array[ind])
        ind=seq[ind]
    return ret[::-1]
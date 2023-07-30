# O(nm) time and space
def longestCommonSubsequence(str1, str2):
    dp=[[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return generateSeq(dp,str1)

def generateSeq(dp,str):
    seq=[]
    i=len(dp)-1
    j=len(dp[0])-1
    while i>0 and j>0:
        if dp[i][j] == dp[i-1][j]:
            i-=1
        elif dp[i][j] == dp[i][j-1]:
            j-=1
        else :
            seq.append(str[i-1])
            i-=1
            j-=1
    return seq[::-1]


def helper(ind,visited,diag,antidiag,n):
    if ind==n: return 1
    ans=0
    for i in range(n):
        if not visited[i] and not diag[ind+i] and not antidiag[ind-i+n-1]:
            visited[i]=True
            diag[ind+i]=True
            antidiag[ind+n-i-1]=True
            ans += helper(ind+1,visited,diag,antidiag,n)
            antidiag[ind+n-i-1]=False
            diag[ind+i]=False
            visited[i]=False
    return ans  
def nonAttackingQueens(n):
    # Write your code here.
    visited=[False]*n
    diag=[False]*(n+n-1)
    antiDiag=[False]*(n+n-1)
    return helper(0,visited,diag,antiDiag,n)

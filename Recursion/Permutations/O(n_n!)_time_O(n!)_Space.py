
def helper(ret,curr,visited,A,ind):
    if ind==len(A):
        ret.append(curr)

    for i in range(len(A)):
        if visited[i] == False:
            visited[i]=True
            helper(ret,curr+[A[i]],visited,A,ind+1)
            visited[i]=False

def getPermutations(array):
    # Write your code here.
    if len(array)==0 : return []
    ret=[]
    curr=[]
    visited=[False]*len(array)
    helper(ret,curr,visited,array,0)
    return ret

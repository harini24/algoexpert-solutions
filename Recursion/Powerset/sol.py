def helper(ret,curr,arr,ind):
    # print(len(arr),curr,ind)
    if ind==len(arr):
        ret.append(curr)
        return
    helper(ret,curr,arr,ind+1)
    helper(ret,curr+[arr[ind]],arr,ind+1)

# O(n*(2^n)) time and O(n) space
def powerset(array):
    # Write your code here.
    ret = []
    curr=[]
    helper(ret,curr,array,0)
    return ret

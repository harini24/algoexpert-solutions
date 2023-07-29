# k - len of string three

# count = 0
def helper(i,j,k,str1,str2,target,dp):
    # global count
    # count+=1
    if k == -1 and (j==-1 or i==-1): return True
    if k == -1 and ( j!=-1 and i!=-1): return False
    
    if (i,j,k) in dp: return dp[(i,j,k)]
    if (i>=0 and  str1[i] == target[k]) and (j>=0 and str2[j]==target[k]):
        dp[(i,j,k)] = helper(i-1,j,k-1,str1,str2,target,dp) or helper(i,j-1,k-1,str1,str2,target,dp)
    elif i>=0 and str1[i] == target[k]:
        dp[(i,j,k)] = helper(i-1,j,k-1,str1,str2,target,dp)
    elif j>=0 and str2[j] == target[k]:
        dp[(i,j,k)] = helper(i,j-1,k-1,str1,str2,target,dp)
    else:
        dp[(i,j,k)] = False
    return dp[(i,j,k)] 
def interweavingStrings(one, two, three):
    # global count
    # count = 0
    if len(three) != (len(one)+len(two)): return False
    dp={}
    ans =  helper(len(one)-1,len(two)-1,len(three)-1,one,two,three,dp)
    # print(len(dp),len(one),len(two),len(three),count)
    return ans
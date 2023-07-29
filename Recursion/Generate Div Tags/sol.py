def helper(ret,curr,open,close,num):
    if open == num and close == num:
        ret.append(curr)
        return
    if open<num:
        helper(ret,curr+"<div>",open+1,close,num)
    if close<open:
        helper(ret,curr+"</div>",open,close+1,num)
def generateDivTags(numberOfTags):
    # Write your code here.
    ret= []
    helper(ret,"",0,0,numberOfTags)
    return ret

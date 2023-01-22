def findThreeLargestNumbers(array):
    # Write your code here.
    ret=[None,None,None]
    for num  in array:
        updateLargest(num,ret)
    return ret

def updateLargest(num,ret):
    if ret[2] is None or num>ret[2]:
        shiftAndUpdate(ret,num,2)
    elif ret[1] is None or num>ret[1]:
        shiftAndUpdate(ret,num,1)
    elif ret[0] is None or num>ret[0]:
        shiftAndUpdate(ret,num,0)
    
def shiftAndUpdate(ret,num,ind):
    for  i in range(ind+1):
        if ind == i:
            ret[i]=num
        else:
            ret[i]=ret[i+1]
def helper(currLow,currHigh,cups, low, high,failed):
    key=(currLow,currHigh)
    if key in failed: return False
    if currHigh>high:
        failed.add(key)
        return False
    if currLow>=low and currHigh<=high:
        return True
    for l,h in cups:
         if helper(currLow+l,currHigh+h,cups, low, high,failed):
             return True
    print(currLow,currHigh, low, high,key)
    
    failed.add(key)
    return False

def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    failedComb=set()
    return helper(0,0,measuringCups, low, high,failedComb)

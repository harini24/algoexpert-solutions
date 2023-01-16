def productSum(array,depth=1):
    # Write your code here.
    sum = 0 
    for val in array:
        if type(val) is list:
            sum += productSum(val,depth+1)
        else:
            sum += val
    return sum*depth
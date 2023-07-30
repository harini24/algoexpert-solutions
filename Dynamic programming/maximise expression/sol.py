# O(n) time and space
def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4: return 0
    maxOfA=[0]*len(array)
    maxOfAMinusB=[float("-inf")]*len(array)
    maxOfAMinusBPlusC=[float("-inf")]*len(array)
    maxOfAMinusBPlusCMinusD=[float("-inf")]*len(array)
    maxOfA[0] = array[0]
    for i in range(1,len(array)):
        maxOfA[i] =  max(array[i],maxOfA[i-1])
    for i in range(1,len(array)):
        maxOfAMinusB[i] =  max(maxOfA[i-1]-array[i],maxOfAMinusB[i-1])
    for i in range(2,len(array)):
        maxOfAMinusBPlusC[i] =  max(maxOfAMinusB[i-1]+array[i],maxOfAMinusBPlusC[i-1])
    for i in range(3,len(array)):
        maxOfAMinusBPlusCMinusD[i] =  max(maxOfAMinusBPlusC[i-1]-array[i],maxOfAMinusBPlusCMinusD[i-1])
    return maxOfAMinusBPlusCMinusD[-1]

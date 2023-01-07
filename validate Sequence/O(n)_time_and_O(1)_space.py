def isValidSubsequence(array, sequence):
    # Write your code here.
    seqInd = 0
    for i in array:
        if seqInd == len(sequence):
            break
        if i == sequence[seqInd]:
            seqInd +=1
    return seqInd == len(sequence)

def isValidSubsequence1(array, sequence):
    # Write your code here.
    arrInd=0
    seqInd=0
    while arrInd < len(array) and seqInd < len(sequence):
        if array[arrInd] == sequence[seqInd]:
            seqInd += 1
        arrInd+= 1
    return seqInd == len(sequence)
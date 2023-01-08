def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]
    for ind in range(len(array)):
        sortedSquares[ind] = array[ind]**2
    sortedSquares.sort()
    return sortedSquares

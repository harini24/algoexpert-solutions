def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    createSumMatrix(matrix)
    print(matrix)
    maxSubMatrixSum = float("-inf")
    for i in range(len(matrix)-size+1):
        for j in range(len(matrix[0])-size+1):
            sr=i
            sc=j
            er=i+size-1
            ec=j+size-1

            if sr==0 and sc==0: 
                maxSubMatrixSum = max(maxSubMatrixSum,matrix[er][ec])
            elif sc==0 or sr == 0:
                if sr == 0:
                 maxSubMatrixSum = max(maxSubMatrixSum,matrix[er][ec]-matrix[er][sc-1])
                else:
                 maxSubMatrixSum = max(maxSubMatrixSum,matrix[er][ec]-matrix[sr-1][ec])
            else:
                 maxSubMatrixSum = max(maxSubMatrixSum,matrix[er][ec]-matrix[sr-1][ec]-matrix[er][sc-1]+matrix[sr-1][sc-1])
    return maxSubMatrixSum

def createSumMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(1,len(matrix[0])):
            matrix[i][j] += matrix[i][j-1]
    for i in range(len(matrix[0])):
        for j in range(1,len(matrix)):
            matrix[j][i] += matrix[j-1][i]
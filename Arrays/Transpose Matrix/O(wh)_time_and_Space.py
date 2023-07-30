def transposeMatrix(matrix):
    # Write your code here.
    arr=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            arr[j][i] = matrix[i][j]
    return arr
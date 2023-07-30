#O(n+m) time O(1) space
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    col=len(matrix[0])-1
    row=0
    while row<len(matrix) and col>=0:
        val = matrix[row][col]
        if val == target:
            return [row,col]
        elif val>target:
            col-=1
        else:
            row+=1
    return [-1,-1]
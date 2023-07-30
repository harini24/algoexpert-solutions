# O(wh) time and space

def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegatives(matrix)
    return passes-1 if not containsNegative(matrix) else -1

def containsNegative(matrix):
    for row in matrix:
        for val in row:
            if val<0:
                return True
    return False

def getAdjacentPosition(row,col,matrix):
    adjacentPositions=[]
    if row>0:
        adjacentPositions.append([row-1,col])
    if row<len(matrix)-1:
        adjacentPositions.append([row+1,col])
    if col>0:
        adjacentPositions.append([row,col-1])
    if col<len(matrix[0])-1:
        adjacentPositions.append([row,col+1])
    return adjacentPositions

def getAllPositivePosition(matrix):
    positivePositions=[]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            val=matrix[row][col]
            if val>0:
                positivePositions.append([row,col])
    return positivePositions

def convertNegatives(matrix):
    nextPasses=getAllPositivePosition(matrix)
    passes=0

    while len(nextPasses)>0:
        currentPasses=nextPasses
        nextPasses=[]
        print(currentPasses)
        while len(currentPasses)>0:
            currentRow,currentCol = currentPasses.pop(0)
            adjacentPositions = getAdjacentPosition(currentRow,currentCol,matrix)

            for position in adjacentPositions:
                row,col = position
                value = matrix[row][col]
                if value<0:
                    print("here")
                    matrix[row][col] *= -1
                    nextPasses.append([row,col])
        passes+=1

    return passes
    

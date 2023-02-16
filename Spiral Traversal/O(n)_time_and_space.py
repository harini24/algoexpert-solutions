def spiralTraverse(array):
    # Write your code here.
    startCol=0
    endCol=len(array[0])-1
    startRow=0
    endRow=len(array)-1
    ret=[]
    while startCol<=endCol and startRow<=endRow:
        for val in range(startCol,endCol+1):
            ret.append(array[startRow][val])

        startRow+=1
        print(ret,startCol,endCol,startRow,endRow)
        for val in range(startRow,endRow+1):
            ret.append(array[val][endCol])
        endCol-=1
        print(ret,startCol,endCol,startRow,endRow)
        for val in reversed(range(startCol,endCol+1)):
            if endRow+1==startRow: break
            ret.append(array[endRow][val])
        endRow-=1
        print(ret,startCol,endCol,startRow,endRow)
        for val in reversed(range(startRow,endRow+1)):
            if endCol==startCol-1: break
            ret.append(array[val][startCol])
        startCol+=1
        print(ret,startCol,endCol,startRow,endRow)
    return ret
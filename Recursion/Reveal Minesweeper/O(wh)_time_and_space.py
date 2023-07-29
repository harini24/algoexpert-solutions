def revealMinesweeper(board, row, col):
    # Write your code here.
    if board[row][col] == "M":
        board[row][col] = "X"
        return board

    neighbors = getNeighbors(board,row,col)
    minesCount=0
    for nRow,nCol in neighbors:
        if board[nRow][nCol]=="M":
            minesCount += 1

    if minesCount>0:
        board[row][col] = str(minesCount)
    else:
        board[row][col] = "0"
        for nRow,nCol in neighbors:
            if board[nRow][nCol]=="H":
                revealMinesweeper(board, nRow, nCol)

    return board

def getNeighbors(board,row,col):
    dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    neighbors=[]
    for r,c in dir:
        nr=row+r
        nc=col+c
        if nr>=0 and nc>=0 and nr<len(board) and nc<len(board[0]):
            neighbors.append((nr,nc))
    return neighbors
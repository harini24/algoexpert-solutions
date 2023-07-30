def zigzagTraverse(array):
    # Write your code here.
    row=0
    col=0
    rowEnd=len(array)-1
    colEnd=len(array[0])-1
    goingDown=True
    ret=[]
    while (row>=0 and col>=0 and row<=rowEnd and col<=colEnd):
        print(array[row][col])
        ret.append(array[row][col])
        if goingDown:
            if col==0 or row==rowEnd:
                goingDown=False
                if row==rowEnd:
                    col+=1
                else:
                    row+=1
            else:
                row+=1
                col-=1
        else:
            if row==0 or col==colEnd:
                goingDown=True
                if col==colEnd:
                    row+=1
                else: 
                    col+=1
            else:
                row-=1
                col+=1
    return ret
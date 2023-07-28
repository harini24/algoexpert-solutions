def minHeightBst(array):
    return constructMinHeightBst(array,None,0,len(array)-1)

def constructMinHeightBst(array,bst,start,end):
    if end<start: return 
    minInd = (start+end)//2
    if bst is None:
        bst=BST(array[minInd])
        print("here")
    else:
        bst.insert(array[minInd])
    constructMinHeightBst(array,bst,start,minInd-1)
    constructMinHeightBst(array,bst,minInd+1,end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

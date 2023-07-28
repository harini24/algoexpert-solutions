# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self,rootInd):
        self.rootInd=rootInd
        
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(preOrderTraversalValues,treeInfo,float("-inf"),float("inf"))

def reconstructBstFromRange(preOrderTraversalValues,treeInfo,minVal,maxVal):
    if treeInfo.rootInd == len(preOrderTraversalValues): return None
    rootValue = preOrderTraversalValues[treeInfo.rootInd]
    if rootValue <minVal or rootValue>=maxVal:
        return None
    treeInfo.rootInd+=1
    leftSubTree =  reconstructBstFromRange(preOrderTraversalValues,treeInfo,minVal,rootValue)
    rightSubTree = reconstructBstFromRange(preOrderTraversalValues,treeInfo,rootValue,maxVal)
    return BST(rootValue,leftSubTree,rightSubTree)
    

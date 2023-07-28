# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 0:
        return None

    currValue=preOrderTraversalValues[0]
    rightSubTreeInd=len(preOrderTraversalValues)
    for i in range(1,len(preOrderTraversalValues)):
        if preOrderTraversalValues[i] >= currValue:
            rightSubTreeInd=i
            break;

    leftSubTree = reconstructBst(preOrderTraversalValues[1:rightSubTreeInd])
    rightSubTree = reconstructBst(preOrderTraversalValues[rightSubTreeInd:])
    return BST(currValue, leftSubTree,rightSubTree)
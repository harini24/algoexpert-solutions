# O(n) time and space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    branchSums=[]
    calculateBranchSums(branchSums, root,0)
    return branchSums

def calculateBranchSums(branchSums,currentNode, currentSum):
    if currentNode is None: return
    currentSum += currentNode.value
    if currentNode.left is None and  currentNode.right is None:
        branchSums.append(currentSum)
        return
    calculateBranchSums(branchSums,currentNode.left, currentSum)
    calculateBranchSums(branchSums,currentNode.right, currentSum)
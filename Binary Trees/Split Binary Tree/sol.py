# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self):
        self.partition=0
def splitBinaryTree(tree):
    # Write your code here.
    totalWeight = getTreeWeight(tree)
    if totalWeight%2 != 0: return 0
    print(totalWeight)
    treeInfo = TreeInfo()
    TreeSplitHelper(tree,totalWeight,treeInfo)
    return treeInfo.partition
    
def TreeSplitHelper(node,treeWeight,treeInfo):
    if node is None:
        return 0
    l=TreeSplitHelper(node.left,treeWeight,treeInfo)
    r=TreeSplitHelper(node.right,treeWeight,treeInfo)
    print(l,r)
    if l == treeWeight//2 or r== treeWeight//2:
        treeInfo.partition = treeWeight//2
    return node.value + l + r
    
def getTreeWeight(node):
    if node is None:
        return 0
    return node.value + getTreeWeight(node.left) + getTreeWeight(node.right)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self):
        self.prevNode = None

def flattenBinaryTree(root):
    # Write your code here.
    treeInfo=TreeInfo()
    traverse(root,treeInfo)
    return treeInfo.prevNode

def traverse(tree,treeInfo):
    if tree is None:
        return 
    traverse(tree.right,treeInfo)
    tree.right = treeInfo.prevNode
    if treeInfo.prevNode:
        treeInfo.prevNode.left = tree
    treeInfo.prevNode=tree
    traverse(tree.left,treeInfo)
    
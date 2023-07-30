# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo


def TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height

def getTreeInfo(tree):
    if tree is None:
        return treeInfo(0,0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = rightTreeInfo.height + leftTreeInfo.height
    currentHeight = 1 + max(rightTreeInfo.height , leftTreeInfo.height)
    maxDiameterSoFar = max(rightTreeInfo.diameter , leftTreeInfo.diameter)
    currentDiameter = max(maxDiameterSoFar,longestPathThroughRoot)

    return TreeInfo(currentDiameter,currentHeight)
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) time O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depth1 = getNodeDepth(descendantOne,topAncestor)
    depth2 = getNodeDepth(descendantTwo,topAncestor)

    if depth1>depth2: return backtrackTree(descendantOne,descendantTwo,depth1-depth2)
    else: return backtrackTree(descendantTwo,descendantOne,depth2-depth1)

def getNodeDepth(node,ancestor):
    depth=0
    while node != ancestor:
        depth+=1
        node=node.ancestor
    return depth

def backtrackTree(lowerNode,topNode,diff):
    print(diff)
    while diff>0:
        lowerNode=lowerNode.ancestor
        diff-=1
    print(lowerNode.name,topNode.name)

    while lowerNode != topNode:
        lowerNode=lowerNode.ancestor
        topNode=topNode.ancestor

    return lowerNode


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# h - height
# k - input param
class TreeInfo:
    def __init__(self,count,val):
        self.visitedNodes=count
        self.lastVisitedValue=val

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    info = TreeInfo(0,-1)
    reverseInorderTraversal(tree,k,info)
    return info.lastVisitedValue

def reverseInorderTraversal(tree,k,info):
    if tree is None or info.visitedNodes>=k:
        return
    reverseInorderTraversal(tree.right,k,info)
    if info.visitedNodes<k:
        info.visitedNodes+=1
        info.lastVisitedValue=tree.value
    reverseInorderTraversal(tree.left,k,info)
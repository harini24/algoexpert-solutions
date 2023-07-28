# O(logn) time and space - average
# O(n) time and space - worst

def findClosestValueInBst(tree, target):
    # Write your code here.
    return findingClosestValueInBtsHelper(tree,target,tree.value)

def findingClosestValueInBtsHelper(tree,target,closest):
    if tree is None: 
        return closest

    if abs(closest-target) > abs(target - tree.value):
        closest = tree.value
    if target > tree.value:
        return findingClosestValueInBtsHelper(tree.right,target,closest)
    elif target < tree.value:
        return findingClosestValueInBtsHelper(tree.left,target,closest)
    else:
        return closest
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

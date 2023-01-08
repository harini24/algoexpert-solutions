# O(logn) time and O(1) space - average
# O(n) time and  O(1) space - worst

def findClosestValueInBst(tree, target):
    # Write your code here.
    currentNode = tree
    closest= tree.value
    while currentNode is not None:
        if abs(closest-target) > abs(target-currentNode.value):
            closest = currentNode.value
        if currentNode.value>target:
            currentNode = currentNode.left
        elif  currentNode.value<target:
            currentNode = currentNode.right
        else:
            break
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
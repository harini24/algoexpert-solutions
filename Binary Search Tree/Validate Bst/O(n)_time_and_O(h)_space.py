# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree,float("-inf"),float("inf"))

def validateBstHelper(tree,minVal,maxVal):
    if tree is None: return True
    if tree.value<minVal or tree.value>=maxVal: return False
    leftIsValid = validateBstHelper(tree.left,minVal,tree.value)
    return leftIsValid and validateBstHelper(tree.right,tree.value,maxVal)
    
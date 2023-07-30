import math
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time and O(h) space
def evaluateExpressionTree(tree):
    # Write your code here.
    return helper(tree)

def helper(tree):
    if tree.left is None and tree.right is None:
        return tree.value
    left = helper(tree.left)
    right= helper(tree.right)

    if tree.value == -1:
        return left+right
    elif tree.value == -2:
        print(left,right)
        return left - right
    elif tree.value == -3:
        print(left,right)
        return int(left/right)
    else:
        return left * right

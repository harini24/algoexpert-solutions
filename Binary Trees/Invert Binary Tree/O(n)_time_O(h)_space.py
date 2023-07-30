def invertBinaryTree(tree):
    # Write your code here.
    if tree:
        swapBranch(tree)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
  

def swapBranch(tree):
  tree.left,tree.right = tree.right,tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertBinaryTree(tree):
    # Write your code here.
    nodes=[tree]
    while len(nodes):
        node= nodes.pop()
        if node is None:
            continue
        swapBranch(node)
        nodes.append(node.left)
        nodes.append(node.right)
        
def swapBranch(tree):
  tree.left,tree.right = tree.right,tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

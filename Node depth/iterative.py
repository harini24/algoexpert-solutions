# O(n) time and O(h) space
# n - number of node
# h - tree height

def nodeDepths(root):
    # Write your code here.
    if root is None: return 0
    depths=0
    stack=[(root,0)]
    while len(stack) > 0:
        currNode,currDepth=stack.pop()
        depths+=currDepth
        if currNode.left: stack.append((currNode.left,currDepth+1))
        if currNode.right: stack.append((currNode.right,currDepth+1))
    return depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# O(n) time and O(1) space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    stack = [(root,0)]
    branchSums=[]
    while len(stack):
        currentNode,currentSum = stack.pop()
        if currentNode.left is None and currentNode.right is None:
            branchSums.append(currentSum+currentNode.value)

        if currentNode.right is not None:
            stack.append((currentNode.right, currentSum+currentNode.value))
        if currentNode.left is not None:
            stack.append((currentNode.left, currentSum+currentNode.value))
        
    return branchSums
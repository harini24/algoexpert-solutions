# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array=[]
    inorderTraversal(array,tree)
    print(array)
    return  array[len(array)-k]

def inorderTraversal(array,tree):
    if tree is not None:
        inorderTraversal(array,tree.left)
        array.append(tree.value)
        inorderTraversal(array,tree.right)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None: return tree2
    stack1=[tree1]
    stack2=[tree2]

    while(len(stack1)):
        node1=stack1.pop()
        node2=stack2.pop()

        if node2 is None: continue
        node1.value += node2.value

        if node1.right is None:
            node1.right=node2.right
        else:
            stack1.append(node1.right)
            stack2.append(node2.right)
            
        if node1.left is None:
            node1.left=node2.left
        else:
            stack1.append(node1.left)
            stack2.append(node2.left)
        
    return tree1

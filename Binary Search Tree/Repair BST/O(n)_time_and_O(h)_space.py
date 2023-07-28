# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# n - number of node
# h - height of tree
def repairBst(tree):
    # Write your code here.
    first=middle=prev=None

    curr=tree
    stack=[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        popped=stack.pop()
        if prev and prev.value > popped.value:
            if not first:
                first=prev
            middle=popped
        prev=popped
        curr=popped.right

    temp=middle.value
    first.value,middle.value=middle.value,first.value
    return tree
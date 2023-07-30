# O(n) time and O(1) space

def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    prev=None
    curr=tree
    while curr:
        if prev is None or prev==curr.parent:
            if curr.left:
                next=curr.left
            else:
                callback(curr)
                next = curr.right if curr.right is not None else curr.parent
        elif prev == curr.left:
            callback(curr)
            next = curr.right if curr.right is not None else curr.parent
        else:
            next = curr.parent
        prev=curr
        curr=next
    
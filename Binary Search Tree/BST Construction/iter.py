# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # avg O(nlogn) time O(1) and space
    # wrst O(n) time and O(1) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currNode = self
        while True:
            if value<currNode.value:
                if currNode.left is None:
                    currNode.left=BST(value)
                    break
                currNode=currNode.left
            else:
                if currNode.right is None:
                    currNode.right=BST(value)
                    break
                currNode=currNode.right 
        return self

    # avg O(nlogn) time O(1) and space
    # wrst O(n) time and O(1) space
    def contains(self, value):
        # Write your code here.
        currNode = self
        while currNode is not None:
            if value==currNode.value:
                return True
            elif value<currNode.value:
                currNode=currNode.left
            else:
                currNode=currNode.right 
        return False

    # avg O(nlogn) time O(1) and space
    # wrst O(n) time and O(1) space
    def remove(self, value,parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currNode = self
        
        while currNode is not None:
            if value<currNode.value:
                parentNode=currNode
                currNode=currNode.left
            elif value>currNode.value:
                parentNode=currNode
                currNode=currNode.right
            else:
                if currNode.left is not None and currNode.right is not None:
                    currNode.value =  currNode.right.getMinValue()
                    currNode.right.remove(currNode.value,currNode)
                elif parentNode is None:
                    if currNode.left is not None:
                        currNode.value=currNode.left.value
                        currNode.right=currNode.left.right
                        currNode.left=currNode.left.left
                    elif currNode.right is not None:
                        currNode.value=currNode.right.value
                        currNode.left=currNode.right.left
                        currNode.right=currNode.right.right
                elif parentNode.left == currNode:
                    parentNode.left = currNode.left if currNode.left is not None else currNode.right
                else:
                    parentNode.right = currNode.left if currNode.left is not None else currNode.right
                break
        return self

    def getMinValue(self):
        currNode = self
        while currNode.left is not None:
            currNode = currNode.left
        return currNode.value

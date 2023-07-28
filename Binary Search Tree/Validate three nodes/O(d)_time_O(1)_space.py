# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# d - distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    searchOne=nodeOne
    searchTwo=nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching = searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundTwo or finishedSearching: break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value>nodeTwo.value else searchOne.right
        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value>nodeTwo.value else searchTwo.right
            
    foundNodeFromAnother  =searchOne is nodeThree  or searchTwo is nodeOne  
    foundTwo  =searchOne is nodeTwo  or searchTwo is nodeTwo  

    if not foundTwo or foundNodeFromAnother:
        return False

    return searchForTarget(nodeTwo,nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node,target):
    while node is not None and node is not target:
        node = node.left if node.value>target.value else node.right
    return node is target
        
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        if self is None: return array
        stack=[self]
        while len(stack):
            currNode= stack.pop()
            array.append(currNode.name)
            for child in reversed(currNode.children):
                stack.append(child)
        return array

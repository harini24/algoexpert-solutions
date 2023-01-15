# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currNode=linkedList
    while currNode:
        nextDistinctNode = currNode.next
        while nextDistinctNode and nextDistinctNode.value==currNode.value:
            nextDistinctNode=nextDistinctNode.next
        currNode.next = nextDistinctNode
        currNode = nextDistinctNode
    return linkedList

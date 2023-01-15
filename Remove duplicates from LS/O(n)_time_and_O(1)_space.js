// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  // Write your code here.
  let currNode = linkedList;
  while (currNode) {
    let nextDistinctNode = currNode.next;
    while (nextDistinctNode && nextDistinctNode.value === currNode.value) {
      nextDistinctNode = nextDistinctNode.next;
    }
    currNode.next = nextDistinctNode;
    currNode = nextDistinctNode;
  }
  return linkedList;
}

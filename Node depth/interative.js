// O(n) time and O(h) space
// n - number of node
// h - tree height

function nodeDepths(root) {
    // Write your code here.
    let sumOfDepth = 0
    const stack=[[root,0]]
    while(stack.length){
      const [currNode,depth]=stack.pop()
      sumOfDepth+=depth
      
      currNode.left && stack.push([currNode.left,depth+1])
      currNode.right && stack.push([currNode.right,depth+1])
    }
    return sumOfDepth
  }
  
  // This is the class of the input binary tree.
  class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function branchSums(root) {
    // Write your code here.
    const stack = []
    stack.push([root,0])
    const branchSums=[]
    while(stack.length){
      const [currentNode,currentSum] = stack.pop()
      if (!currentNode.left && !currentNode.right){
        branchSums.push(currentSum+currentNode.value)
      }
      if (currentNode.right){
         stack.push([currentNode.right,currentSum+currentNode.value])
      }
      if (currentNode.left){
         stack.push([currentNode.left,currentSum+currentNode.value])
      }
    }
    return branchSums
  }
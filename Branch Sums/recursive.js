// O(n) time and space
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function branchSums(root) {
    // Write your code here.
    let branchSums=[]
    calculateBranchSums(branchSums, root, 0)
    return branchSums
  }
  
  const calculateBranchSums = (branchSums, node, currentSum) => {
    
    if (!node) return 
  
    currentSum += node.value 
    if (!node.right && !node.left){
      branchSums.push(currentSum)
    }
  
    calculateBranchSums(branchSums, node.left, currentSum)
    calculateBranchSums(branchSums, node.right, currentSum)
  }
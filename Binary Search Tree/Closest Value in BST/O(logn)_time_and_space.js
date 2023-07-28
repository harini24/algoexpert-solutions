// O(logn) time and O(logn) space - average
// O(n) time and  O(n) space - worst

function findClosestValueInBst(tree, target) {
    // Write your code here.
    return findClosestValueInBtsHelper(tree,target,tree.value)
  }
  
  const findClosestValueInBtsHelper = (tree, target, closest) =>{
    if (!tree) return closest
    if( Math.abs(closest - target) > Math.abs(target-tree.value)){
      closest=tree.value
    }
    if(target > tree.value){
      return findClosestValueInBtsHelper(tree.right,target,closest)
    }else if(target <tree.value){
      return findClosestValueInBtsHelper(tree.left,target,closest)
    }else{
      return closest
    }
  }
  // This is the class of the input tree. Do not edit.
  class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
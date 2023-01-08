// O(logn) time and O(1) space - average
// O(n) time and  O(1) space - worst

function findClosestValueInBst(tree, target) {
    // Write your code here.
     return findClosestValueInBtsHelper(tree,target,tree.value)
  }
  const findClosestValueInBtsHelper = (tree, target, closest) =>{
    let currentNode = tree
    while(currentNode){
      if (Math.abs(target-closest)>Math.abs(target - currentNode.value)){
        closest=currentNode.value
      }
      if(target>currentNode.value){
        currentNode=currentNode.right
      }else if(target<currentNode.value){
        currentNode=currentNode.left
      }else{
        break
      }
    }
    return closest
  }
  // This is the class of the input tree. Do not edit.
  class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
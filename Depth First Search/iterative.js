class Node {
    constructor(name) {
      this.name = name;
      this.children = [];
    }
  
    addChild(name) {
      this.children.push(new Node(name));
      return this;
    }
  
    depthFirstSearch(array) {
      // Write your code here.
      if(!this) return array
      let stack=[this]
      while (stack.length){
        const currNode = stack.pop()
        array.push(currNode?.name)
        for (let i=currNode?.children?.length-1;i>=0;i--){
          currNode.children[i] && stack.push(currNode.children[i])
        }
      }
      return array
    }
  }
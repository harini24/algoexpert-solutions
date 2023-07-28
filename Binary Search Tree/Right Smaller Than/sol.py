class BST:
    def __init__(self,value,ind):
        self.value=value
        self.ind=ind
        self.left=None
        self.right=None

    def insertNode(self,value,ind):
        curr=self
        while True:
            if value<curr.value:
                if not curr.left:
                    curr.left=BST(value,ind)
                    return
                curr=curr.left
            else:
                if not curr.right:
                    curr.right=BST(value,ind)
                    return
                curr=curr.right
        
def dfsHelper(value,tree,ind):
    ans=0
    print("->",value,ind)
    while tree:
        print(tree.value,tree.ind)
        if tree.value<value and tree.ind>ind:
            ans+=1
        if tree.value<=value:
            ans+=dfsHelper(value,tree.right,ind)
        tree=tree.left
    return ans
def rightSmallerThan(array):
    # Write your code here.
    if len(array) == 0: return []
    root=BST(array[0],0)
    for i in range(1,len(array)):
        root.insertNode(array[i],i)

    ans=[]
    for i in range(len(array)):
        ans.append(dfsHelper(array[i],root,i))
    return ans

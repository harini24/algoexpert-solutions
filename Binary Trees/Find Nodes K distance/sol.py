from collections import defaultdict,deque

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time and space
def findNodesDistanceK(tree, target, k):
    # Write your code here.
    adjList=defaultdict(list)

    def dfs(node,parent):
        if node is None:
            return
        adjList[node.value].append(parent.value)
        adjList[parent.value].append(node.value)
        dfs(node.left,node)
        dfs(node.right,node)
    
    dfs(tree.left,tree)
    dfs(tree.right,tree)
    # print(adjList)
    steps=0
    q=deque()
    q.append(target)
    visited=defaultdict(lambda:False)
    visited[target]=True
    while q:
        size=len(q)
        for i in range(size):
            temp=q.popleft()
            
            for neigh in adjList[temp]:
                if not visited[neigh]:
                    q.append(neigh)
                    visited[neigh]=True
        steps+=1
        if steps==k:
            break
    return list(q)

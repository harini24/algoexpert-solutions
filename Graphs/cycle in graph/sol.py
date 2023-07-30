# O(v+e) time O(v) space

def cycleInGraph(edges):
    # Write your code here.
    visited = [False for _ in edges]
    inStack = [False for _ in edges]

    for edge in range(len(edges)):
        print("->",edge)
        if visited[edge]: continue
        print("-->",edge)
        containsCycle = ifNodeInCycle(edge,edges,visited,inStack)
        if containsCycle:
            return True
    return False

def ifNodeInCycle(node,edges,visited,currentlyInStack):
    print(node,visited,currentlyInStack)
    visited[node] = True
    currentlyInStack[node]=True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = ifNodeInCycle(neighbor,edges,visited,currentlyInStack)
            if containsCycle:
                return True
        elif currentlyInStack[neighbor]:
            return True
            
    currentlyInStack[node]=False
    return False
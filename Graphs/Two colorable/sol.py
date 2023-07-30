def validateBipartite(edges,colors,node):
    print(node,colors)
    for neigh in edges[node]:
        if colors[neigh] == colors[node]:
            return False
        elif colors[neigh] == -1:
            colors[neigh] = 1 - colors[node]
            if not validateBipartite(edges,colors,neigh):
                return False
    return True

# O(v+E) time and O(E) space
def twoColorable(edges):
    # Write your code here.
    colors = [-1]*len(edges)
    for i in range(len(edges)):
        if colors[i] == -1:
            colors[i] = 0 
            if not validateBipartite(edges,colors,i):
                return False
            
    return True

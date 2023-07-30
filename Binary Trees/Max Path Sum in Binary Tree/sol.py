# O(n) time and O(kogn) space
def maxPathSum(tree):
    # Write your code here.
    def helper(node):
        if node is None: return (0,float("-inf") )
        leftTreeBranchSum,leftTreePathSum = helper(node.left)
        rightTreeBranchSum,rightTreePathSum = helper(node.right)
        childBranchSum = max(leftTreeBranchSum,rightTreeBranchSum) 
        currentBranchSum=max(childBranchSum + node.value,node.value)

        currentTreePathSum = max(currentBranchSum , node.value+leftTreeBranchSum+rightTreeBranchSum)
        maxBranchSumSoFar = max(currentTreePathSum,max(leftTreePathSum,rightTreePathSum))
        return (currentBranchSum, maxBranchSumSoFar)
    
    return helper(tree)[1]
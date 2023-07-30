# O(n*n) time and O(n) space
def diskStacking(disks):
    # Write your code here.
    disks.sort(key=lambda x:x[2])
    heights=[disk[2] for disk in disks]
    seq=[None]*len(disks)
    maxHeightInd=0
    for i in range(1,len(disks)):
        for j in range(i):
            if areValidDimensions(disks[j],disks[i]) and heights[i] < heights[j]+disks[i][2]:
                heights[i] = heights[j]+disks[i][2]      
                seq[i]=j
        if heights[i]>heights[maxHeightInd]:
            maxHeightInd=i
    return generateSequence(disks,seq,maxHeightInd)
    
def areValidDimensions(s1,s2):
    return s1[0]<s2[0] and s1[1]<s2[1] and s1[2]<s2[2]

def generateSequence(disks,seq,ind):
    ans=[]
    while ind != None:
        ans.append(disks[ind])
        ind=seq[ind]
    return ans[::-1]
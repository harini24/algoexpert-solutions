def getPath(head,node,path):
    if head is None: return False
    if head.name ==node.name:
        path.append(head)
        return True
    for rep in head.directReports:
        if getPath(rep,node,path):
            path.append(head)
            return True
    return False
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    pathOne=[]
    getPath(topManager,reportOne,pathOne)
    pathTwo=[]
    getPath(topManager,reportTwo,pathTwo)
    i=len(pathOne)-1
    j=len(pathTwo)-1
    while i>=0 and j>=0:
        if pathOne[i].name==pathTwo[j].name:
            i-=1
            j-=1
        else:
            break
    return pathOne[i+1]


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

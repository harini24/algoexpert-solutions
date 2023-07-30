def countSquares(points):
    # Write your code here.
    hash={}
    n=len(points)
    if n<4: return 0
    for point in points:
        val=str(point[0])+"-"+str(point[1])
        hash[val]=True
    count=0
    for i in range(n):
        for j in range(n):
            if points[i]==points[j]: continue
            x1,y1=points[i]
            x2,y2=points[j]
            xMid=(x1+x2)/2
            yMid=(y1+y2)/2

            xDist = xMid-x1
            yDist = yMid-y1

            point1 = pointToString([xMid+yDist,yMid-xDist])
            point2 = pointToString([xMid-yDist,yMid+xDist])
            if point1 in hash and point2 in hash:
                print(i,j,point1,point2)
                
                count+=1

            
            
    return count/4

def pointToString(point):
    if point[0]%1 == 0 and point[1]%1==0:
        return str(int(point[0]))+'-'+str(int(point[1]))
    return str(point[0])+'-'+str(point[1])
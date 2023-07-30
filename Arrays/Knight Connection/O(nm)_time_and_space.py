from collections import deque
def knightConnection(knightA, knightB):
    # Write your code here.
    moves=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
    q=deque()
    q.append([knightA[0],knightA[1],0])
    visited={positionToString(knightA)}
    while q:
        currPos=q.popleft()
        if currPos[0]==knightB[0] and currPos[1]==knightB[1]:
            return (currPos[2]+1)//2

        for x,y in moves:
            dx=currPos[0]+x
            dy=currPos[1]+y
            posString = positionToString([dx,dy])
            if posString not in visited:
                q.append([dx,dy,currPos[2]+1])
                visited.add(posString)
                


def positionToString(pos):
    return ",".join(map(str,pos))
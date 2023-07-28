# O(n*n + m) time and O(n+m) space

def patternMatcher(pattern, string):
    # Write your code here.
    if len(pattern) > len(string): return []
    newPattern = getNewPatten(pattern)
    hasSwitch = pattern[0] != newPattern[0]
    counts={'x':0,'y':0}
    firstYPos = countFrequencies(counts,newPattern)
    print(firstYPos)
    n=len(string)
    if counts['y'] != 0:
        for lenOfX in range(1,n):
            lenOfY = (n - (lenOfX*counts['x'])) / counts['y']
            if lenOfY == 0 or lenOfY%1 != 0:
                continue
            lenOfY=int(lenOfY)
            x=string[:lenOfX]
            yInd=lenOfX*firstYPos
            y=string[yInd:yInd+lenOfY]
            potentialMatch = map(lambda char: x if char=='x' else y,newPattern)
            print(x,y,firstYPos)
            if string == "".join(potentialMatch):
                return [x,y] if not hasSwitch else [y,x]
    else:
        xCount = counts['x']
        if n % xCount == 0:
            lenOfX= n//xCount
            x=string[:lenOfX]
            potentialMatch = [x for _ in pattern]
            if string == "".join(potentialMatch):
                return [x,""] if not hasSwitch else ["",x]
    return []
                
            


def countFrequencies(count,string):
    yPos=None
    for i,char in enumerate(string):
        count[char]+=1
        if char == 'y' and yPos is None:
            yPos=i
    return yPos
        
    
def getNewPatten(pattern):
    if pattern[0] == 'x':
        return pattern
    else:
        val ="".join(list(map(lambda char: 'x' if char == 'y' else 'y',pattern)))
        return val
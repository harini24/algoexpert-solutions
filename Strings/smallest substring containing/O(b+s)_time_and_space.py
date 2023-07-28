# b, s- len of big string and small string
from collections import Counter
def smallestSubstringContaining(big, small):
    # Write your code here.
    m=len(big)
    n=len(small)
    if n>m: return ""
    hash = Counter(small)
    i,j=0,0
    start=0
    end=m-1
    count=n
    minLength = float("inf")
    found=False
    while j<=m:
        if count != 0:
            if j>=m:
                break
            if big[j] in hash:
                hash[big[j]]-=1
                if hash[big[j]]>=0:
                    count-=1
            j+=1
        else:
            if j-i < minLength:
                found=True
                minLength = j-i
                start=i
                end=j
            if big[i] in hash:
                hash[big[i]]+=1
                if hash[big[i]]>0:
                    count+=1
            i+=1

    return big[start:end] if found else ""

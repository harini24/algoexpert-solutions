def longestSubstringWithoutDuplication(string):
    # Write your code here.
    if len(string) <=1: return string
    i,j=0,0
    ind=None
    range=0
    chars=set()
    while j<len(string):
        print(i,j,string[i:j+1])
        if string[j] not in chars:
            chars.add(string[j])
            if j-i+1 > range:
                print("here",range,j-i+1)
                range = j-i+1
                ind=[i,j]
            j+=1
        else:
            chars.remove(string[i])
            i+=1
    return string[ind[0]:ind[1]+1]
# n- len(strings) 
# m - max num of char in a strings val
# c - unique characts in strings
def commonCharacters(strings):
    # Write your code here
    ret=[]
    charCount={}
    for string in strings:
        uniquechars = set(string)
        for char in uniquechars:
            if char not in charCount:
                charCount[char]=0
            charCount[char] += 1

    for word, occ in charCount.items():
        if occ == len(strings):
            ret.append(word)
    
    return ret
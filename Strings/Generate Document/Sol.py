# O(n+m) time and O(c) space
# n - number of characters
# m - length of document
# c - number of unique chars in characters

def generateDocument(characters, document):
    # Write your code here.
    charCounts={}

    for char in characters:
        if char not in charCounts:
            charCounts[char]=0
        charCounts[char]+=1

    for char in document:
        if char not in charCounts or charCounts[char] == 0: return False
        charCounts[char]-=1
        
    return True
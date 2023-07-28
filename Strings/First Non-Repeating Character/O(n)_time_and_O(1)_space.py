def firstNonRepeatingCharacter(string):
    # Write your code here.
    charFreq = {}

    for char in string:
        charFreq[char] = charFreq.get(char,0) + 1

    for ind in range(len(string)):
        char=string[ind]
        if charFreq[char] == 1:
            return ind
            
    return -1
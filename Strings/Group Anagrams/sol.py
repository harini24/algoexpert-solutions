# O(w*nlogn) time and (wn) space
# w - number of words
# n - longest word len

def groupAnagrams(words):
    # Write your code here.
    if len(words) ==0:
        return []
    hashmap={}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in hashmap:
            hashmap[sortedWord].append(word)
        else:
            hashmap[sortedWord] = [word]
    return list(hashmap.values())

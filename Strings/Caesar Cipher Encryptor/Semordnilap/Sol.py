# O(n*m) time and space
# n - number of words
# m - length of longest word in word

def semordnilap(words):
    # Write your code here.
    wordsSet=set(words)
    ret=[]
    for word in words:
        reversed=word[::-1]
        if reversed in wordsSet and reversed != word:
            ret.append([word,reversed])
            wordsSet.remove(word)
            wordsSet.remove(reversed)
    return ret

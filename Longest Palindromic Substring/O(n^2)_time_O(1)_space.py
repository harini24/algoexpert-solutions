def longestPalindromicSubstring(string):
    # Write your code here.
    currRange=[0,1]
    for i in range(len(string)-1):
        odd = palindromeHelper(string,i,i)
        even = palindromeHelper(string,i,i+1)
        longest = even if even[1]-even[0]>odd[1]-odd[0] else odd  
        currRange = currRange if currRange[1]-currRange[0]>longest[1]-longest[0] else longest  
    return string[currRange[0]:currRange[1]]

def palindromeHelper(string,i,j):
    while i>=0 and j<len(string) and string[i]==string[j]:
        i-=1
        j+=1
    return [i+1,j]
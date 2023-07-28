def reverseWordsInString(string):
    # Write your code here.
    word=''
    spaces=''
    ret=""
    i=0
    while i<len(string):
        print(string[i],ord(string[i]))
        if ord(string[i]) != 32:
            word+=string[i]
            i+=1
        else:
            ret = word+ret
            word=""
            while i<len(string) and ord(string[i]) == 32:
                ret = string[i]+ret
                i+=1
    ret = word+ret
    return ret

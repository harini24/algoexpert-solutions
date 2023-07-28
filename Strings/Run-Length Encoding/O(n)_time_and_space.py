def runLengthEncoding(string):
    # Write your code here.
    ret=[]
    count=0
    word=string[0]
    for char in string:
        if count ==9 or word !=char:
            ret.append(str(count))
            ret.append(word)
            word=char
            count=0
        count+=1
    ret.append(str(count))
    ret.append(word)
    return "".join(ret)

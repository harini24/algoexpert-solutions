def shortenPath(path):
    # Write your code here.
    paths=filter(isImportantToken,path.split("/"))
    
    stack=[]
    # print(list(paths))
    if path[0] == "/":
        stack.append("")
    for val in paths:
        if val == "..":
            if len(stack)==0 or stack[-1] == "..":
                stack.append(val)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(val)
    if len(stack) ==1 and stack[-1] == "":
        return "/"
    return ("/").join(stack)

def isImportantToken(token):
    return len(token)>0 and token !="."
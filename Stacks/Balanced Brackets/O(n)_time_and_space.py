def balancedBrackets(string):
    # Write your code here.
    opening="{[("
    closing="}])"
    matches={
        "}":"{",
        "]":"[",
        ")":"("
    }
    arr=[]

    for char in string:
        if char in opening:
            arr.append(char)
        elif char in closing:
            if len(arr) == 0:
                return False
            elif arr[-1] != matches[char]:
                return False
            else:
                arr.pop()
    return len(arr) == 0

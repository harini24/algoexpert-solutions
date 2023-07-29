def bestDigits(number, numDigits):
    # Write your code here.
    stack=[]
    for digit in number:
        while numDigits>0 and stack and stack[-1]<digit:
            numDigits-=1
            stack.pop()
        stack.append(digit)

    while numDigits>0:
        numDigits-=1
        stack.pop()

    return "".join(stack)

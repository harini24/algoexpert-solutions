
def oneEdit(stringOne, stringTwo):
    # Write your code here.
    lengthOne = len(stringOne)
    lengthTwo = len(stringTwo)
    if abs(lengthOne-lengthTwo)>1:
        return False

    ind1=0
    ind2=0
    editMade=False
    while ind1<lengthOne and ind2<lengthTwo:
        if stringOne[ind1] != stringTwo[ind2]:
            if editMade:
                return False
            editMade=True

            if lengthOne>lengthTwo:
                ind1+=1
            elif lengthTwo>lengthOne:
                ind2+=1
            else:
                ind1+=1
                ind2+=1
        else:
            ind1+=1
            ind2+=1
    return True

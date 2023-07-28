def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters=[]
    key=key%26
    for char in string:
        newLetters.append(getNewLetter(char,key))

    return "".join(newLetters)

def getNewLetter(letter,key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode<=122 else chr(96 +(newLetterCode%122))
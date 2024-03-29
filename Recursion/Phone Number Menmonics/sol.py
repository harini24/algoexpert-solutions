mnem={
    '0':['0'],
    '1':['1'],
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}

# O(n*(4^n)) time and O(n) space
# n - length of phone number
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    if int(phoneNumber) <2: return [phoneNumber]
    arr=[]
    helper(phoneNumber,0,arr,"")
    return arr

def helper(num,ind,arr,pattern):
    if len(pattern) == len(num): 
        arr.append(pattern)
        return
    for char in mnem[num[ind]]:
        helper(num,ind+1,arr,pattern+char)
        
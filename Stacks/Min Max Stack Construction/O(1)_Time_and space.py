# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack=[]
        self.minMaxStack=[]
        
    # O(1) time and space
    def peek(self):
        return self.stack[-1]

    # O(1) time and space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time and space
    def push(self, number):
        newMinMax={"min":number,"max":number}
        if self.minMaxStack:
            lastVal= self.minMaxStack[-1]
            newMinMax["min"] = min(number,lastVal["min"])
            newMinMax["max"] = max(number,lastVal["max"])
        self.stack.append(number)
        self.minMaxStack.append(newMinMax)

    # O(1) time and space
    def getMin(self):
        return self.minMaxStack[-1]["min"]

    # O(1) time and space
    def getMax(self):
        return self.minMaxStack[-1]["max"]

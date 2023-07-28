# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # avg O(nlogn) time and space
    # wrst O(n) time and space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value<self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
            
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
            
        return self

    # avg O(nlogn) time and space
    # wrst O(n) time and space
    def contains(self, value):
        # Write your code here.
        if value==self.value:
            return True
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            if self.left is None:
                 return False
            else:
                return self.left.contains(value)

    # avg O(nlogn) time and space
    # wrst O(n) time and space
    def remove(self, value,parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        # print(self,self.value,value)
        if value>self.value:
            if self.right is not None:
                self.right.remove(value,self)
        elif value<self.value:
            if self.left is not None:
                self.left.remove(value,self)
        else:
            if self.left is not None and self.right is not None:
                self.value=self.right.getMinValue()
                # print(self.value)
                self.right.remove(self.value,self)     
            elif parent is None:
                if self.left is not None:
                    self.value=self.left.value
                    self.right=self.left.right
                    self.left=self.left.left
                elif self.right is not None:
                    self.value=self.right.value
                    self.left=self.right.left
                    self.right=self.right.right
                else:
                    pass
                   
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            else:
                parent.right = self.left if self.left is not None else self.right
                
        return self
        
    def getMinValue(self):
        # print(self,self.value,self.left,self.right)
        if self.left is None:
            # print("here")
            return self.value
        else:
            return self.left.getMinValue()

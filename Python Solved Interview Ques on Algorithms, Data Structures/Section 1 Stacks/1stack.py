class Stack:
    
    def __init__(self):
        self.stackArray = list()
        self.maxLimit = 8
        self.top = 0
    
    def push(self,element):
        if self.top>=self.maxLimit:
            return ("The Stack Is Full")
        self.stackArray.append(element)
        self.top += 1
        
    def pop(self):
        if self.top<=0:
            return ("The Stack Array Is Empty")
        item = self.stackArray.pop()
        self.top -= 1
        return item
        
    def size(self):
        return self.top

stackObject = Stack()
stackObject.push(1)
stackObject.push(2)
stackObject.push(3)
stackObject.push(4)
stackObject.push(5)
stackObject.push(6)
stackObject.push(7)
stackObject.push(8)
stackObject.push(9)
print("size of stack:", stackObject.size())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())

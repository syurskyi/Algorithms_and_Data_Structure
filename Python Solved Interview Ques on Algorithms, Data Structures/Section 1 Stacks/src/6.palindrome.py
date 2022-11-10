class Stack:
    #Constructor function
    def __init__(self):
        self.stackArray = list()
        self.maxLimit = 10 
        self.top = 0

    #Insert element into the Stack
    def push(self,element):
        if self.top>=self.maxLimit:
            return ("The Stack Array Is Full!")
        self.stackArray.append(element)
        self.top += 1

    #Remove element from the stack
    def pop(self):
        if self.top<=0:
            return ("The Stack Array Is Empty!")
        item = self.stackArray.pop()
        self.top -= 1
        return item

    #return the size of the stack
    def size(self):
        return self.top

    def isEmpty(self):
        return len(self.stackArray) <= 0

def isPalindrome(str):
  print "input:", str
  strStack = Stack()
  palindrome = False
  for char in str:
    strStack.push(char)
  for char in str:
    if char == strStack.pop():
       palindrome = True
    else:
       palindrome = False

  return palindrome

print isPalindrome("12321")
#print isPalindrome("malayalam")

from pprint import pprint


class Stack:
    #Constructor function
    def __init__(self, items=[]):
        self.stackArray = items 

    #Insert element into the Stack
    def push(self,element):
        return self.stackArray.append(element)

    #Remove element from the stack
    def pop(self):
        return self.stackArray.pop() 

    def isEmpty(self):
        return not self.stackArray

    def __repr__(self):
        return "Stack {0}".format(self.stack)

def reverseStack(stack):
  def reverseStackRecursive(stack, newStack=Stack()):
     if not stack.isEmpty():
        newStack.push(stack.pop())
        reverseStackRecursive(stack, newStack)
     return newStack

  return reverseStackRecursive(stack)

stk=Stack(range(3))
pprint(vars(stk))
pprint (vars(reverseStack(stk)))

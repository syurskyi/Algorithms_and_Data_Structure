# Write a program to convert infix expression to postfix expression
# Implementation:
# 3 arrays\storage units:
# Postfix array: contains the operands(ex: A, B, C)
# Stack array: contains the operators(ex: +, *)
# Precedence dict: contains the priority values for different operators
# We will use this to decide whether the stack's top element(operator)
# should be appended to the postfix array or the parsed operator
# to be pushed to stack
# For each element in the infix expression ( A + B * C)
# {
#   if the element is operand, append it in the output postfix array
# else if the element is '(', push it on the stack
# else if the element is ')', then get all the elements
# from the stack and append it to the output postfix array
# else if the element is a operator, then get the priority value
# of this operator

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def iTop(infixexpr):
    print("input:",infixexpr)
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stackObject = Stack()
    postfixArray = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixArray.append(token)
        elif token == '(':
            stackObject.push(token)
        elif token == ')':
            topToken = stackObject.pop()
            while topToken != '(':
                postfixArray.append(topToken)
                topToken = stackObject.pop()
        else:
            while (not stackObject.isEmpty()) and \
               (prec[stackObject.peek()] >= prec[token]):
                  postfixArray.append(stackObject.pop())
            stackObject.push(token)

    while not stackObject.isEmpty():
        postfixArray.append(stackObject.pop())
    return " ".join(postfixArray)

myarray="A + B * C "
print(iTop(myarray))

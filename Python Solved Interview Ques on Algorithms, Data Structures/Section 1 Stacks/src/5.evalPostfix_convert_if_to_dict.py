class Stack:
    def __init__(self):
        self.stackArray = list()
        self.maxLimit = 8
        self.top = 0

    def push(self,element):
        if self.top>=self.maxLimit:
            return ("The Stack Array Is Full!")
        self.stackArray.append(element)
        self.top += 1

    def pop(self):
        if self.top<=0:
            return ("The Stack Array Is Empty!")
        item = self.stackArray.pop()
        self.top -= 1
        return item

    def size(self):
        return self.top

    def isEmpty(self):
        return len(self.stackArray) <= 0


def pfEval(postfixExpr):
    print("input:", postfixExpr)
    stackObject = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            stackObject.push(int(token))
        else:
            operand2 = stackObject.pop()
            operand1 = stackObject.pop()
            result = doMath(token,operand1,operand2)
            stackObject.push(result)
    return stackObject.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(pfEval('1 2 3 * +'))


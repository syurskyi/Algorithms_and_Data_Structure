class Stack:
    def __init__(self):
        self.items = []     # list

    def isEmpty(self):
        return self.items == []    # list

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def iTop(infixexpr):
    print("input:", infixexpr)
    prec = {}   # dict
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stackObject = Stack()
    postfixArray = []   # list
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixArray.append(token)
        elif token is '(':
            stackObject.push(token)
        elif token is ')':
            topToken = stackObject.pop()
            while topToken != '(':
                postfixArray.append(topToken)
                topToken = stackObject.pop()
        else:
            while not stackObject.isEmpty() and \
               (prec[stackObject.peek()] >= prec[token]):
                  postfixArray.append(stackObject.pop())
            stackObject.push(token)

    while not stackObject.isEmpty():
        postfixArray.append(stackObject.pop())
    return " ".join(postfixArray)

myarray = "A + B * C)"
print(iTop(myarray))

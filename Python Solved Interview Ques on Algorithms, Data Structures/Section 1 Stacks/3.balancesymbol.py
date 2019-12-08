class Stack:
    def __init__(self):
        self.items = []
         
    def push(self, item):
        self.items.append(item)
         
    def pop(self):
        return self.items.pop()
     
    def isEmpty(self):
        return (self.items == [])
     
    def peek(self):
        return self.items[-1]
     
    def __str__(self):
        return str(self.items)


def symbolmatch(top, symbol):
    startSymbols = "({["
    closeSymbols = ")}]"
    return startSymbols.index(top) == closeSymbols.index(symbol)
 
 
def balancesymbol(input):
    print("input:", input)
    stackObject = Stack()
    balanced = 0
    for symbols in input:
        if symbols in ["(", "{", "["]:
            stackObject.push(symbols)
        else:
            if stackObject.isEmpty():
                balanced = 0
            else:
                topSymbol = stackObject.pop()
                if not symbolmatch(topSymbol, symbols):
                    balanced = 0
                else:
                    balanced = 1
                     
    return balanced
 

print(balancesymbol("{([])}"))


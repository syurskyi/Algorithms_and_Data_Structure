c_ Stack:

    ___ -
        stack _ []

    ___ isEmpty
        r_ stack == []

    ___ push data
        stack.append(data)

    ___ pop
        data _ stack[-1]
        del stack[-1]
        r_ data

    ___ peek
        r_ stack[-1]

    ___ sizeStack
        r_ len(stack)


stack _ Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek:", stack.peek())
print(stack.sizeStack())

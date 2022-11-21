
class Stack:

    ? ? __init__(self):
        self.stack _ []

    # O(1) running time
    ? ? is_empty(self):
        r_ self.stack __ []

    # O(1) running time
    ? ? push(self, data):
        self.stack.append(data)

    # O(1) because we manipulate the last item
    ? ? pop(self):

        __ self.size_stack < 1:
            r_ None

        data _ self.stack[-1]
        del self.stack[-1]
        r_ data

    # O(1) constant running time
    ? ? peek(self):
        r_ self.stack[-1]

    # O(1)
    ? ? size_stack(self):
        r_ l..(self.stack)

# %%
'''
# Implement a Stack
A very common interview question is to begin by just implementing a Stack! Try your best to implement your own stack!
It should have the methods:

* Check if its empty
* Push a new item
* Pop an item
* Peek at the top item
* Return the size
'''

# %%
class Stack(object):
    # Fill out the Stack Methods here
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, e):
        self.items.append(e)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[self.size()-1] # reuse the size funtion
    pass

# %%
stack = Stack()

# %%
stack.size()

# %%
stack.push(1)

# %%
stack.push(2)

# %%
stack.push('Three')

# %%
stack.pop()

# %%
stack.pop()

# %%
stack.size()

# %%
stack.isEmpty()

# %%
stack.peek()

# %%

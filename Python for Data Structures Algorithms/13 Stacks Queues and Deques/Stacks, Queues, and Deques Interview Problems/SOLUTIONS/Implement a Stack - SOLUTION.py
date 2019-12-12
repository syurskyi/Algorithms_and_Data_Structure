# %%
'''
# Implement a Stack -SOLUTION
**Please refer to the lecture on implementation for a full explanation. Here is the code from that lecture:**
'''

# %%
class Stack(object):
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
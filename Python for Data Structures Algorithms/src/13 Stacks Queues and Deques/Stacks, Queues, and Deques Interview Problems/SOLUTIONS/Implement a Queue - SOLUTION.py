# %%
'''
# Implement a Queue - SOLUTION
**Please refer to the Implementation of Queue lecture for a full explanation. The code from that lecture is below:**
'''

# %%
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
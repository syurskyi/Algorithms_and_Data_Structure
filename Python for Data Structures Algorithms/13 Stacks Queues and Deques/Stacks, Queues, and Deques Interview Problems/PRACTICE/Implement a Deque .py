# %%
'''
# Implement a Deque
Finally, implement a Deque class! It should be able to do the following:
* Check if its empty
* Add to both front and rear
* Remove from Front and Rear
* Check the Size
'''

# %%
class Deque(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, e):
        self.items.insert(0, e)
    def add_rear(self, e):
        self.items.append(e)
    def remove_front(self):
        return self.items.pop(0)
    def remove_rear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    pass

# %%
deq = Deque()

# %%
deq.size()

# %%
deq.add_front(2)

# %%
deq.add_front(1)

# %%
deq.add_rear(3)

# %%
deq.remove_front()

# %%
deq.remove_rear()

# %%
deq.remove_rear()

# %%
deq.is_empty()

# %%

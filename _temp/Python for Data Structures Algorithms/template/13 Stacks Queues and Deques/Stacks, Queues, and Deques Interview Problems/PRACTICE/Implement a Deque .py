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
c_ Deque o..
    ___ -
        items _ []
    ___ is_empty
        r_ items == []
    ___ add_front e
        items.insert(0, e)
    ___ add_rear e
        items.append(e)
    ___ remove_front
        r_ items.pop(0)
    ___ remove_rear
        r_ items.pop()
    ___ size
        r_ len(items)
    pass

# %%
deq _ Deque()

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

# %%
'''
# Implementation of Deque
In this lecture we will implement our own Deque class!
## Methods and Attributes
* Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
* addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
* addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
* removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
* removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
* isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
* size() returns the number of items in the deque. It needs no parameters and returns an integer.

## Deque Implementation
'''

# %%
c_ Deque:
    ___ -  
        items _    # list

    ___ isEmpty 
        r_ items __    # list

    ___ addFront item
        items.a..(item)

    ___ addRear item
        items.insert(0,item)

    ___ removeFront 
        r_ items.pop()

    ___ removeRear 
        r_ items.pop(0)

    ___ size 
        r_ l..(items)

# %%
d _ Deque()

# %%
d.addFront('hello')

# %%
d.addRear('world')

# %%
d.size()

# %%
print d.removeFront() + ' ' +  d.removeRear()

# %%
d.size()

# %%
'''
## Good Job!
'''
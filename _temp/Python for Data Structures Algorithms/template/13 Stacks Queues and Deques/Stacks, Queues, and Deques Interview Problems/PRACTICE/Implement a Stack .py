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
c_ Stack o..
    # Fill out the Stack Methods here
    ___ -  
        items _ []
    ___ isEmpty 
        r_ len(items) == 0
    ___ push e
        items.append(e)
    ___ pop 
        r_ items.pop()
    ___ size 
        r_ len(items)
    ___ peek 
        r_ items[size()-1] # reuse the size funtion
    pass

# %%
stack _ Stack()

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

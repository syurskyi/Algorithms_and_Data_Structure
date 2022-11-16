# %%
'''
# Implement a Queue
It's very common to be asked to implement a Queue class! The class should be able to do the following:
* Check if Queue is Empty
* Enqueue
* Dequeue
* Return the size of the Queue
'''

# %%
c_ Queue o..
    ___ -  
        items _    # list
    ___ is_empty 
        r_ items __    # list
    ___ enqueue e
        items.insert(0, e)
    ___ dequeue 
        r_ items.p.. 
    ___ size 
        r_ l..(items)
    pass

# %%
q _ Queue()
q.is_empty()
q.enqueue(1)
q.enqueue('two')
q.enqueue(3)
q.size()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.is_empty()

# %%

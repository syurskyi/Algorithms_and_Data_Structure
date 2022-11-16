# %%
'''
# Implement a Queue - SOLUTION
**Please refer to the Implementation of Queue lecture for a full explanation. The code from that lecture is below:**
'''

# %%
c_ Queue:
    ___ -
        items _    # list

    ___ isEmpty
        r_ items __    # list

    ___ enqueue item
        items.insert(0,item)

    ___ dequeue
        r_ items.pop()

    ___ size
        r_ l..(items)
# %%
'''
# Implement a Deque - SOLUTION
**Please refer to the Implementation of Deque lecture for a full explanation. The code from that lecture is below:**
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
# %%
'''
# Implement a Queue - Using Two Stacks - SOLUTION
Given the Stack class below, implement a Queue class using **two** stacks! Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
'''

# %%
stack1 _    # list
stack2 _    # list

# %%
'''
## Solution
The key insight is that a stack reverses order (while a queue doesn't). A sequence of elements pushed on a stack comes 
back in reversed order when popped. Consequently, two stacks chained together will return elements in the same order, 
since reversed order reversed again is original order.
 We use an in-stack that we fill when an element is enqueued and the dequeue operation takes elements from an out-stack. 
 If the out-stack is empty we pop all elements from the in-stack and push them onto the out-stack. 
'''

# %%
c_ Queue2Stacks o..
    
    ___ -  
        
        # Two Stacks
        instack _    # list
        outstack _    # list
     
    ___ enqueueelement
        
        # Add an enqueue with the "IN" stack
        instack.a..(element)
    
    ___ dequeue 
        __ n.. outstack:
            _____ instack:
                # Add the elements to the outstack to reverse the order when called
                outstack.a..(instack.pop())
        r_ outstack.p.. 

# %%
'''
# Test Your Solution
You should be able to tell with your current knowledge of Stacks and Queues if this is working as it should. 
For example, the following should print as such:
'''

# %%
"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q _ Queue2Stacks()

___ i __ xrange(5
    q.enqueue(i)
    
___ i __ xrange(5
    print q.dequeue()

# %%
'''
## Good Job!
'''
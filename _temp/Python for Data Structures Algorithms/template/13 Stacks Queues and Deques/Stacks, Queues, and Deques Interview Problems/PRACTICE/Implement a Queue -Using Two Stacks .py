# %%
'''
# Implement a Queue - Using Two Stacks
Given the Stack class below, implement a Queue class using **two** stacks! Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
'''

# %%
# Uses lists instead of your own Stack class.
stack1 _    # list
stack2 _    # list

# %%
'''
## Solution

Fill out your solution below:
'''

# %%
c_ Queue2Stacks o..
    
    ___ -  
        
        # Two Stacks
        in_stack _    # list
        out_stack _    # list
     
    ___ enqueue element
        # FILL OUT CODE HERE
        in_stack.a..(element)
        pass
    
    ___ dequeue 
        
        # FILL OUT CODE HERE
        __ n.. out_stack:
            _____ in_stack:
                out_stack.a..(in_stack.pop())
        r_ out_stack.p.. 
        pass

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

___ i __ r..(5
    q.enqueue(i)
    
___ i __ r..(5
    print (q.dequeue())

# %%
'''
## Good Job!
'''
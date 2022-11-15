# %%
'''
# Implement a Queue - Using Two Stacks
Given the Stack class below, implement a Queue class using **two** stacks! Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
'''

# %%
# Uses lists instead of your own Stack class.
stack1 = []
stack2 = []

# %%
'''
## Solution

Fill out your solution below:
'''

# %%
class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        
        # FILL OUT CODE HERE
        pass
    
    def dequeue(self):
        
        # FILL OUT CODE HERE
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
q = Queue2Stacks()

for i in xrange(5):
    q.enqueue(i)
    
for i in xrange(5):
    print q.dequeue()

# %%
'''
## Good Job!
'''
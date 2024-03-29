# # %%
# '''
# # Implementation of Queue
# In this lecture we will build on our previous understanding of Queues by implementing our own class of Queue!
# '''
#
# # %%
# '''
# ____
# ## Queue Methods and Attributes
#
# Before we begin implementing our own queue, let's review the attribute and methods it will have:
#
# * Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
# * enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
# * dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
# * isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
# * size() returns the number of items in the queue. It needs no parameters and returns an integer.
# '''
#
# # %%
# '''
# ____
# ## Queue Implementation
# '''
#
# # %%
# c_ Queue
#     ___ -
#         items _    # list
#
#     ___ isEmpty
#         r_ ? __    # list
#
#     ___ enqueue item
#         ?.i..  0 ?
#
#     ___ dequeue
#         r_ ?.p..
#
#     ___ size
#         r_ l.. ?
#
# # %%
# q _ Queue()
#
# # %%
# q.size()
#
# # %%
# q.isEmpty()
#
# # %%
# q.enqueue(1)
#
# # %%
# q.dequeue()
#
# # %%
# '''
# ## Good Job!
# '''
# # Implementation of Stack
# # Stack Attributes and Methods
# #
# # Before we implement our own Stack class, let's review the properties and methods of a Stack.
# #
# # The stack abstract data type is defined by the following structure and operations. A stack is structured,
# # as described above, as an ordered collection of items where items are added to and removed from the end called
# # the top. Stacks are ordered LIFO. The stack operations are given below.
# #
# #     Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# #     push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# #     pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# #     peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not
# #     modified.
# #     isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# #     size() returns the number of items on the stack. It needs no parameters and returns an integer.
# #
# # Stack Implementation
#
# c_ Stack
#
#     ___ -
#         items _    # list
#
#     ___ isEmpty
#         r_ ? __    # list
#
#     ___ push item
#         ?.a.. ?
#
#     ___ pop
#         r_ ?.p..
#
#     ___ peek
#         r_ ? l.. ? - 1]
#
#     ___ size
#         r_ l.. ?
#
# # Let's try it out!
#
# s _ Stack()
#
# print s.isEmpty()
# # True
#
# s.push(1)
# s.push('two')
# s.peek()
# # 'two'
#
# s.push(T..)
# s.size()
# # 3
#
# # s.isEmpty()
# F..
#
# s.p..
# # True
#
# s.p..
# # two
#
# s.size()
# # 1
#
# s.p..
# # 1
#
# s.isEmpty()
# # True
# #   Created by Elshad Karimov on 04/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Implement a queue using two stacks.
#
# c_ Stack
#   ___ -
#     list _    # list
#
#   ___ -l
#     r_ l.. ?
#
#   ___ push item
#     ?.a.. ?
#
#   ___ pop
#     __ l.. ? __ 0
#       r_ N..
#     r_ ?.p..
#
# c_ QueueviaStack
#   ___ -
#     inStack _ ?
#     outStack _ ?
#
#   ___ enqueue item
#     i__.p.. ?
#
#   ___ dequeue
#     _____ l.. i.
#       o__.p.. i__.p..
#     result _ o__.p..
#     _____ l.. ?
#       i__.p.. o__.p..
#     r_ ?
#
#
# customQueue _ QueueviaStack()
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue.dequeue())
# customQueue.enqueue(4)
# print(customQueue.dequeue())
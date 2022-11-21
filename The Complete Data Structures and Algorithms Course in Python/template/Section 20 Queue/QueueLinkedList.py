# #   Created by Elshad Karimov on 30/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
#
# c_ Node
#     ___ -  value_N..
#         ? _ ?
#         n.. _ N..
#
#     ___ -s
#         r_ s.. ?
#
# c_ LinkedList
#     ___ -
#         h.. _ N..
#         t.. _ N..
#
#     ___ -i..
#         curNode _ ?
#         _____ ?
#             y.. ?
#             c.. _ ?.n..
#
# c_ Queue
#     ___ -
#         linkedList _ ?
#
#     ___ -s
#         values _ s..(x) ___ ? __ ?
#         r_ ' '.j.. ?
#
#     ___ enqueue value
#         newNode _ ? ?
#         __ ?.h.. __ N..
#             ?.h.. _ ?
#             ?.t.. _ ?
#         ____
#             ?.?.n.. _ ?
#             ?.t.. _ ?
#
#     ___ isEmpty
#         __ ?.h.. __ N..
#             r_ T..
#         ____
#             r_ F..
#
#     ___ dequeue
#         __ ?
#             r_ "There is not any node in the Queue"
#         ____
#             tempNode _ ?.h..
#             __ ?.h.. __ ?.t..
#                 ?.h.. _ N..
#                 ?.t.. _ N..
#             ____
#                 ?.h.. _ ?.?.n..
#             r_ ?
#
#     ___ peek
#         __ ?
#             r_ "There is not any node in the Queue"
#         ____
#             r_ ?.h..
#
#     ___ delete
#         ?.h.. _ N..
#         ?.t.. _ N..
#
#
#
#
# custQueue _ Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)
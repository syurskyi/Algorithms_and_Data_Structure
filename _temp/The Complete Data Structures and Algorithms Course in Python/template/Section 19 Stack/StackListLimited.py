# #   Created by Elshad Karimov on 22/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ Stack:
#     ___ -  maxSize
#         ? _ ?
#         list _    # list
#
#     ___ -s
#         values _ ?.r..
#         values _  s..(x) ___ ? __ ?
#         r_ '\n'.j.. ?
#
#     # isEmpty
#     ___ isEmpty
#         __ list __    # list:
#             r_ T..
#         ____
#             r_ F..
#
#     # isFull
#     ___ isFull
#         __ l.. ? __ ?
#             r_ T..
#         ____
#             r_ F..
#
#     #  Push
#     ___ push value
#         __ ?
#             r_ "The stack is full"
#         ____
#             ?.a.. ?
#             r_ "The element has been successfully inserted"
#     # Pop
#     ___ pop
#         __ ?
#             r_ "There is not any element in the stack"
#         ____
#             r_ ?.p..
#
#     # peek
#     ___ peek
#         __ ?
#             r_ "There is not any element in the stack"
#         ____
#             r_ l.. l.. l..-1
#
#     #  delete
#     ___ delete
#         list _ N..
#
#
# customStack _ Stack(4)
# print(customStack.isEmpty())
# print(customStack.isFull())
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
#
#
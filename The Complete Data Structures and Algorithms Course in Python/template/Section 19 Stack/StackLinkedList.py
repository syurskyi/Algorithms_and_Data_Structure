# #   Created by Elshad Karimov on 23/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ Node:
#     ___ -  value _ N..
#         ? _ ?
#         n.. _ N..
#
# c_ LinkedList
#     ___ -
#         h.. _ N..
#
#     ___ -i..
#         curNode _ ?
#         _____ ?
#             y.. ?
#             c.. _ ?.n..
#
# c_ Stack
#     ___ -
#         LinkedList _ ?
#
#     ___ -s
#         values _  s.. x.v.. ___ ? __ ?
#         r_ '\n'.j.. ?
#
#     ___ isEmpty
#         __ ?.h.. __ N..
#             r_ T..
#         ____
#             r_ F..
#
#     ___ push value
#         node _ ? ?
#         ?.n.. _ ?.h..
#         ?.h.. _ ?
#
#     ___ pop
#         __ ?
#             r_ "There is not any element in the stack"
#         ____
#             nodeValue _ ?.h__.v..
#             ?.h.. _ ?.?.n..
#             r_ n?
#
#     ___ peek
#         __ ?
#             r_ "There is not any element in the stack"
#         ____
#             nodeValue _ ?.h__.v..
#             r_ ?
#
#     ___ delete
#         ?.h.. _ N..
#
#
#
#
# customStack _ Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
#
# print(customStack.peek())
#

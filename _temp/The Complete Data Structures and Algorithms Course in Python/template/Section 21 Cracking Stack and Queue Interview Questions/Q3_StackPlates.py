# #   Created by Elshad Karimov on 02/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Stack of Plates
#
# c_ PlateStack
#     ___ -  capacity
#         ? _ ?
#         stacks _    # list
#
#     ___ -s
#         r_ ?
#
#     ___ push item
#         __ l.. ? > 0 ___ (l..(? -1 < ?
#             ? -1 .a.. ?
#         ____
#             ?.a.. ?
#
#     ___ pop
#         _____ l.. ? ___ l.. ? -1 __ 0
#             ?.p..
#         __ l.. ? __ 0
#             r_ N..
#         ____
#             r_ ? -1 .p..
#
#     ___ pop_at stackNumber
#         __ l.. ? ? > 0
#             r_ ? ? .p..
#         ____
#             r_ N..
#
#
# customStack_ PlateStack(2)
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# customStack.push(4)
# print(customStack.pop_at(1))
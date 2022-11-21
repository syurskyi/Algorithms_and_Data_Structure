# #   Created by Elshad Karimov on 02/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Use a single list to implement three stacks.
#
# c_ MultiStack:
#     ___ -  stacksize
#         numberstacks _ 3
#         custList _ [0] * ? * ?
#         sizes _ [0] * ?
#         ? _ ?
#
#     ___ isFull stacknum
#         __ ? ? __ ?
#             r_ T..
#         ____
#             r_ F..
#
#     ___ isEmpty stacknum
#         __ ? ? __ 0
#             r_ T..
#         ____
#             r_ F..
#
#     ___ indexOfTop stacknum
#         offset _ ? * ?
#         r_ ? + ? ?- 1
#
#     ___ push item, stacknum
#         __ ? ?
#             r_ "The stack is full"
#         ____
#             ? ? +_ 1
#             c.. i.. ? _ ?
#
#     ___ pop stacknum
#         __ ? ?
#             r_ "The stack is empty"
#         ____
#             value _ c.. i.. ?
#             c.. i.. ? _ 0
#             ? ? -_ 1
#             r_ ?
#
#     ___ peek stacknum
#         __ ? ?
#             r_ "The stack is empty"
#         ____
#             value _ c.. i.. ?
#             r_ ?
#
#
# customStack _ MultiStack(6)
# print(customStack.isFull(0))
# print(customStack.isEmpty(1))
# customStack.push(1, 0)
# customStack.push(2, 0)
# customStack.push(3, 2)
# print(customStack.p.. 0))
#

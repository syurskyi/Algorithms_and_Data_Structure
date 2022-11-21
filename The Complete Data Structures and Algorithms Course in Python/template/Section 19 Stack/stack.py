# #   Created by Elshad Karimov on 19/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ MultiStack
#
#     ___ -  stacksize
#         numstacks _ 3
#         array _ 0 * (? * ?
#         sizes _ 0 * ?
#         ? _ ?
#         # print(self.array)
#         # print(self.sizes)
#
#     ___ Push item, stacknum
#         __ I.. ?
#             r... E..('Stack is full')
#         ? ? +_ 1
#         a.. I.. ? _ ?
#
#     ___ Pop stacknum
#         __ I.. ?
#             r... E..('Stack is empty')
#         value _ a.. I.. ?
#         a.. I.. ? _ 0
#         ? ? -_ 1
#         r_ ?
#
#     ___ Peek stacknum
#         __ I.. ?
#             r... E..('Stack is empty')
#         r_ a.. I.. ?
#
#     ___ IsEmpty stacknum
#         r_ ? ? __ 0
#
#     ___ IsFull stacknum
#         r_ ? ? __ ?
#
#     ___ IndexOfTop stacknum
#         offset _ ? * ?
#         r_ ? + ? ? - 1
#
# stack _ MultiStack(1)
#

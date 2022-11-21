# #   Created by Elshad Karimov on 04/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# #   Create Stack with min method
#
# c_ Node
#     ___ -  value_N.., n.. _ N..
#         ? _ ?
#         ? _ ?
#
#     ___ -s
#         string _ s.. ?
#         __ n..
#             ? +_ ',' + s.. ?
#         r_ ?
#
# c_ Stack
#     ___ -
#         top _ N..
#         minNode _ N..
#
#     ___ min
#         __ n.. ?
#             r_ N..
#         r_ ?.v..
#
#     ___ push item
#         __ m.. ___ (?.v.. < ?
#             m.. _ ? v.. _ ?.v.. next_self.m..
#         ____
#             m.. _ ? v.. _ ? next_self.m..
#         top _ ? value_item, next_self.t..
#
#     ___ pop
#         __ n.. top
#             r_ N..
#         minNode _ ?.n..
#         item _ ?.v..
#         top _ ?.n..
#         r_ ?
#
# customStack _ Stack()
# customStack.push(5)
# print(customStack.min())
# customStack.push(6)
# print(customStack.min())
# customStack.push(3)
# print(customStack.min())
# customStack.p..
# print(customStack.min())
#

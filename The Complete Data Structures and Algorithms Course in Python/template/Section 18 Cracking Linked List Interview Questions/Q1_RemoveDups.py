# #   Created by Elshad Karimov on 17/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list.
#
#
# ____ L.. ______ L..
#
# ___ removeDups ll
#     __ ?.h.. __ N..
#         r_
#     ____
#         currentNode _ ?.h..
#         visited _ s.. ?.v..
#         _____ ?.n..
#             __ ?.n...v. __ ?
#                 ?.n.. _ ?.n...n..
#             ____
#                 ?.a..?.n...v..
#                 c.. _ ?.n..
#         r_ ?
#
# ___ removeDups1 ll
#     __ ?.h.. __ N..
#         r_
#
#     currentNode _ ?.h..
#     _____ ?
#         runner _ ?
#         _____ ?.n..
#             __ ?.n...v.. __ ?.v..
#                 ?.n.. _ ?.n...n..
#             ____
#                 r.. _ ?.n..
#         c.. _ ?.n..
#     r_ ?.h..
#
#
#
# customLL _ LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# removeDups1(customLL)
# print(customLL)
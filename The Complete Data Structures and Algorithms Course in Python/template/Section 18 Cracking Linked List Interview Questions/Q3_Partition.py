# #   Created by Elshad Karimov on 18/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# #  Question 3 - Write code to partition a linked list around a value x,
# #               such that all nodes less than x come before all nodes greater than or equal to x.
#
# ____ L.. ______ L..
#
# ___ partition ll x
#     curNode _ ?.h..
#     ?.t.. _ ?.h..
#
#     _____ ?
#         nextNode _ ?.n..
#         ?.n.. _ N..
#         __ ?.v.. < ?
#             ?.n.. _ ?.h..
#             ?.h.. _ c..
#         ____
#             ?.t__.n.. _ ?
#             ?.t.. _ ?
#         c.. _ n..
#
#     __ ?.t__.n.. __ n.. N..
#         ?.t__.n.. _ N..
#
# customLL _ LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# partition(customLL, 30)
# print(customLL)
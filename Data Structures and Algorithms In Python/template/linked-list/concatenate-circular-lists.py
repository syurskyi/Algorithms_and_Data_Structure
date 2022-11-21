# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node o..
#
#     ___ - value
#         info _ ?
#         link _ N..
#
#
# c_ CircularLinkedList o..
#
#     ___ -
#         last _ N..
#
#     ___ display_list
#         __ ? __ N..
#             print("List is empty\n")
#             r_
#
#         p _ ?.l..
#
#         _____ T..
#             print(?.i.. " ",end_'')
#             p _ ?.l..
#             __  p __ ?.l..
#                 b..
#         print()
#
#     ___ insert_in_empty_list data
#         temp _ ? ?
#         ? _ ?
#         ?.l.. _ ?
#
#
#     ___ insert_at_end data
#         temp _ ? ?
#         ?.l.. _ ?.l..
#         ?.l.. _ ?
#         ? _ ?
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ n __ 0:
#             r_
#         data _ i..(i..("Enter the element to be inserted : "))
#         ? ?
#
#         # for(i = 2  i <= n  i++)
#         ___ i __ r.. ?-1
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ concatenatelist2
#         __ ? __ N..
#             last _ list.l//
#             r_
#
#         __ ?.l.. __ N..
#             r_
#
#         p _ ?.l..
#         ?.l.. _ ?.?.l..
#         ?.?.l.. _ p
#         last _ ?.l..
#
#
# ###############################################################
# list1 _ CircularLinkedList()
# list2 _ CircularLinkedList()
#
# print("Enter first list :- ")
# list1.create_list()
#
# print("Enter second list :- ")
# list2.create_list()
#
# print("First ");   list1.display_list()
# print("Second ");  list2.display_list()
#
# list1.concatenate(list2)
# print("First ")
# list1.display_list()
#
#
#

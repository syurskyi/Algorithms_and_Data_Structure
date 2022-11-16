# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node:
#
#     ___ - value
#         info _ ?
#         link _ N..
#
# c_ SingleLinkedList:
#
#     ___ -
#         start _ N..
#
#     ___ display_list
#         __ ? __ N..
#             print("List is empty")
#             r_
#         ____
#             print("List is :   ")
#             p _ ?
#             _____ ? __ n.. N..
#                 print(?.i.. " ", end_''
#                 p _ ?.l..
#             print()
#
#     ___ insert_at_end data
#         temp _ ? ?
#         __ start __ N..
#             ? _ ?
#             r_
#
#         p _ start
#         _____ ?.l..__ n.. N..
#             p _ ?.l..
#         ?.l.._ ?
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ ? __ 0
#             r_
#         ___ i __ r.. ?
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ concatenate list2
#         __ start __ N..
#             start _ ?.s..
#             r_
#
#         __ ?.s.. __ N..
#             r_
#
#         p _ start
#         _____ ?.l..__ n.. N..
#             p _ ?.l..
#
#         ?.l.._ ?.s..
#
# #########################################################################################
#
# list1 _ SingleLinkedList()
# list2 _ SingleLinkedList()
#
# print("Enter first list :- ")
# list1.create_list()
# print("Enter second list :- ")
# list2.create_list()
#
# print("First "); list1.display_list()
# print("Second "); list2.display_list()
#
# list1.concatenate(list2)
# print("First "); list1.display_list()
#

# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node o..
#
#     ___ - value
#         info _ ?
#         link _ N..
#
# c_ SortedLinkedList o..
#
#     ___ -
#         start _ N..
#
#     ___ insert_in_order data
#             temp _ ?
#
#             # List empty or node to be inserted before first node
#             __ ? __ N.. __ ? < ?.i..
#                 ?.l.. _ s..
#                 s.. _ ?
#                 r_
#
#             p _ s..
#             _____ ?.l.. __ n.. N.. ___ ?.l...i.. <_ ?
#                 p _ ?.l..
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ n __ 0
#             r_
#
# 	___ i __ r.. ?
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ search x
#         __ s.. __ N..
#             print("List is empty")
#             r_
#         p _ s..
#         position _ 1
#         _____  p __ n.. N.. ___ ?.i.. <_ ?
#             __  ?.i.. __ ?
#                 b..
#             ?+_1
#             p _ ?.l..
#
#         __ ? __ N.. __ ?.i.. !_ ?
#             print ?" not found in list"
#         ____
#             print ? " is at position " ?
#
#     ___ display_list
#         __ s.. __ N..
#             print("List is empty")
#             r_
#         print("List is :   ")
#         p _ s..
#         _____ ? __ n.. N..
#             print(?.i.. "  ", end_''
#             p _ ?.l..
#         print()
#
# #########################################################################
#
# list _ SortedLinkedList()
# list.create_list()
#
# _____ T..:
#     print("1.Display list")
#     print("2.Insert")
#     print("3.Search for an element")
#     print("4.Quit")
#
#     option _ i..(i..("Enter your choice : " ))
#
#     __ option __ 1:
#         list.display_list()
#     ____ option __ 2:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_in_order(data)
#     ____ option __ 3:
#         data _ i..(i..("Enter the element to be searched : "))
#         list.search(data)
#     ____ option __ 4:
#         b..
#     ____
#         print("Wrong option")
#     print()
#
#
#
#

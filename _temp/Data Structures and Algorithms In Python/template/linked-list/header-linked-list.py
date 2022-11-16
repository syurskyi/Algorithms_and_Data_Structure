# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node o..
#
#     ___ - value
#         info _ value
#         link _ N..
#
# c_ HeaderLinkedList o..
#
#     ___ -
#         head _ ? 0
#
#     ___ display_list
#         __ ?.l.. __ N..
#             print("List is empty")
#             r_
#
#         p _ ?.l..
#         print("List is : ")
#         _____ ? __ n.. N..
#             print(?.i.. " ", end_'')
#             p _ ?.l..
#         print()
#
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         ___ i __ r.. ?
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#
#     ___ insert_at_enddata
#
#         temp _ ? ?
#
#         p _ head
#         _____ ?.l.. __ n.. N..:
#             p _ ?.l..
#
#         ?.l.. _ ?
#         ?.l.. _ N..
#
#     ___ insert_before data, x
#         # Find pointer to predecessor of node containing x
#         p _ h..
#         _____  ?.l.. __ n.. N..
#             __ ?.l...i.. __ ?
#                 b..
#             p _ ?.l..
#
#         __ ?.l.. __ N..
#             print ? " not present in the list")
#         ____
#             temp _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#     ___ insert_at_position data k
#         p _ h..
#         i _ 1
#         _____ i <_ ?-1 ___ p __ n.. N..
#             p _ ?.l..
#             ?+_1
#
#         __ p __ N..
#             print("You can insert only upto " , (i-1) , "th position ")
#         ____
#             temp _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#     ___ delete_node data
#         p _ h..
#         _____ ?.l.. __ n.. N..
#             __ ?.l...i.. __ ?
#                 b..
#             p _ ?.l..
#
#         __ ?.l.. __ N..
#             print(? + "Element _d not found")
#         ____
#             ?.l.. _ ?.l...l..
#
#     ___ reverse_list
#         prev _ N..
#         p _ ?.l..
#         _____ ? __ n.. N..
#             next _ ?.l..
#             ?.l.. _ p..
#             p.. _ p
#             p _ n..
#
#         ?.l.. _ p..
#
# list _ HeaderLinkedList()
#
# list.create_list()
#
# _____ T..:
#     print("1.Display list")
#     print("2.Insert a node at the end of the list")
#     print("3.Insert a node before a specified node")
#     print("4.Insert a node at a given position")
#     print("5.Delete a node")
#     print("6.Reverse the list")
#     print("7.Quit")
#
#     option _ i..(i..("Enter your choice : " ))
#
#     __ option __ 1:
#         list.display_list()
#     ____ option __ 2:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_at_end(data)
#     ____ option __ 3:
#         data _ i..(i..("Enter the element to be inserted : "))
#         x _ i..(i..("Enter the element before which to insert : "))
#         list.insert_before(data,x)
#     ____ option __ 4:
#         data _ i..(i..("Enter the element to be inserted : "))
#         k _ i..(i..("Enter the position at which to insert : "))
#         list.insert_at_position(data,k)
#     ____ option __ 5:
#         data _ i..(i..("Enter the element to be deleted : "))
#         list.delete_node(data)
#     ____ option __ 6:
#         list.reverse_list()
#     ____ option __ 7:
#         b..
#     ____
#         print("Wrong option")
#     print()

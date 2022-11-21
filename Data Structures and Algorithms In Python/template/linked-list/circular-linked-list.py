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
#             print ?.i.. , " ",e.._''
#             p _ ?.l..
#             __  p __ ?.l..
#                 b..
#         print()
#
#     ___ insert_in_beginning data
#         temp _ ? ?
#         ?.l.. _ ?.l..
#         ?.l.. _ ?
#
#     ___ insert_in_empty_list data
#         temp _ ? ?
#         l.. _ ?
#         ?.l.. _ ?
#
#     ___ insert_at_end data
#         temp _ ? ?
#         ?.l.. _ ?.l..
#         ?.l.. _ ?
#         ? _ ?
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ n __ 0
#             r_
#         data _ i..(i..("Enter the element to be inserted : "))
#         ? ?
#
#         ___ i __ r.. ?-1
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ insert_after data,x
#         p _ ?.l..
#
#         _____ T..
#             __ ?.i.. __ ?
#                 b..
#             p _ ?.l..
#             __ ? __ ?.l..
#                 b..
#
#         __ p __ ?.l.. ___ ?.i.. !_ ?
#             print ? " not present in the list")
#         ____
#             temp _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#             __ p __ ?
#                 ? _ ?
#
#     ___ delete_first_node
#         __ ? __ N.. # List is empty
#             r_
#         __ ?.l.. __ ? # List has only one node
#             ? _ N..
#             r_
#         ?.l.. _ ?.l__.l..
#
#
#     ___ delete_last_node
#         __ ? __ N.. # List is empty
#             r_
#         __ ?.l.. __ ? # List has only one node
#             ? _ N..
#             r_
#
#         p _ ?.l..
#         _____ ?.l.. !_ ?
#             p _ ?.l..
#         ?.l.. _ ?.l..
#         l.. _ ?
#
#     ___ delete_node x
#
#         __ ? __ N.. # List is empty
#                 r_
#         __ ?.l.. __ ? ___ ?.i.. __ ?  # Deletion of only node
#             last _ N..
#             r_
#
#         __ ?.l...i.. __ ?  # Deletion of first node
#             ?.l.. _ ?.l...l..
#             r_
#
#         p _ ?.l..
#         _____ ?.l.. !_ ?.l..
#             __  ?.l...i.. __ ?
#                 b..
#             p _ ?.l..
#
#         __ ?.l.. __ ?.l..
#             print ?  " not found in the list")
#         ____
#             ?.l.. _ ?.l...l..
#             __ ?.i.. __ ?
#                 ? _ p
#
#
# ##############################################################
#
# list _ CircularLinkedList()
# list.create_list()
#
# _____ T..
#     print("1.Display list")
#     print("2.Insert in empty list")
#     print("3.Insert a node in the beginning of the list")
#     print("4.Insert a node at the end of the list")
#     print("5.Insert a node after a specified node")
#     print("6.Delete first node")
#     print("7.Delete last node")
#     print("8.Delete any node")
#     print("9.Quit")
#
#     option _ i..(i..("Enter your choice : " ))
#
#     __ option __ 1:
#         list.display_list()
#     ____ option __ 2:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_in_empty_list(data)
#     ____ option __ 3:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_in_beginning(data)
#     ____ option __ 4:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_at_end(data)
#     ____ option __ 5:
#         data _ i..(i..("Enter the element to be inserted : "))
#         x _ i..(i..("Enter the element after which to insert : "))
#         list.insert_after(data,x)
#     ____ option __ 6:
#         list.delete_first_node()
#     ____ option __ 7:
#         list.delete_last_node()
#     ____ option __ 8:
#         data _ i..(i..("Enter the element to be deleted : "))
#         list.delete_node(data)
#     ____ option __ 9:
#         b..
#     ____
#         print("Wrong option")
#     print()
#
#
#

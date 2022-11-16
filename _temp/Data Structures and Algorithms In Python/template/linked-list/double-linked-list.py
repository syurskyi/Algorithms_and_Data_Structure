# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node o..
#
#     ___ - value
#         info _ ?
#         prev _ N..
#         next _ N..
#
#
# c_ DoubleLinkedList o..
#
#     ___ -
#         start _ N..
#
#     ___ display_list
#         __ ? __ N..
#             print("List is empty")
#             r_
#
#         print("List is : ")
#         p _ s..
#         _____ p __ n.. N..:
#             print(?.i.. "  ", end_'')
#             p _ ?.n..
#         print()
#
#
#     ___ insert_in_beginningdata
#         temp _ ? ?
#         ?.n.. _ start
#         ?.p.. _ ?
#         ? _ ?
#
#     ___ insert_in_empty_listdata
#         temp _ ? ?
#         ? _ ?
#
#     ___ insert_at_enddata
#         temp _ ? ?
#         p _ s..
#         _____ ?.n.. __ n.. N..
#             p _ ?.n..
#         ?.n.. _ ?
#         ?.p.. _ p
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ ? __ 0
#             r_
#         data _ i..(i..("Enter the first element to be inserted : "))
#         ? ?
#
#         ___ i __ r.. ?-1
#             data _ i..(i..("Enter the next element to be inserted : "))
#             ? ?
#
#
#     ___ insert_afterdata, x
#         temp _ ? ?
#         p _ s..
#         _____ ? __ n.. N..
#             __  ?.i.. __ ?
#                 b..
#             p _ ?.n..
#
#         __ p __ N..
#             print ?" not present in the list")
#         ____
#             ?.p.. _ p
#             ?.n.. _ ?.n..
#             __ ?.n.. __ n.. N..
#                 ?.n...p.. _ ? # should not be done when p refers to last node
#             ?.n.. _ ?
#
#     ___ insert_before data x
#         __ start __ N..
#             print("List is empty")
#             r_
#
#         __ ?.i.. __ x
#             temp _ ? ?
#             ?.n.. _ ?
#             ?.p.. _ ?
#             ? _ ?
#             r_
#
#         p _ s..
#         _____ p __ n.. N..
#             __ ?.i.. __ ?
#                 b..
#             p _ ?.n..
#
#         __ p __ N..
#             print ? " not present in the list")
#         ____
#             temp _ ? ?
#             ?.p.. _ ?.p..
#             ?.n.. _ p
#             ?.p...n.. _ ?
#             ?.p.. _ ?
#
#     ___ delete_first_node
#         __ s.. __ N..  # list is empty
#             r_
#         __ ?.n.. __ N.. # list has only one node
#             s.. _ N..
#             r_
#         s.. _ ?.n..
#         ?.p.. _ N..
#
#     ___ delete_last_node
#         __ s.. __ N..   # list is empty
#             r_
#         __ ?.n.. __ N..  # list has only one node
#             s.. _ N..
#             r_
#
#         p _ s..
#         _____ ?.n.. !_ N..
#             p _ ?.n..;
#         ?.p...n.. _ N..
#
#
#     ___ delete_node x
#         __ s.. __ N..:  # list is empty
#             r_
#         __ ?.n.. __ N..	# list has only one node
#             __ ?.i.. __ x
#                 s.. _ N..
#             ____
#                 print ? " not found")
#             r_
#
#         # Deletion of first node
#         __ ?.i.. __ x
#             s.. _ ?.n..
#             ?.p.. _ N..
#             r_
#
#         p _ ?.n..
#         _____ ?.n.. __ n.. N..
#             __ ?.i.. __ x:
#                 b..
#             p _ ?.n..
#
#
#         __ ?.n.. __ n.. N..  # node to be deleted is in between
#             ?.p...n.. _ ?.n..
#             ?.n...p.. _ ?.p..
#         ____ # p refers to last node
#             __ ?.i.. __ ? # node to be deleted is last node
#                 ?.p...n.. _ N..
#             ____
#                 print ?" not found")
#
#     ___ reverse_list
#         __ s.. __ N..
#             r_
#
#         p1 _ s..
#         p2 _ ?.n..
#         ?.n.. _ N..
#         ?.p.. _ ?
#         _____ ? __ n.. N..
#             ?.p.. _ ?.n..
#             ?.n.. _ ?
#             ? _ ?
#             ? _ ?.p..
#         s.. _ ?
#
# #########################################################################
#
# list _ DoubleLinkedList()
# list.create_list()
#
# _____ T..:
#     print("1.Display list")
#     print("2.Insert in empty list")
#     print("3.Insert a node in the beginning of the list")
#     print("4.Insert a node at the end of the list")
#     print("5.Insert a node after a specified node")
#     print("6.Insert a node before a specified node")
#     print("7.Delete first node")
#     print("8.Delete last node")
#     print("9.Delete any node")
#     print("10.Reverse the list")
#     print("11.Quit")
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
#         data _ i..(i..("Enter the element to be inserted : "))
#         x _ i..(i..("Enter the element before which to insert : "))
#         list.insert_before(data,x)
#     ____ option __ 7:
#         list.delete_first_node()
#     ____ option __ 8:
#         list.delete_last_node()
#     ____ option __ 9:
#         data _ i..(i..("Enter the element to be deleted : "))
#         list.delete_node(data)
#     ____ option __ 10:
#         list.reverse_list()
#     ____ option __ 11:
#         b..
#     ____
#         print("Wrong option")
#     print()
#
#
#

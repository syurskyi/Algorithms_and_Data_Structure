# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node:
#
#     ___ - value
#         info _ ?
#         link _ N..
#
# c_ SingleLinkedList
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
#             p _ s..
#             _____ p __ n.. N..
#                 print(?.i.. " ", end_'')
#                 p _ ?.l..
#             print()
#
#     ___ count_nodes
#         p _ s..
#         n _ 0
#         _____ p __ n.. N..
#             ?+_1
#             p _ ?.l..
#         print("Number of nodes in the list = " ?
#
#     ___ searchx
#         position _ 1
#         p _ s..
#         _____ ? __ n.. N..
#             __ ?.i.. __ ?
#                 print ? " is at position " ?
#                 r_ T..
#             ?+_1
#             p _ ?.l..
#         ____
#             print ? " not found in list")
#             r_ F..
#
#     ___ insert_in_beginning data
#         temp _ ? ?
#         ?.l.. _ s..
#         s.. _ ?
#
#     ___ insert_at_end data
#         temp _ ? ?
#         __ s.. __ N..
#             s.. _ ?
#             r_
#
#         p _ s..
#         _____ ?.l.. __ n.. N..
#             p _ ?.l..
#         ?.l.. _ ?
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ n __ 0
#             r_
#         ___ i __ r.. ?
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ insert_after data x
#         p..
#
#     ___ insert_before data, x
#         p..
#
#     ___ insert_at_position data, k
#         p..
#
#     ___ delete_node x
#         p..
#
#     ___ delete_first_node
#         p..
#
#     ___ delete_last_node
#         p..
#
#     ___ reverse_list
#         p..
#
#     ___ bubble_sort_exdata
#         p..
#
#     ___ bubble_sort_exlinks
#         p..
#
#     ___ has_cycle
#         p..
#
#     ___ find_cycle
#         p..
#
#     ___ remove_cycle
#         p..
#
#     ___ insert_cyclex
#         p..
#
#     ___ merge2list2
#         p..
#
#     ___ _merge2 p1, p2
#         p..
#
#     ___ merge_sort
#         p..
#
#     ___ _merge_sort_reclistStart
#         p..
#
#     ___ _divide_list p
#         p..
#
#
# #######################################################################################
#
# list _ SingleLinkedList()
#
# list.create_list()
#
# _____ T..:
#     print("1.Display list")
#     print("2.Count the number of nodes")
#     print("3.Search for an element")
#     print("4.Insert in empty list/Insert in beginning of the list")
#     print("5.Insert a node at the end of the list")
#     print("6.Insert a node after a specified node")
#     print("7.Insert a node before a specified node")
#     print("8.Insert a node at a given position")
#     print("9.Delete first node")
#     print("10.Delete last node")
#     print("11.Delete any node")
#     print("12.Reverse the list")
#     print("13.Bubble sort by exchanging data")
#     print("14.Bubble sort by exchanging links")
#     print("15.MergeSort")
#     print("16.Insert Cycle")
#     print("17.Detect Cycle")
#     print("18.Remove cycle")
#     print("19.Quit")
#
#     option _ i..(i..("Enter your choice : " ))
#
#     __ option __ 1:
#         list.display_list()
#     ____ option __ 2:
#         list.count_nodes()
#     ____ option __ 3:
#         data _ i..(i..("Enter the element to be searched : "))
#         list.search(data)
#     ____ option __ 4:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_in_beginning(data)
#     ____ option __ 5:
#         data _ i..(i..("Enter the element to be inserted : "))
#         list.insert_at_end(data)
#     ____ option __ 6:
#         data _ i..(i..("Enter the element to be inserted : "))
#         x _ i..(i..("Enter the element after which to insert : "))
#         list.insert_after(data,x)
#     ____ option __ 7:
#         data _ i..(i..("Enter the element to be inserted : "))
#         x _ i..(i..("Enter the element before which to insert : "))
#         list.insert_before(data,x)
#     ____ option __ 8:
#         data _ i..(i..("Enter the element to be inserted : "))
#         k _ i..(i..("Enter the position at which to insert : "))
#         list.insert_at_position(data,k)
#     ____ option __ 9:
#         list.delete_first_node()
#     ____ option __ 10:
#         list.delete_last_node()
#     ____ option __ 11:
#         data _ i..(i..("Enter the element to be deleted : "))
#         list.delete_node(data)
#     ____ option __ 12:
#         list.reverse_list()
#     ____ option __ 13:
#         list.bubble_sort_exdata()
#     ____ option __ 14:
#         list.bubble_sort_exlinks()
#     ____ option __ 15:
#         list.merge_sort()
#     ____ option __ 16:
#         data _ i..(i..("Enter the element at which the cycle has to be inserted : "))
#         list.insert_cycle(data)
#     ____ option __ 17:
#         __ list.has_cycle(
#             print("List has a cycle")
#         ____
#             print("List does not have a cycle")
#     ____ option __ 18:
#         list.remove_cycle()
#     ____ option __ 19:
#         b..
#     ____
#         print("Wrong option")
#     print()
#
#

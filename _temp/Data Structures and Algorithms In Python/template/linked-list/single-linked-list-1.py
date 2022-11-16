# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ Node:
#
#     ___ - value
#         info _ ?
#         link _ N..
#
#
# c_ SingleLinkedList
#
#     ___ -
#         start _ N..
#
#
#     ___ display_list
#         __ ? __ N..
#             print("List is empty")
#             r_
#         ____
#             print("List is :   ")
#             p _ s..
#             _____ ? __ n.. N..
#                 print ?.i.. " ", end_'')
#                 p _ ?.l..
#             print()
#
#
#     ___ count_nodes
#         p _ s..
#         n _ 0
#         _____ ? __ n.. N..
#             ?+_1
#             p _ ?.l..
#         print("Number of nodes in the list = " ?
#
#     ___ search x
#         position _ 1
#         p _ s..
#         _____ p __ n.. N..
#             __ ?.i.. __ ?
#                 print ? " is at position " ?
#                 r_ T..
#             ?+_1
#             p _ ?.l..
#         ____
#             print ?" not found in list")
#             r_ F..
#
#     ___ insert_in_beginning data
#         t.. _ ? ?
#         ?.l.. _ s..
#         s.. _ ?
#
#
#     ___ insert_at_end data
#         t.. _ ? ?
#         __ s.. __ N..
#             s.. _ t..
#             r_
#
#         p _ s..
#         _____ ?.l.. __ n.. N..
#             p _ ?.l..
#         ?.l.. _ t..
#
#
#     ___ create_list
#         n _ i..(i..("Enter the number of nodes : "))
#         __ n __ 0:
#             r_
#         ___ i __ r.. ?
#             data _ i..(i..("Enter the element to be inserted : "))
#             ? ?
#
#     ___ insert_after data x
#         p _ s..
#         _____ p __ n.. N..
#             __ ?.i.. __ ?
#                 b..
#             p _ ?.l..
#
#         __ p __ N..
#             print(x, "not present in the list")
#         ____
#             t.. _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#
#
#     ___ insert_before data, x
#         # If list is empty
#         __ s.. __ N..
#             print("List is empty")
#             r_
#
#         # x is in first node,new node is to be inserted before first node
#         __ x __ s__.i..
#             t.. _ ? ?
#             ?.l.. _ s..
#             s.. _ ?
#             r_
#
#         # Find reference to predecessor of node containing x
#         p _ s..
#         _____ ?.l.. __ n.. N..
#             __ ?.l...i.. __ ?
#                 b..
#             p _ ?.l..
#
#
#         __ ?.l.. __ N..
#              print ? " not present in the list")
#         ____
#             t.. _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#
#
#     ___ insert_at_position data, k
#         __ ? __ 1
#             t.. _ ? ?
#             ?.l.. _ s..
#             s.. _ ?
#             r_
#
#         p _ s..
#         i _ 1
#         _____ i<?-1 ___ p __ n.. N.. # find a reference to k-1 node
#             p _ ?.l..
#             ?+_1
#
#         __ p __ N..
#             print("You can insert only upto position",i)
#         ____
#             t.. _ ? ?
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#     ___ delete_node x
#
#             __ s.. __ N..
#                 print("List is empty")
#                 r_
#
#             # Deletion of first node
#             __ s__.i.. __ ?
#                 s.. _ s...l..
#                 r_
#
#             # Deletion in between or at the end
#             p _ s..
#             _____ ?.l.. __ n.. N..
#                 __ ?.l...i.. __ ?
#                     b..
#                 p _ ?.l..
#
#             __ ?.l.. __ N..
#                 print("Element ", x ,"not in list")
#             ____
#                 ?.l.. _ ?.l...l..
#
#
#     ___ delete_first_node
#
#         __ s.. __ N..
#             r_
#         s.. _ s...l..
#
#
#     ___ delete_last_node
#
#         __ s.. __ N..
#             r_
#
#         __ s...l.. __ N..
#             s.. _ N..
#             r_
#
#         p _ s..
#         _____ ?.l...l.. __ n.. N..
#             p _ ?.l..
#         ?.l.. _ N..
#
#     ___ reverse_list
#
#         prev _ N..
#         p _ s..
#         _____ ? __ n.. N..
#             next _ ?.l..
#             ?.l.. _ p..
#             p.. _ ?
#             p _ n..
#
#         s.. _ p..
#
#
#
#     ___ bubble_sort_exdata
#         end_N..
#
#         _____ ? !_ s...l..
#
#             p _ s..
#             _____  ?.l.. !_ ?
#                 q _ ?.l..
#                 __ ?.i.. > ?.i..
#                     ?.i..,?.i.. _ ?.i..,?.i..
#                 p _ ?.l..
#             end _ ?
#
#
#     ___ bubble_sort_exlinks
#         end _ N..
#         _____ ? !_ s...l..
#             r _ p _ s..
#             _____ ?.l.. !_ ?
#                 q _ ?.l..
#                 __ ?.i.. > ?.i..
#                     ?.l.. _ ?.l..
#                     ?.l.. _ p
#                     __ p!_self.s..
#                         ?.l.. _ ?
#                     ____
#                         s.. _ ?
#                     ? ? _ ? ?
#                 ? _ ?
#                 p _ ?.l..
#             end _ ?
#
#
#     ___ has_cycle
#
#         __ ? __ N..
#             r_ F..
#         ____
#             r_ T..
#
#
#     ___ find_cycle
#
#         __ s.. __ N.. __ s...l.. __ N..
#             r_ N..
#
#         slowR _ s..
#         fastR _ s..
#
#         _____ f..__ n.. N.. ___ f__.l.. __ n.. N..
#             slowR _ ?.l..
#             fastR _ ?.l...l..
#             __ s.. __ f..
#                 r_ s..
#         r_ N..
#
#
#     ___ remove_cycle
#
#         c _ ?
#         __ ? __ N..
#             r_
#         print("Node at which the cycle was detected is " , ?.i..)
#
#         p _ c
#         q _ c
#         lenCycle _ 0
#
#         _____ T..
#             ?+_1
#             q _ ?.l..
#             __ ? __ ?
#                 b..
#
#         print("Length of cycle is :" ?
#
#         lenRemList _ 0
#         p _ s..
#         _____ ? !_ ?
#             l.. +_1
#             p _ ?.l..
#             q _ ?.l..
#
#         print("Number of nodes not included in the cycle are : " ?
#
#         length_list _ ? + ?
#         print("Length of the list is : " ?
#
#         p _ s..
#         ___ i __ r.. ?-1
#                 p _ ?.l..
#         ?.l.. _ N..
#
#
#     ___ insert_cyclex
#         __ s.. __ N..
#             r_
#         p _ s..
#         px _ N..
#         prev _ N..
#
#         _____ p __ n.. N..
#             __ ?.i.. __ ?
#                 px _ p
#             p.. _ p
#             p _ ?.l..
#
#         __ px __ n.. N..
#             p__.l.. _ px
#         ____
#             print ? " not present in list")
#
#
#     ___ merge2list2
#         merge_list _ S..
#         ?.s.. _ ? s.. ?.s..
#         r_ ?
#
#     ___ _merge2 p1, p2
#
#         __ ?.i.. <_ ?.i..
#             startM _ p1
#             p1 _ ?.l..
#         ____
#             startM _ p2
#             p2 _ p2.l..
#
#         pM _ startM
#
#         _____ p1 __ n.. N.. ___ p2 __ n.. N..
#             __ p1.i.. <_ p2.i.. :
#                 pM.l.. _ p1
#                 pM _ pM.l..
#                 p1 _ p1.l..
#             ____
#                 pM.l.. _ p2
#                 pM _ pM.l..
#                 p2 _ p2.l..
#
#         __ p1 __ N..
#             pM.l.. _ p2
#         ____
#             pM.l.. _ p1
#
#         r_ startM
#
#
#
#     ___ merge_sort
#         s.. _ _merge_sort_rec(s..)
#
#
#     ___ _merge_sort_reclist_start
#
#         #if list empty or has one element
#         __ list_start __ N.. __ list_start.l.. __ N..
#                 r_ list_start
#
#         #if more than one element
#         start1 _ list_start
#         start2 _ _divide_list(list_start)
#         start1 _ _merge_sort_rec(start1)
#         start2 _ _merge_sort_rec(start2)
#         startM _ _merge2(start1, start2)
#         r_ startM
#
#
#     ___ _divide_list p
#         q _ ?.l...l..
#         _____ q __ n.. N.. ___ q.l.. __ n.. N..
#             p _ ?.l..
#             q _ q.l...l..
#         start2 _ ?.l..
#         ?.l.. _ N..
#         r_ start2
#
#
#
# ########################################################################################
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

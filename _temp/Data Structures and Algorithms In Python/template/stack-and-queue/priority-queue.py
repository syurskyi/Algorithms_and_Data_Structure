# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     p..
#
# c_ Node:
#
#     ___ - value pr
#         info _ ?
#         priority _ ?
#         link _ N..
#
# c_ PriorityQueue:
#
#     ___ -
#         front _ N..
#
#     ___ enqueue data, data_priority
#
#         temp _ ? ? ?
#
#         #If queue is empty or element to be added has priority more than first element
#         __ ? __ d.. < ?.p..
#             ?.l.. _ f..
#             ? _ ?
#         ____
#             p _ f..
#             _____ ?.l.. !_ N.. ___ ?.l...p.. <_ d..
#                 p _ ?.l..
#             ?.l.. _ ?.l..
#             ?.l.. _ ?
#
#     ___ dequeue
#         __ ?
#             r... E..("Queue is empty")
#         x _ ?.i..
#         f.. _ ?.l..
#         r_ ?
#
#     ___ is_empty
#         r_ ? __ N..
#
#     ___ display
#         __ ?
#             print("Queue is empty")
#             r_
#
#         print("Queue is : ")
#         p _ f..
#         _____ p __ n.. N..
#             print(?.i.. , "     ", ?.p..
#             p _ ?.l..
#         print()
#
#     ___ size
#         n _ 0
#         p _ f..
#         _____ ? __ n.. N..
#             ?+_1
#             p _ ?.l..
#         r_ ?
#
#
#
# #########################################################################################
#
# __ __name__ __ "__main__":
#     qu _ PriorityQueue()
#
#     _____ T..:
#         print("1.Enqueue")
#         print("2.Dequeue")
#         print("3.Display all queue elements")
#         print("4.Display size of the queue")
#         print("5.Quit")
#
#         choice _ i..(i..("Enter your choice : "))
#
#         __ choice __ 1:
#             x _ i..(i..("Enter the element : "))
#             pr _ i..(i..("Enter its priority : "))
#             qu.enqueue(x,pr)
#         ____ choice __ 2:
#             x_qu.dequeue()
#             print("Element is : " , x)
#         ____ choice __ 3:
#             qu.display()
#         ____ choice __ 4:
#             print("Size of queue " , qu.size())
#         ____ choice __ 5:
#           b..;
#         ____
#           print("Wrong choice")
#         print()

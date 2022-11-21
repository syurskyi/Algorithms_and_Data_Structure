# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     p..
#
# c_ Node
#
#     ___ - value
#         info _ ?
#         link _ N..
#
# c_ Queue
#
#     ___ -
#         rear _ N..
#
#     ___ is_empty
#         r_ ? __ N..
#
#     ___ size
#         __ ?
#             r_ 0
#         n _ 0
#         p _ ?.l..
#         _____ T..
#             ?+_1
#             p _ ?.l..
#             __  ? __ ?.l..
#                 b..
#         r_ n
#
#     ___ enqueue data
#         temp _ ? ?
#
#         __ is_empty
#             r.. _ ?
#             ?.l.. _ ?
#         ____
#             ?.l.. _ r__.l..
#             r__.l.. _ t..
#             r.. _ ?
#
#     ___ dequeue
#         __ ?
#             r... E..("Queue is Empty")
#
#         __ r__.l.. __ r.. #List has only one node
#             ? _ r..
#             ? _ N..
#         ____
#             t.. _ r__.l..
#             r__.l.. _ r__.l...l..
#         r_ ?.i..
#
#     ___ peek
#         __ ?
#             r... E..("Queue is Empty")
#         r_ r__.l...i..
#
#     ___ display
#         __ ?
#             print("List is empty")
#             r_
#
#         p _ r__.l..
#         _____ T..
#             print(?.i.. , " ",end_'')
#             p _ ?.l..
#             __ p __ r__.l..
#                 b..
#         print()
#
# ########################################################################
#
# __ __name__ __ "__main__":
#     qu _ Queue()
#
#     _____ T..:
#         print("1.Enqueue")
#         print("2.Dequeue")
#         print("3.Peek")
#         print("4.Size")
#         print("5.Display")
#         print("6.Quit")
#
#         choice _ i..(i..("Enter your choice : "))
#
#         __ choice __ 1:
#             x_int(i..("Enter the element : "))
#             qu.enqueue(x)
#         ____ choice __ 2:
#             x_qu.dequeue()
#             print("Element deleted from the queue is : " , x)
#         ____ choice __ 3:
#             print("Element at the front end is " , qu.peek())
#         ____ choice __ 4:
#             print("Size of queue ", qu.size())
#         ____ choice __ 5:
#             qu.display()
#         ____ choice __ 6:
#           b..;
#         ____
#           print("Wrong choice")
#         print()
#

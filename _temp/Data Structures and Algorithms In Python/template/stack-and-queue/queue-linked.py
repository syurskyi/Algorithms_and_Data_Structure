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
#         front _ N..
#         rear _ N..
#         size_queue _ 0
#
#     ___ is_empty
#         r_ ? __ N..
#
#     ___ size
#         r_ s..
#
#     ___ enqueue data
#         temp _ ? ?
#         __ ? __ N..
#             f.. _ ?
#         ____
#             r__.l.. _ ?
#         r.. _ ?
#         s.. +_1
#
#     ___ dequeue
#         __ ?
#             r... E..("Queue is empty")
#         x _ ?.i..
#         f.. _ ?.l..
#         ? -_1
#         r_ ?
#
#     ___ peek
#         __ >
#             r... E..("Queue is empty")
#         r_ ?.i..
#
#     ___ display
#         __ ?
#             print("Queue is empty")
#             r_
#         print("Queue is :   ")
#         p _ ?
#         _____ p __ n.. N..
#             print(?.i.., " ", end_'')
#             p _ ?.l..
#         print()
#
#
# #########################################################################################
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

# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     p..
#
# c_ Node:
#     ___ - value
#         info _ ?
#         prev _ N..
#         next _ N..
#
# c_ Deque:
#
#     ___ -
#         front _ N..
#         rear _ N..
#
#     ___ is_empty
#          r_ ? __ N..
#
#     ___ size
#         count _ 0
#         p _ f..
#         _____ p __ n.. N..
#             ?+_1
#             p _ ?.n..
#         r_ ?
#
#     ___ insert_front item
#         temp _ ? ?
#         __ ?
#             f.. _ ? _ ?
#         ____
#             ?.n.. _ f..
#             ?.p.. _ ?
#             f.. _ ?
#
#     ___ insert_rear item
#         temp _ ? ?
#         __ ?
#             ? _ ? _ ?
#         ____
#             ?.n.. _ ?
#             ?.p.. _ ?
#
#         r.. _ ?
#
#     ___ delete_front
#         __ ? ?
#            r... E..("Queue is empty")
#
#         x _ ?.i..
#         __ ?.n.. __ N.. # list has only one node
#             ? _ ? _ N..
#         ____
#             f.. _ ?.n..
#             ?.p.. _ N..
#         r_ ?
#
#     ___ delete_rear
#         __ ?
#            r... E..("Queue is empty")
#
#         x _ ?.i..
#         __ ?.n.. __ N.. # list has only one node
#             ? _ ? _ N..
#         ____
#             r.. _ ?.p..
#             ?.n.. _ N..
#         r_ ?
#
#     ___ first
#         __ ?
#            r... E..("Queue is empty")
#
#         r_ ?.i..
#
#     ___ last
#         __ ?
#            r... E..("Queue is empty")
#
#         r_ r__.i..
#
#     ___ display
#         __ f.. __ N..
#             print("List is empty")
#             r_
#
#         print("List is : ")
#         p _ f..
#         _____ ? __ n.. N..
#             print ?.i.. "  ", end_''
#             p _ ?.n..
#         print()
#
#
# ####################################################################
#
# __ __name__ __ "__main__":
#     qu _ Deque()
#
#     _____ T..:
#         print("1.Insert at the front end")
#         print("2.Insert at the rear end")
#         print("3.Delete from front end")
#         print("4.Delete from rear end")
#         print("5.Display first element")
#         print("6.Display last element")
#         print("7.Display")
#         print("8.Size")
#         print("9.Quit")
#
#         choice _ i..(i..("Enter your choice : "))
#
#         __ choice __ 1:
#             x_int(i..("Enter the element : "))
#             qu.insert_front(x)
#         ____ choice__ 2:
#             x_int(i..("Enter the element : "))
#             qu.insert_rear(x)
#         ____ choice __ 3:
#             x _ qu.delete_front()
#             print("Element deleted from front end is  ", x)
#         ____ choice __ 4:
#             x _ qu.delete_rear()
#             print("Element deleted from rear end is  ", x)
#         ____ choice __ 5:
#             print("First element is  ", qu.first())
#         ____ choice __ 6:
#             print("Last element is  ", qu.last())
#         ____ choice __ 7:
#             qu.display()
#         ____ choice __ 8:
#             print("Size of queue " , qu.size())
#         ____ choice __ 9:
#             b..
#         ____
#             print("Wrong choice")
#         print()

# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     p..
#
# c_ Deque:
#     ___ -
#         items _    # list
#
#     ___ is_empty
#         r_ ? __    # list
#
#     ___ size
#         r_ l.. ?
#
#     ___ insert_front item
#         ?.i.. (0 ?
#
#     ___ insert_rear item
#         ?.a.. ?
#
#     ___ delete_front
#         __ i..
#             r... E..("Queue is Empty")
#         r_ ?.p.. 0
#
#     ___ delete_rear
#         __ i..
#             r... E..("Queue is Empty")
#         r_ ?.p..
#
#     ___ first
#         __ ?
#             r... E..("Queue is Empty")
#         r_ ? 0
#
#     ___ last
#         __ ?
#             r... E..("Queue is Empty")
#         r_ ? -1
#
#     ___ display
#         print ?
#
# ####################################################################
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
#

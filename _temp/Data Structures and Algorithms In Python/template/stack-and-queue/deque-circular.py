# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     p..
#
# c_ Deque
#
#     ___ - default_size_10
#         items _ [N..] * ?
#         front _ 0
#         count _ 0
#
#     ___ is_empty
#         r_ ? __ 0
#
#     ___ size
#         r_ ?
#
#     ___ insert_front item
#         __ ? __ l.. ?
#             r.. 2*l.. ?
#
#         front _ (? - 1) % l.. ?
#         ? ? _ ?
#         ?+_1
#
#     ___ insert_rear item
#         __ ? __ l.. ?
#             r.. 2*l.. ?
#
#         i _ (f.. + c.. % l.. ?
#         ? ? _ ?
#         ? +_1
#
#     ___ delete_front
#         __ ?
#             r... E..("Queue is empty")
#
#         x _ ? ?
#         ? ? _ N..
#         f.. _ (? + 1) % l.. ?
#         ?-_1
#         r_ x
#
#     ___ delete_rear
#         __ ?
#             r... E..("Queue is empty")
#         rear _ (f.. + ? - 1) % l.. ?
#         x _ ? ?
#         ? ? _ N..
#         ?-_1
#         r_ ?
#
#     ___ first
#         __ ?
#             r... E..("Queue is empty")
#         r_ ? ?
#
#     ___ last
#         __ ?
#             r... E..("Queue is empty")
#         rear _ (f.. + ? - 1) % l.. ?
#         r_ ? ?
#
#     ___ display
#         print ?
#
#     ___ resizenewsize
#         old_list _ ?
#         items _ [N..]*?
#         i _ front
#         ___ j __ r.. ?
#             ?_ o.. ?
#             i _ (1+?)%l.. ?
#         f.. _ 0
#
# ####################################################################
#
# __ __name__ __ "__main__":
#     qu _ Deque(6)
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

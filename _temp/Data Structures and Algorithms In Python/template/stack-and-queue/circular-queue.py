# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ E.. E..
#     pass
#
# c_ Queue
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
#     ___ enqueue item
#         __ ? __ l.. ?
#             resize( 2*l.. ?
#
#         i _ (? + ?) % l.. ?
#         ? ? _ ?
#         ?+_1
#
#     ___ dequeue
#         __ i..
#             r... E.. ("Queue is empty")
#
#         x _ ? ?
#         ? ? _ N..
#         f.. _ (f.. + 1) % l.. ?
#         ?-_1
#         r_ ?
#
#     ___ peek
#         __ i..
#             r... E..("Queue is empty")
#         r_ ? ?
#
#     ___ display
#         print ?
#
#     ___ resizenewsize
#         old_list _ i..
#         items _ [N..]* ?
#         i _ f..
#         ___ j __ r.. c..
#             ? ? _ o.. ?
#             i _ (1+i)%l.. ?
#         front _ 0
#
# ###########################################################
#
# __ __name__ __ "__main__":
#     qu _ Queue(6)
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
#           b..
#         ____
#           print("Wrong choice")
#         print()

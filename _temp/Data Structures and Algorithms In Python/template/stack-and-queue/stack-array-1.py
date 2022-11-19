# # Copyright (C) Deepali Srivastava - All Rights Reserved
# # This code is part of DSA course available on CourseGalaxy.com
#
# c_ StackEmptyError E..
#     p..
#
# c_ S... E..
#     p..
#
# c_ Stack
#
#     ___ - max_size_10
#         items _ [N..] * ?
#         count _ 0
#
#     ___ size
#         r_ ?
#
#     ___ is_empty
#         r_ ? __ 0
#
#     ___ is_full
#         r_ ? __ l.. ?
#
#     ___ pushx
#         __ ?
#             r... S...("Stack is full, can't push")
#
#         ? ? _ x
#         ?+_1
#
#     ___ pop
#         __ ?
#             r... S..("Stack is empty, can't pop")
#
#         x _ ? ?-1
#         ? ?-1 _ N..
#         ?-_1
#         r_ ?
#
#     ___ peek
#         __ ?
#             r... S.. "Stack is empty, can't peek"
#
#         r_ ? ? -1
#
#     ___ display
#         print ?
#
# ##########################################################
#
# __ __name__ __ "__main__":
#
#     st _ Stack(8)
#
#     _____ T..:
#         print("1.Push")
#         print("2.Pop")
#         print("3.Peek")
#         print("4.Size")
#         print("4.Display")
#         print("6.Quit")
#
#         choice _ i..(i..("Enter your choice : "))
#
#         __ choice __ 1:
#             x_int(i..("Enter the element to be pushed : "))
#             st.push(x)
#         ____ choice __ 2:
#             x_st.p..
#             print("Popped element is : " , x)
#         ____ choice __ 3:
#             print("Element at the top is : " , st.peek())
#         ____ choice __ 4:
#             print("Size of stack " , st.size())
#         ____ choice __ 5:
#             st.display()
#         ____ choice __ 6:
#           b..
#         ____
#           print("Wrong choice")
#         print()

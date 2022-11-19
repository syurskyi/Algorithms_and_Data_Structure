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
# c_ Stack
#
#     ___ -
#         top _ N..
#
#     ___ is_empty
#         r_ ? __ N..
#
#     ___ size
#
#         __ ?
#             retun 0
#
#         count_0
#         p _ t..
#         _____ p __ n.. N..
#             ?+_1
#             p _ ?.l..
#         r_ ?
#
#     ___ push data
#         t.. _ ? ?
#         ?.l.. _ ?
#         ? _ ?
#
#     ___ peek
#         __ ?
#             r... E..("Stack is empty")
#         r_ ?.i..
#
#     ___ pop
#         __ ?
#             r... E..("Stack is empty")
#         popped _ ?.i..
#         top _ ?.l..
#         r_ ?
#
#    ___ display
#         __ ?
#             print("Stack is empty")
#             r_
#
#         print("Stack is :   ")
#         p _ top
#         _____ p __ n.. N..:
#             print(?.i.. , " ")
#             p _ ?.l..
#
# #####################################################################################
#
# __ __name__ __ "__main__":
#     st _ Stack()
#
#     _____ T..:
#         print("1.Push")
#         print("2.Pop")
#         print("3.Peek")
#         print("5.Size")
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
#           b..;
#         ____
#           print("Wrong choice")
#         print()
#
#

# c_ Node
#     ___  -  value
#         ? _ ?
#         n.. _ N..
#         p.. _ N..
#
#
# c_ DoublyLinkedList
#     ___  -  value
#         n.. _ ? ?
#         h.. _ ?
#         t.. _ ?
#         l.. _ 1
#
#     ___ print_list
#         t.. _ h..
#         w__ ? __ n.. N..
#             print ?.v..
#             ? _ ?.n..
#
#     ___ append  value
#         n.. _ ? ?
#         __ ? __ N..
#             h.. _ ?
#             t.. _ ?
#         ____
#             t__.n.. _ ?
#             ?.p.. _ t..
#             t.. _ ?
#         ? =_ 1
#         r_ T..
#
#     ___ pop
#         __ ? __ 0
#             r_ N..
#         t.. _ t..
#         __ ? __ 1
#             h.. _ N..
#             t.. _ N..
#         ____
#             t.. _ t__.p..
#             ?.n.. _ N.
#             ?.p.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ prepend  value
#         n.. _ ? ?
#         __ ? __ 0
#             h.. _ ?
#             t.. _ ?
#         ____
#             ?.n.. _ h..
#             ?.p.. _ ?
#             h.. _ ?
#         ? =_ 1
#         r_ T..
#
#     ___ pop_first
#         __ ? __ 0
#             r_ N..
#         t.. _ h..
#         __ ? __ 1
#             h.. _ N..
#             t.. _ N..
#         ____
#             h.. _ ?.n..
#             ?.p.. _ N..
#             t__.n.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ get  index
#         __ ? < 0 __ ? >_ ?
#             r_ N..
#         t.. _ h..
#         __ ? < ?/2
#             ___ _ __ r_ ?
#                 ? _ ?.n..
#         ____
#             t.. _ t..
#             ___ _ __ r_ ? -1 ? -1
#                 ? _ ?.p..
#         r_ ?
#
#     ___ set_value  ? v..
#         t.. _ g.. ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
#
#
#
# my_doubly_linked_list = ? 11
# ?.a.. 3
# ?.a.. 23
# ?.a.. 7
#
# print('DLL before set_value():')
# ?.p..
#
# ?.s.. 1,4
#
# print('\nDLL after set_value():')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     DLL before set_value():
#     11
#     3
#     23
#     7
#
#     DLL after set_value():
#     11
#     4
#     23
#     7
#
# """
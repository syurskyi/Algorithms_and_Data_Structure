# c_ Node
#     ___  -  value)
#         ? _
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
#
#
#
# my_doubly_linked_list = ? 2
# ?.append(1)
#
#
# # (2) Items - Returns 2 Node
# print(?.p__.v..
# # (1) Item -  Returns 1 Node
# print(?.p__.v..
# # (0) Items - Returns None
# print(?.p..
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     2
#     1
#     None
#
# """
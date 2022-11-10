# c_ Node
#     ___  - value
#         ? _ ?
#         n.. _ N..
#
#
# c_ LinkedList
#     ___  - value
#         n.. _ ? v..
#         h.. _ ?
#         t.. _ ?
#         l.. _ 1
#
#     ___ print_list
#         t.. _ h..
#         w____ t.. __ n.. N..
#             print ?.v..
#             temp _ ?.n..
#
#     ___ append value
#         n.. _ ? v..
#         __ l.. __ 0
#             h.. _ ?
#             t.. _ ?
#         ____
#             t__.n.. _ ?
#             t.. _ ?
#         l.. +_ 1
#         r_ T..
#
#     ___ pop
#         __ l.. __ 0
#             r_ N..
#         t.. _ h..
#         pre _ h..
#         w____ ?.n..
#             pre _ t..
#             temp _ ?.n..
#         tail _ p..
#         t__.n.. _ N..
#         l.. -_ 1
#         __ l.. __ 0
#             h.. _ N..
#             t.. _ N..
#         r_ ?
#
#
#
#
# my_linked_list _ ? 1
# ?.a.. 2)
#
# # (2) Items - Returns 2 Node
# print(?.p.. .v..
# # (1) Item -  Returns 1 Node
# print(?.p.. .v..
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
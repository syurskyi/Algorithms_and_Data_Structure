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
#         w____ ? __ n.. N..
#             print ?.v..
#             t.. _ ?.n..
#
#     ___ appendvalue
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
#         p.._ h..
#         w____ ?.n..
#             p.. _ t..
#             t.. _ ?.n..
#         t.. _ p..
#         t__.n.. _ N..
#         l.. -_ 1
#         __ l.. __ 0
#             h.. _ N..
#             t.. _ N..
#         r_ ?
#
#     ___ prependvalue
#         n.. _ ? v..
#         __ l.. __ 0
#             h.. _ ?
#             t.. _ ?
#         ____
#             ?.n.. _ h..
#             h.. _ ?
#         l.. +_ 1
#         r_ T..
#
#     ## WRITE POP_FIRST METHOD HERE ##
#     #                               #
#     #                               #
#     #                               #
#     #                               #
#     #################################
#
#
#
#
# my_linked_list _ ? 2
# ?.a.. 1)
#
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

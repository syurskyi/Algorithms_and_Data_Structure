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
#         w____  ? __ n.. N..
#             print ?.v..
#             t.. _ ?.n..
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
#     ___ pop_first
#         __ l.. __ 0
#             r_ N..
#         t.. _ h..
#         h.. _ ?.n..
#         ?.n.. _ N..
#         l.. -_ 1
#         __ l.. __ 0
#             t.. _ N..
#         r_ ?
#
#     ___ get  i..
#          __  ? < 0 __ ? >_ l..
#             r_ N..
#         t.. _ h..
#         ___ _ __ r.. ?
#             t.. _ ?.n..
#         r_ ?
#
#     ___ set_value  i.. v..
#         t.. _ g.. ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
#     ___ insert  i.. v..
#          __  ? < 0 __ ? > l..
#             r_ F..
#         __ ? __ 0
#             r_ p.. v..
#         __ ? __ l..
#             r_ a.. v..
#         n.. _ ? v..
#         t.. _ g.. ? - 1
#         n__.n.. _ ?.n..
#         ?.n.. _ ?
#         l.. +_ 1
#         r_ T..
#
#     ___ remove  i..
#          __  ? < 0 __ ? >_ l..
#             r_ N..
#         __ ? __ 0
#             r_ p..
#         __ ? __ l.. - 1
#             r_ p..
#         p.. _ g.. ? - 1
#         t.. _ ?.n..
#         ?.n.. _ ?.n..
#         ?.n.. _ N..
#         l.. -_ 1
#         r_ ?
#
#     ## WRITE REVERSE METHOD HERE ##
#     #                             #
#     #                             #
#     #                             #
#     #                             #
#     ###############################
#
#
#
#
# my_linked_list _ ? 1
# ?.a.. 2
# ?.a.. 3
# ?.a.. 4
#
# print('LL before reverse():')
# ?.p..
#
# ?.r..
#
# print('\nLL after reverse():')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     LL before reverse():
#     1
#     2
#     3
#     4
#
#     LL after reverse():
#     4
#     3
#     2
#     1
#
# """
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
#     ___ get  index
#          __  ? < 0 __ ? >_ l..
#             r_ N..
#         t.. _ h..
#         ___ _ __ r.. ?
#             t.. _ ?.n..
#         r_ ?
#
#     ___ set_value  index, v..
#         t.. _ g.. ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
#
#
#
# my_linked_list _ ? 11
# ?.a.. 3
# ?.a.. 23
# ?.a.. 7
#
# print('LL before set_value():')
# ?.p..
#
# ?.s.. 1 4
#
# print('\nLL after set_value():')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     LL before set_value():
#     11
#     3
#     23
#     7
#
#     LL after set_value():
#     11
#     4
#     23
#     7
# """
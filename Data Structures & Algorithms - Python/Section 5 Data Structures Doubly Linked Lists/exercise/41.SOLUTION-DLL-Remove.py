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
#     ___ set_value  ? value
#         t.. _ g.. ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
#     ___ insert  ? value
#         __ ? < 0 __ ? > ?
#             r_ F..
#         __ ? __ 0
#             r_ p.. ?
#         __ ? __ ?
#             r_ a.. ?
#
#         n.. _ ? ?
#         b.. _ g.. ? - 1
#         a.. _ b__.n..
#
#         ?.p.. _ b..
#         ?.n.. _ a..
#         b__.n.. _ ?
#         a__.p.. _ n..
#
#         ? =_ 1
#         r_ T..
#
#     ___ remove  index
#         __ ? < 0 __ ? >_ ?
#             r_ N..
#         __ ? __ 0
#             r_ p..
#         __ ? __ ? - 1
#             r_ p..
#
#         t.. _ get ?
#
#         ?.n__.p.. _ ?.p..
#         ?.p...n.. _ ?.n..
#         t__.n.. _ N..
#         ?.p.. _ N..
#
#         ? -_ 1
#         r_ ?
#
#
#
#
# my_doubly_linked_list = ? 1
# ?.a.. 2
# ?.a.. 3
# ?.a.. 4
# ?.a.. 5
#
# print('DLL before remove():')
# ?.p..
#
# print('\nRemoved node:')
# print(?.r.. 2 .v..
# print('DLL after remove() in middle:')
# ?.p..
#
# print('\nRemoved node:')
# print(?.r.. 0 .v..
# print('DLL after remove() of first node:')
# ?.p..
#
# print('\nRemoved node:')
# print(?.r.. 2 .v..
# print('DLL after remove() of last node:')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     DLL before remove():
#     1
#     2
#     3
#     4
#     5
#
#     Removed node:
#     3
#     DLL after remove() in middle:
#     1
#     2
#     4
#     5
#
#     Removed node:
#     1
#     DLL after remove() of first node:
#     2
#     4
#     5
#
#     Removed node:
#     5
#     DLL after remove() of last node:
#     2
#     4
#
# """
#

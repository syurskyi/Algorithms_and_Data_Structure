# c_ Node
#     ___  - value
#         ? _ ?
#         n.. _ N..
#
#
# c_ LinkedList
#     ___  - v..
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
#     ___ make_empty
#         h.. _ N..
#         t.. _ N..
#         l.. _ 0
#
#     ___ append value
#         n.. _ ? v..
#         __ h.. __ N..
#             h.. _ ?
#             t.. _ ?
#         ____
#             t__.n.. _ n..
#             t.. _ n..
#         l.. +_ 1
#
#
#
#
# my_linked_list _ ? 1
# ?.make_empty()
#
# ?.a.. 1
# ?.a.. 2
#
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n'
#
# print('Linked List:')
# ?.p..
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Head: 1
#     Tail: 2
#     Length: 2
#
#     Linked List:
#     1
#     2
#
# """

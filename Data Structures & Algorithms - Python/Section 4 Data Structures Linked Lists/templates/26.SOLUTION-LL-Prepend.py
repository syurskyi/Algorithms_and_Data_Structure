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
#             print(temp.v..
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
#
#
#
# my_linked_list _ ? 2
# ?.a.. 3)
#
# print('Before prepend():'
# print('----------------'
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n'
# print('Linked List:'
# ?.p..
#
#
# ?.p.. 1
#
#
# print('\n\nAfter prepend():'
# print('---------------'
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n'
# print('Linked List:'
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#
#     Before prepend():
#     ----------------
#     Head: 2
#     Tail: 3
#     Length: 2
#
#     Linked List:
#     2
#     3
#
#
#     After prepend():
#     ---------------
#     Head: 1
#     Tail: 3
#     Length: 3
#
#     Linked List:
#     1
#     2
#     3
#
# """
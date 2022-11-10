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
#
#
#
# my_doubly_linked_list = ? 2
# ?.append(3)
#
# print('Before prepend():')
# print('----------------')
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n'
# print('Doubly Linked List:')
# ?.p..
#
#
# ?.p.. 1
#
#
# print('\n\nAfter prepend():')
# print('---------------')
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n')
# print('Doubly Linked List:')
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
#     Doubly Linked List:
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
#     Doubly Linked List:
#     1
#     2
#     3
#
# """
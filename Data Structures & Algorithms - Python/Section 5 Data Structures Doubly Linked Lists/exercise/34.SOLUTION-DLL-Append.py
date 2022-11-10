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
#
#
#
# my_doubly_linked_list = ? 1
# ?.a.. 2
#
#
# print('Head:', ?.h__.v..
# print('Tail:', ?.t__.v..
# print('Length:', ?.l.. '\n')
#
# print('Doubly Linked List:')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Head: 1
#     Tail: 2
#     Length: 2
#
#     Doubly Linked List:
#     1
#     2
#
# """

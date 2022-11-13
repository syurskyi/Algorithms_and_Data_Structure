# c_ Node
#     ___ -  value
#         ? _ ?
#         n.. _ N..
#
#
# c_ Queue
#     ___ -  value
#         n... _ ? ?
#         f.. _ ?
#         l.. _ ?
#         ? _ 1
#
#     ___ print_queue
#         t.. _ ?
#         _____  ? __ n.. N..
#             print ?.v..
#             ? _ ?.n..
#
#     ___ enqueue value
#         n... _ ? ?
#         __ f.. __ N..
#             f.. _ ?
#             l.. _ ?
#         ____
#             ?.n.. _ ?
#             l.. _ ?
#         ? +_ 1
#
#
#
#
# my_queue = ? 1
#
# print('Queue before enqueue(2):')
# ?.p..
#
# ?.e.. 2
#
# print('\nQueue after enqueue(2):')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Queue before enqueue(2):
#     1
#
#     Queue after enqueue(2):
#     1
#     2
#
# """
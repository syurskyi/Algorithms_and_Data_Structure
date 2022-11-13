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
#         __ ? __ N..
#             f.. _ ?
#             l.. _ ?
#         ____
#             ?.n.. _ ?
#             l.. _ ?
#         ? +_ 1
#         r.. T..
#
#     ___ dequeue
#         __ ? __ 0
#             r.. N..
#         t.. _ ?
#         __ ? __ 1
#             ? _ N..
#             ? _ N..
#         ____
#             ? _ ?.n..
#             ?.n.. _ N..
#         ? -_ 1
#         r.. ?
#
#
#
#
# my_queue = Queue(1)
# my_queue.enqueue(2)
#
# # (2) Items - Returns 2 Node
# print(my_queue.dequeue().value
# # (1) Item -  Returns 1 Node
# print(my_queue.dequeue().value
# # (0) Items - Returns None
# print(my_queue.dequeue())
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     1
#     2
#     None
#
# """
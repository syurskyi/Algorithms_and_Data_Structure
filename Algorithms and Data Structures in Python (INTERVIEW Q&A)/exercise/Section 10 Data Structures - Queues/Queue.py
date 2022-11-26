#
# c_ Queue:
#
#     ? ? -
#         queue _   # list
#
#     # O(1) running time
#     ? ? is_empty
#         r_ ? __   # list
#
#     # O(1) running time
#     ? ? enqueue data
#         ?.a.. ?
#
#     # O(N) linear running time but we could use doubly linked list
#     # to achieve O(1) for all operations
#     ? ? dequeue
#         data _ ? 0
#         d.. ? 0
#         r_ ?
#
#     # O(1) constant running time
#     ? ? peek
#         r_ ? 0
#
#     # O(1)
#     ? ? size_queue
#         r_ l.. ?

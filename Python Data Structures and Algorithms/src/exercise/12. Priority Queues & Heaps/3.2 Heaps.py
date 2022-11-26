# ____ e.. _______ E..
#
#
# c_ ArrayHeap
#
#     ___ -
#         _maxsize _ 10
#         _data _ [-1] * ?
#         _currentsize _ 0
#
#     ___ -l
#         r_ l.. ?
#
#     ___ is_empty
#         r_ l.. ?
#
#     ___ maxh
#         __ ? __ 0
#             r_ ? 'Heap is empty')
#         r_ ? 1
#
#     ___ insert e
#         __ ? __ ?
#             r_ ? 'No Space'
#         ? +_ 1
#         i _ ?
#         _____ i!_ 1 ___ e > ? ?//2
#             ? ? _ ? ?//2
#             i _ ? // 2
#         ? ? _ ?
#
#     ___ deletemax
#         __ ? __ 0
#             r_ ? 'Heap is Empty'
#         x _ ? 1
#         y _ ? ?
#         ? -_ 1
#         i _ 1
#         ci _ 2
#         _____ c. <_ ?
#             __ c. < ? ___ ? ? < ? ?+1
#                 c. +_ 1
#             __ y >_ ? ?
#                 b..
#             ? ? _ ? c.
#             i _ c.
#             c. _ c. * 2
#             ? ? _ y
#
#
# h _ ArrayHeap()
# h.i.. (25)
# h.i.. (14)
# h.i.. (2)
# h.i.. (20)
# h.i.. (10)
# h.i.. (12)
# print(h._data)
# h.deletemax()
# print(h._data)

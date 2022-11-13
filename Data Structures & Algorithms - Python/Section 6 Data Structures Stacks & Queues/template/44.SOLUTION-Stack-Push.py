# c_ Node
#     ___ -  value
#         ? _ ?
#         n.. _ N..
#
#
# c_ Stack
#     ___ -  value
#         n... _ ? ?
#         t.. _ ?
#         h. _ 1
#
#     ___ print_stack
#         t.. _ t..
#         _____  ? __ n.. N..
#             print ?.v..
#             ? _ ?.n..
#
#     ___ push value
#         n... _ ? ?
#         __ ? __ 0
#             t.. _ ?
#         ____
#             ?.n.. _ t..
#             ? _ ?
#         ? +_ 1
#
#
#
#
# my_stack = ? 2
#
# print('Stack before push(1):')
# ?.p..
#
# ?.p.. 1
#
# print('\nStack after push(1):')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Stack before push(1):
#     2
#
#     Stack after push(1):
#     1
#     2
#
# """

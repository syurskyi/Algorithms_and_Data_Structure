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
#         h.. _ 1
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
#         r.. T..
#
#     ___ pop
#         __ ? __ 0
#             r.. N..
#         t.. _ t..
#         t.. _ ?.n..
#         ?.n.. _ N..
#         ? -_ 1
#         r.. ?
#
#
#
#
# my_stack = Stack(4)
# my_stack.push(3)
# my_stack.push(2)
# my_stack.push(1)
#
# print('Stack before pop():')
# my_stack.print_stack()
#
# print('\nPopped node:')
# print(my_stack.pop().value
#
# print('\nStack after pop():')
# my_stack.print_stack()
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Stack before pop():
#     1
#     2
#     3
#     4
#
#     Popped node:
#     1
#
#     Stack after pop():
#     2
#     3
#     4
#
# """
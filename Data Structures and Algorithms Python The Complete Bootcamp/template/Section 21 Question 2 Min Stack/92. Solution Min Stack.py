# c_ MinStack
#
#     ___  -
#         stack   # list
#         min   # list
#
#     ___ push  x
#         ?.a.. ?
#
#         __ min
#             __ x <= ? -1
#                 ?.a.. ?
#         ____
#             ?.a.. ?
#
#     ___ pop
#         __ ? -1 __ ? -1
#             ?.p..
#         ?.p..
#
#     ___ top
#         r_ ? -1
#
#     ___ getMin
#         r_ m.. -1
#
#
# ## Example Execution ##
# obj = MinStack()
# obj.push(10)
# obj.push(5)
# obj.push(15)
# obj.p..
# obj.push(20)
#
# result_top = obj.top()
# print("Top Value:", result_top)
#
# result_min = obj.getMin()
# print("Minimum Value __ Stack:", result_min)
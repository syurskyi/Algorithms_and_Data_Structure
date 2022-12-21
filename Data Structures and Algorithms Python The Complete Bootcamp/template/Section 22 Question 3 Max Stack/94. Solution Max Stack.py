# c_ MaxStack
#
#     ___  -
#         stack   # list
#         max   # list
#
#     ___ push  x
#         ?.a.. ?
#
#         __ max
#             __ x >_ ?-1
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
#     ___ getMax
#         r_ ? -1
#
#
# ## Example Execution ##
# obj = MaxStack()
# obj.push(10)
# obj.push(5)
# obj.p..
# obj.push(20)
# obj.push(15)
#
# result_top = obj.top()
# print("Top Value:", result_top)
#
# result_max = obj.getMax()
# print("Maximum Value __ Stack:", result_max)
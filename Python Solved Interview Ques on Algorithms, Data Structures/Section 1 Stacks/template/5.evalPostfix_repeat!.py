# c_ Stack
#     ___ -
#         stackArray _ li..
#         maxLimit _ 8
#         top _ 0
#
#     ___ push element
#         __ ? >_ m..
#             r_ ("The Stack Array Is Full!")
#         ?.a.. ?
#         ? +_ 1
#
#     ___ pop
#         __ ? <_ 0
#             r_ ("The Stack Array Is Empty!")
#         item _ ?.p..
#         ? -_ 1
#         r_ ?
#
#     ___ size
#         r_ ?
#
#     ___ isEmpty
#         r_ le. ? <_ 0
#
#
# ___ pfEval postfixExpr
#     print("input:" ?
#     stackObject _ ?
#     tokenList _ p__.sp..
#
#     ___ token __ ?
#         __ ? __ "0123456789":
#             ?.p.. in. ?
#         ____
#             operand2 _ ?.p..
#             operand1 _ ?.p..
#             result _ d.. ? _1 _2
#             ?.p.. ?
#     r_ ?.p..
#
#
# ___ doMath op op1 op2
#     __ ? __ "*"
#         r_ _1 * _2
#     ____ ? __ "/"
#         r_ _1 / _2
#     ____ ? __ "+"
#         r_ _1 + _2
#     ____
#         r_ _1 - _2
#
# print ?'1 2 3 * +'
#

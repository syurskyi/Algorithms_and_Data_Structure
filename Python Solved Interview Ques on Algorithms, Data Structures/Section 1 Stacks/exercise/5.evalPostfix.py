# c_ Stack
#     ___ -
#         stackArray _ li..
#         maxLimit _ 8
#         top _ 0
#
#     ___ push element
#         __ ? >_ mL..
#             r_ ("The Stack Array Is Full!")
#         stA__.ap.. ?
#         ? +_ 1
#
#     ___ pop
#         __ ? <_ 0
#             r_ ("The Stack Array Is Empty!")
#         item _ sA__.p..
#         ? -_ 1
#         r_ ?
#
#     ___ size
#         r_ ?
#
#     ___ isEmpty
#         r_ le. sA.. <_ 0
#
#
# ___ pfEval postfixExpr
#     print("input:" ?
#     stackObject _ ?
#     tokenList _ pE__.sp..
#
#     ___ token __ ?
#         __ ? __ "0123456789":
#             sO__.pu.. in. ?
#         ____
#             operand2 _ sO__.po.
#             operand1 _ sO__.po.
#             result _ dM.. ? _1 _2
#             sO__.pu.. ?
#     r_ sO__.po.
#
#
# ___ doMath op op1 op2
#     __ ? __ "*"
#         r_ _1 * _2
#     ____ ? __ "/"
#         r_ _1 / _2
#     ____ ? __ "+":
#         r_ _1 + _2
#     ____
#         r_ _1 - _2
#
# print ?'1 2 3 * +'
#

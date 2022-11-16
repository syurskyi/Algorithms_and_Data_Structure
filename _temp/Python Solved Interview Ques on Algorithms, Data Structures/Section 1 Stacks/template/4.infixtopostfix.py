# c_ Stack
#     ___ -
#         items _     # list
#
#     ___ isEmpty
#         r_ ? __    # list
#
#     ___ push  item
#         ?.i.. 0 ?
#
#     ___ pop
#         r_ ?.p.. 0
#
#     ___ peek
#         r_ ? 0
#
#     ___ size
#         r_ le. ?
#
# ___ iTop infixexpr
#     print "input:" ?
#     prec _    # dict
#     prec["^"] _ 4
#     prec["*"] _ 3
#     prec["/"] _ 3
#     prec["+"] _ 2
#     prec["-"] _ 2
#     prec["("] _ 1
#     stackObject _ ?
#     postfixArray _   # list
#     tokenList _ ?.sp..
#
#     ___ token __ tokenList
#         __ ? __ "ABCDEFGHIJKLMNOPQRSTUVWXYZ" o. ? __ "0123456789":
#             pA__.ap.. ?
#         ____ ?? __ '(':
#             sO__.pu.. ?
#         ____ ? __ ')'
#             topToken _ sO__.po.
#             w___ tT.. !_ '(':
#                 pA__.ap.. tT..
#                 tT.. _ sO__.p..
#         ____
#             w___ no. sO__.iE.. an. \
#                (p__|s..O___.pe.. >_ p__|?
#                   pA__.ap.. sO__.po.
#             sO__.pu.. ?
#
#     w___ no. sO__.iE..
#         pA__.ap.. sO__.po.
#     r_ " ".j.. pA..
#
# myarray_"A + B * C"
# print iT..  ?

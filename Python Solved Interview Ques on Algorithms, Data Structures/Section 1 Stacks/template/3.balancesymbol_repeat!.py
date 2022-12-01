# Write a program to balance symbols using stack
# c_ Stack
#     ___ -
#         items _    # list
#
#     ___ push  item
#         ?.ap.. ?
#
#     ___ pop
#         r_ ?.po.
#
#     ___ isEmpty
#         r_ ? __     # list
#
#     ___ peek
#         r_ ? -1
#
#     ___ -s
#         r_ st. ?
#
#
# ___ symbolmatch top symbol
#     startSymbols _ "({["
#     closeSymbols _ ")}]"
#     r_ s__.in.. ? __ c__.in.. ?
#
#
# ___ balancesymbol input
#     print("input:" ?
#     stackObject _ ?
#     balanced _ 0
#     ___ symbols __ ?
#         __ ? __ ["(", "{", "["]
#             ?.p.. ?
#         ____
#             __ ?.i..
#                 b.. _ 0
#             ____
#                 topSymbol _ ?.p..
#                 __ no. s.. t.. s..
#                     b.. _ 0
#                 ____
#                     b.. _ 1
#
#     r_ ?
#
#
# print(?("{([])}"))
#

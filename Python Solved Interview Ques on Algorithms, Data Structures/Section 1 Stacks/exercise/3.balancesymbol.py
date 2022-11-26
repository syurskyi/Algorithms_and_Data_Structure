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
#     r_ sS__.in.. ? __ cS__.in.. ?
#
#
# ___ balancesymbol input
#     print("input:" ?
#     stackObject _ ?
#     balanced _ 0
#     ___ symbols __ ?
#         __ symbols __ ["(", "{", "["]
#             sO__.pu.. ?
#         ____
#             __ sO__.iE..
#                 b.. _ 0
#             ____
#                 topSymbol _ sO__.po.
#                 __ no. s.. tS.. s..
#                     b.. _ 0
#                 ____
#                     b.. _ 1
#
#     r_ ?
#
#
# print(?("{([])}"))
#

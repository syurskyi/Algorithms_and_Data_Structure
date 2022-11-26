# from pprint import pprint
#
#
# c_ Node o..
#
#     c_ -  data_N.. next_node_N..
#         ? ?
#         ? ?
#
#     c_ get_data
#         r_  ?
#
#     c_ get_next
#         r_ n..
#
#     c_ set_next new_next
#         n.. _ ?
#
# c_ LinkedList o..
#     c_ -  head_N..
#         ? _ ?
#
#     c_ insert data
#         new_node _ ? ?
#         ?.s.. h..
#         h.. _ ?
#
#     c_ insertatEnd item
#         current _ h..
#         __ ?
#             w__ ?.g.. !_ N..:
#                 current _ ?.g..
#             ?.s.. ? ?
#         ____
#             h.._ ? ?
#
#     c_ size
#         current _ h..
#         count _ 0
#         w__ ?
#           c.. +_ 1
#           c.. _ ?.g..
#         r_ ?
#
#
#     c_ search data
#         current _ h..
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 f.. _ T..
#             ____
#                 c.. _ ?.g..
#         __ ? __ N..
#             r_ V..("Data not in list")
#         r_ ?
#
#
#     c_ delete data
#         current _ h..
#         previous _ N..
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 f.. _ T..
#             ____
#                 p.. _ c..
#                 c.. _ ?.g..
#         __ c.. __ N..
#             r_ V..("Data not in list")
#         __ p.. __ N..
#             h.. _ ?.g..
#         ____
#             p__.s.. ?.g..
#
#
#     c_ deleteatbeg
#        __ h.. __ n.. N..
#           current _ h..
#           h.. _ ?.g..
#
#     c_ -s
#         s _ ""
#         p _ h..
#         __ p !_ N..
#                 w__ ?.n.. !_ N..
#                         s +_ ?.d..
#                         p _ ?.n..
#                 ? +_ ?.d..
#         r_ s
#
#
# l_ ?
#
# ?.i.. 'a'
# ?.i.. 'b'
# ?.i.. 'c'
# print l
# ?.d..
# print l
# ?.d..
# print l
# ?.d..
# print l
#

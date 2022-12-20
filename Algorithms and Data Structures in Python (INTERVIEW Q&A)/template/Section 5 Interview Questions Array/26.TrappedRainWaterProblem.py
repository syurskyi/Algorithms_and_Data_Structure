# ? ? trapping_water_problem heights
#     __ l.. ? < 3
#         r_ 0
#
#     left_max _ 0 ___ _ __ r.. l.. ?
#     right_max _ 0 ___ _ __ r.. l.. ?
#
#     # dealing with the left max values
#     ___ i __ r.. 1, l.. ?
#         l.. ? _ m.. l.. ?- 1 , ? ? - 1
#
#     # dealing with the right max values
#     ___ i __ r..(l..(?) - 2, -1, -1
#         r.. ? _ m.. r.. ? + 1 , ? ? + 1
#
#     # consider all the items in O(N) and sum up the trapped rain water units
#     trapped _ 0
#
#     ___ i __ r.. 1 l.. ? - 1
#         __ m.. ? ? ? ? > ? ?
#             ? +_ m.. ? ?, ? ? - ? ?
#
#     r_ ?
#
#
# __ _____ __ ____
#     print(?([1, 0, 2, 1, 3, 1, 2, 0, 3]))

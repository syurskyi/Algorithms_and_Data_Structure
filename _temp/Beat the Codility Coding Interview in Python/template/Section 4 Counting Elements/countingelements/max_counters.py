# # This is the solution for CountingElements > MaxCounters
# #
# # This is marked as RESPECTABLE difficulty
#
# ___ solution N, A
#     counters _ [0] * N
#     start_line _ 0
#     current_max _ 0
#     ___ i __ ?
#         x _ ? - 1
#         __ ? > ?
#             s.. _ c..
#         ____ c.. ? < s..
#             c.. ? _ s.. + 1
#         ____
#             c.. ? +_ 1
#         __ ? <_ ? ___ c.. ? > c..
#             c.. _ c.. ?
#     ___ i __ r..(0, l.. c..
#         __ c.. ? < s..
#             c.. ? _ s..
#     r_ ?
#
# print (solution(5, [3, 4, 4, 6, 1, 4, 4]))

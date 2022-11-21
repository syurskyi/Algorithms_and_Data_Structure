# c_ Solution
#     ___ getLeftPosition nums, target
#         left _ 0
#         right _ l.. ? -1
#
#         _____ ? <_ ?
#             mid _ ?+(?-? //2
#             __ ? ? __ t..
#                 __(?-1 >_ 0 ___ ? ?-1 !_ t.. __ ? __ 0
#                     r_ ?
#                 r.. _ ?-1
#             ____ ? ? > ?
#                 r.. _ ?-1
#             ____
#                 l.. _ ?+1
#
#         r_ -1
#
#     ___ getRightPosition nums, target
#         left _ 0
#         right _ l.. ? -1
#
#         _____ ? <_ ?
#             mid _ ?+(?-? //2
#             __ ? ? __ ?
#                 __ ?+1 < l.. ? ___ ? ?+1 !_ t.. __ ? __ l.. ?-1
#                     r_ ?
#                 l.. _ ?+1
#             ____ ? ? > t..
#                 r.. _ ?-1
#             ____
#                 l.. _ ?+1
#
#         r_ -1
#
#     ___ searchRange nums: L.. i.. target i.. __ L.. i..
#         left _ ? ? ?
#         right _ ? ? ?
#
#         r_ ? ?

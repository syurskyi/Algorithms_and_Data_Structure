# ___ mergesort A
#
#     __ l.. ? > 1
#         mid _ l.. ? // 2
#         left _ ? |?
#         right _ ? ?|
#
#         ? ?
#         ? ?
#
#         i _ 0
#         j _ 0
#         k _ 0
#         _____ i < l.. ? ___ j < l.. ?
#             __ ? ? < ? ?
#                 ? ? _ ? ?
#                 i _ ? + 1
#             ____
#                 ? ? _ ? ?
#                 j _ ? + 1
#             k _ ? + 1
#
#         _____ i < l.. ?
#             ? ? _ ? ?
#             i _ ? + 1
#             k _ ? + 1
#
#         _____ j < l.. ?
#             ? ? _ ? ?
#             j _ ? + 1
#             k _ ? + 1
#
#
# A _ [84, 21, 96, 15, 47]
# print('Original Array: ', A)
# mergesort(A)
# print('Sorted Array: ', A)

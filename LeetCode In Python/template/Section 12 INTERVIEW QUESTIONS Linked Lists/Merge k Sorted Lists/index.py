# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
#
# c_ Solution
#
#     ___ mergeTwoLists l1, l2
#         cur _ ? 0
#         ans _ ?
#
#         _____ ? ___ ?
#             __ ?.v.. > ?.v..
#                 ?.n.. _ l2
#                 l2 _ ?.n..
#
#             ____
#                 ?.n.. _ l1
#                 l1 _ ?.n..
#             cur _ ?.n..
#
#         _____ ?
#             ?.n.. _ ?
#             l1 _ ?.n..
#             cur _ ?.n..
#         _____ ?
#             ?.n.. _ l2
#             l2 _ ?.n..
#             cur _ ?.n..
#         r_ ?.n..
#
#     ___ mergeKLists lists L.. ? __ L..
#         __ l.. ? __ 0
#             r_ N..
#
#         i _ 0
#         last _ l.. ?-1
#         j _ ?
#
#         _____ ? !_ 0
#             ? _ 0
#             ? _ ?
#
#             _____ j > i
#                 ? ? _ m.. ? ? ? ?
#                 ? +_ 1
#                 ? -_ 1
#                 l.. _ j
#
#         r_ ? 0

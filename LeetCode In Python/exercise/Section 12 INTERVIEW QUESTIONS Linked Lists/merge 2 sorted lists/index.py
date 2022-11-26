# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# c_ Solution
#     ___ mergeTwoLists l1 L.. l2 L.. __ L.
# 		cur _ ? 0
# 		ans _ ?
#
# 		_____ ? ___ ?
# 			__(?.v..>?.v..
# 				?.n.. _ l2
# 				l2 _ ?.n..
# 			____
# 				?.n.. _ l1
# 				l1 _ ?.n..
# 			cur _ ?.n..
#
# 		_____ ?
# 			?.n.. _ l1
# 			l1 _ ?.n..
# 			cur _ ?.n..
#
# 		_____ ?
# 			?.n.. _ l2
# 			l2 _ ?.n..
# 			cur _ ?.n..
# 		r_ ?.n..
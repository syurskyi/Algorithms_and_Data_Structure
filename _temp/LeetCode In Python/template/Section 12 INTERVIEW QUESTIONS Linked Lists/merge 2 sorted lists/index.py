# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution
    ___ mergeTwoLists l1: ListNode, l2: ListNode) __ ListNode:
		cur _ ListNode(0)
		ans _ cur
		
		_____(l1 ___ l2
			__(?.v..>?.v..
				?.n.. _ l2
				l2 _ ?.n..
			____
				?.n.. _ l1
				l1 _ ?.n..
			cur _ ?.n..
			
		_____(l1
			?.n.. _ l1
			l1 _ ?.n..
			cur _ ?.n..
		
		_____(l2
			?.n.. _ l2
			l2 _ ?.n..
			cur _ ?.n..
		r_ ans.n..
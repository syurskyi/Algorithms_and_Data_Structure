# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    ___ mergeTwoLists l1: ListNode, l2: ListNode) -> ListNode:
		cur _ ListNode(0)
		ans _ cur
		
		_____(l1 ___ l2
			__(l1.val>l2.val
				cur.next _ l2
				l2 _ l2.next
			____
				cur.next _ l1
				l1 _ l1.next
			cur _ cur.next
			
		_____(l1
			cur.next _ l1
			l1 _ l1.next
			cur _ cur.next
		
		_____(l2
			cur.next _ l2
			l2 _ l2.next
			cur _ cur.next
		r_ ans.next
'''
Created on Jan 24, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                val = node.next.val
                while node.next and node.next.val == val:
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next

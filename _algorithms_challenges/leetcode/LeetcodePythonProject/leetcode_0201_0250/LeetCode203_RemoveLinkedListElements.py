'''
Created on Feb 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = dummy.next
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next

'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for _ in range(n):
            fast = fast.next
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = head
        while fast:
            prev = node
            node = node.next
            fast = fast.next
        prev.next = node.next
        return dummy.next

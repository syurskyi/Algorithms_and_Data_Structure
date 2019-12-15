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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head and head.next:
            nextNode = head.next.next
            tmp = head.next
            prev.next = tmp
            tmp.next = head
            head.next = nextNode
            prev = head
            head = nextNode
        return dummy.next

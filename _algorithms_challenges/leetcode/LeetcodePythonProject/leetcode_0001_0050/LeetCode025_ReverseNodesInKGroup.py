'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        count = 1
        node = head
        while node:
            if count % k == 0:
                node = self.reverse(prev, node)
                prev = node
            count += 1
            node = node.next
        return dummy.next
    
    def reverse(self, prev, tail):
        nextNode = tail.next
        p = prev.next
        res = p
        while p != nextNode:
            tmp = p.next
            p.next = prev.next
            prev.next = p
            p = tmp
        res.next = p
        return res

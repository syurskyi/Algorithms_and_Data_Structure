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
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        return dummy.next

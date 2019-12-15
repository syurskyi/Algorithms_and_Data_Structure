'''
Created on Nov 8, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev = dummy
        carry = 0
        while l1 and l2:
            tmpVal = l1.val+l2.val+carry
            if tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            else:
                carry = 0
            prev.next = ListNode(tmpVal)
            l1 = l1.next
            l2 = l2.next
            prev = prev.next
        while l1:
            tmpVal = l1.val+carry
            if tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            else:
                carry = 0
            prev.next = ListNode(tmpVal)
            l1 = l1.next
            prev = prev.next
        while l2:
            tmpVal = l2.val+carry
            if tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            else:
                carry = 0
            prev.next = ListNode(tmpVal)
            l2 = l2.next
            prev = prev.next
        if carry:
            prev.next = ListNode(1)
        return dummy.next

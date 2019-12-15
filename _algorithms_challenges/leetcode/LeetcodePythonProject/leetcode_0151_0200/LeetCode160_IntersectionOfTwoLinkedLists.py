'''
Created on May 22, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode):
        self.val = x
        self.next = nextNode

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if not lenA or not lenB: return None
        if lenA < lenB:
            headA, headB = headB, headA
        diff = abs(lenA-lenB)
        while diff and headA:
            headA = headA.next
            diff -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

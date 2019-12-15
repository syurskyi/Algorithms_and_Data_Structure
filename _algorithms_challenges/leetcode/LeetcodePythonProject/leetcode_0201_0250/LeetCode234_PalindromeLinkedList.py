'''
Created on Feb 25, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        node1 = head
        node2 = head
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next
            if node2.next:
                node2 = node2.next
        mid = node1
        p1 = mid
        p2 = mid.next
        p1.next = None
        while p1 and p2:
            nextNode = p2.next
            p2.next = p1
            p1 = p2
            p2 = nextNode
        node1 = head
        node2 = p1
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

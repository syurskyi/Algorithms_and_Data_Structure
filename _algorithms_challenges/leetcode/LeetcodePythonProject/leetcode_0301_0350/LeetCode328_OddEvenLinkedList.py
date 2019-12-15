'''
Created on Mar 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head: return head
        node1 = head
        prev1 = head
        head2 = head.next
        node2 = head2
        while node1 and node2:
            prev1 = node1
            node1.next = node2.next
            node1 = node2.next
            if node1:
                prev1 = node1
                node2.next = node1.next
                node2 = node2.next
        prev1.next = head2
        return head
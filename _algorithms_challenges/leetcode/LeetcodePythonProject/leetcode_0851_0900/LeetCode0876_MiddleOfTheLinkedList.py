'''
Created on Oct 8, 2019

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        count >>= 1
        node = head
        for _ in range(count):
            node = node.next
        return node

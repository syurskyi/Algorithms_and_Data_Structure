'''
Created on Feb 10, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head)
    
    def helper(self, node):
        if not node or not node.next:
            return node
        prev = ListNode(-1)
        node1 = node
        prev.next = node1
        node2 = node
        while node2:
            node2 = node2.next
            if not node2: break
            prev = node1
            node1 = node1.next
            node2 = node2.next
        prev.next = None
        mid = node1
        result1 = self.helper(node)
        result2 = self.helper(mid)
        result = self.merge(result1, result2)
        return result
    
    def merge(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.val > node2.val:
            node = node2
            node2 = node2.next
        else:
            node = node1
            node1 = node1.next
        head = node
        while node:
            if not node1 and not node2:
                return head
            elif not node1 and node2:
                node.next = node2
                node = node.next
                node2 = node2.next
            elif node1 and not node2:
                node.next = node1
                node = node.next
                node1 = node1.next
            else:
                if node1.val < node2.val:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
                else:
                    node.next = node2
                    node = node.next
                    node2 = node2.next
        return head
    
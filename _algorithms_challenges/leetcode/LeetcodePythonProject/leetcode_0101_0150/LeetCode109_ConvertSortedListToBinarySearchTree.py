'''
Created on May 30, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        node = head
        length = 0
        self.h = head
        while node:
            node = node.next
            length += 1
        return self.helper(0, length-1)
    
    def helper(self, l, r):
        if l > r:
            return None
        mid = (l+r)//2
        left = self.helper(l, mid-1)
        root = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.helper(mid+1, r)
        root.left = left
        root.right = right
        return root

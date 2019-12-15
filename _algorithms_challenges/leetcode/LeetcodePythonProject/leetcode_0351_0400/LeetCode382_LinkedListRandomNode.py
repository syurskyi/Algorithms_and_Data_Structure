'''
Created on Apr 2, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        self.head = head
    
    def getRandom(self):
        import random
        res = -1
        count = 0
        node = self.head
        while node:
            if random.randint(0, count) == 0:
                res = node.val
            count += 1
            node = node.next
        return res

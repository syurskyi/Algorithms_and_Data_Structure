'''
Created on Apr 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        nextNode = None
        while stack1 and stack2:
            v1, v2 = stack1.pop(), stack2.pop()
            val = v1 + v2 + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(val)
            node.next = nextNode
            nextNode = node
        if stack2 and not stack1:
            stack1, stack2 = stack2, stack1
        while stack1:
            val = stack1.pop() + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(val)
            node.next = nextNode
            nextNode = node
        if carry:
            node = ListNode(1)
            node.next = nextNode
            nextNode = node
        return nextNode

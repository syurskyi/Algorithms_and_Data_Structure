'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return head
        newHead = RandomListNode(head.label)
        newNode = newHead
        hashmap = {head: newHead}
        node = head.next
        while node:
            tmp = RandomListNode(node.label)
            hashmap[node] = tmp
            newNode.next = tmp
            newNode = newNode.next
            node = node.next
        node = head
        newNode = newHead
        while node:
            if node.random:
                newNode.random = hashmap[node.random]
            else:
                newNode.random = None
            node = node.next
            newNode = newNode.next
        return newHead
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
'''
Created on Jan 28, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n or not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        for _ in range(1, m):
            if not head:
                return None
            head = head.next
        prevNode = head
        mNode = head.next
        nNode, postnNode = mNode, mNode.next
        for _ in range(m, n):
            if not postnNode:
                return None
            tmp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = tmp
        mNode.next = postnNode
        prevNode.next = nNode
        return dummy.next
    
    def test(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        node = self.reverseBetween(head, 2, 4)
        while node:
            print(node.val)
            node = node.next
        print

def main():
    Solution().test()

if __name__ == '__main__':
    main()
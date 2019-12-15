'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        node = head
        node2 = head.next
        while node and node2:
            node2 = node2.next
            if not node2:
                break
            node2 = node2.next
            node = node.next
        head2 = node.next
        node.next = None
        head2 = self.reverse(head2)
        self.merge(head, head2)
    
    def reverse(self, root):
        if not root or not root.next: return root
        p1, p2 = root, root.next
        p1.next = None 
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1
    
    def merge(self, head1, head2):
        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
    
    def test(self):
        testCases = [
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
        ]
        for head in testCases:
            print('before:')
            node = head
            while node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            self.reorderList(head)
            print('after:')
            node = head
            while node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
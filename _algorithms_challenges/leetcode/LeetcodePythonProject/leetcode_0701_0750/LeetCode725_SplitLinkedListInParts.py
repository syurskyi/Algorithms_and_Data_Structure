'''
Created on Feb 21, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        length = 0
        head = root
        while head:
            head = head.next
            length += 1
        length0 = length//k
        count0 = length-length0*k
        lengths = [length0]*k
        for i in range(count0):
            lengths[i] += 1
        head = root
        prev = ListNode(-1)
        prev.next = head
        prevHead = head
        i = 0
        print('lengths: %s' % lengths)
        print('length: %s' % length)
        print('count0: %s' % count0)
        while head:
            if lengths[i] == 0:
                prev.next = None
                i += 1
                res.append(prevHead)
                prevHead = head
            lengths[i] -= 1
            prev = head
            head = head.next
        res.append(prevHead)
        for _ in range(i+1, k):
            res.append(None)
        return res
    
    def test(self):
        testCases = [
            [
                ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
                5,
            ],
            [
                ListNode(1, ListNode(2, ListNode(3))),
                5,
            ],
        ]
        for head, k in testCases:
            res = self.splitListToParts(head, k)
            print('res: %s' % res)

if __name__ == '__main__':
    Solution().test()

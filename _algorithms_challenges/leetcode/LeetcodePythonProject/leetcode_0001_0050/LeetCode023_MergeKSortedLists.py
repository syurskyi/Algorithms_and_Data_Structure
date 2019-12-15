'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        dummy = ListNode(-1)
        prev = dummy
        while heap:
            val = heapq.heappop(heap)
            prev.next = ListNode(val)
            prev = prev.next
        return dummy.next
    
    def test(self):
        testCases = [
            [
                ListNode(-1, ListNode(-1, ListNode(-1))),
                ListNode(-2, ListNode(-2, ListNode(-1))),
            ],
        ]
        for lists in testCases:
            node = self.mergeKLists(lists)
            while node:
                print('%s -> ' % node.val, end='')
                node = node.next
            print('')
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

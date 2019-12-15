'''
Created on Mar 23, 2017

@author: MT
'''

import heapq

class Solution(object):
    def rearrangeString(self, s, k):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        heap = []
        for c, freq in hashmap.items():
            heapq.heappush(heap, [-freq, c])
        queue = []
        res = []
        while heap:
            freq, c = heapq.heappop(heap)
            res.append(c)
            queue.append([freq, c])
            if len(queue) < k:
                continue
            freq, c = queue.pop(0)
            freq = -freq-1
            if freq > 0:
                heapq.heappush(heap, [-freq, c])
        return ''.join(res) if len(res) == len(s) else ''
    
    def test(self):
        testCases = [
            ('aabbcc', 3),
            ('aaabc', 3),
            ('aaadbbcc', 2),
        ]
        for s, k in testCases:
            print('s: %s' % (s))
            print('k: %s' % (k))
            result = self.rearrangeString(s, k)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

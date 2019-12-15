'''
Created on Apr 3, 2018

@author: tongq
'''
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import heapq
        s = S
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        heap = []
        for c, freq in hashmap.items():
            heapq.heappush(heap, [-freq, c])
        res = ''
        while heap:
            freq1, c1 = heapq.heappop(heap)
            if res and res[-1] == c1:
                return ''
            res += c1
            if heap:
                freq2, c2 = heapq.heappop(heap)
                res += c2
                if freq2+1 < 0:
                    heapq.heappush(heap, [freq2+1, c2])
            if freq1+1 < 0:
                heapq.heappush(heap, [freq1+1, c1])
        return ''.join(res)
    
    def test(self):
        testCases = [
            "vvvlo",
            "aab",
            'aaab',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.reorganizeString(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

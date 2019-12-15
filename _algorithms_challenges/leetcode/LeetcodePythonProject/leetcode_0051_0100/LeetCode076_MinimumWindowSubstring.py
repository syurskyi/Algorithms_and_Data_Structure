'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap0 = {}
        for c in t:
            hashmap0[c] = hashmap0.get(c, 0)+1
        left = 0
        res = ''
        minLen = float('inf')
        hashmap = {}
        count = 0
        for i, c in enumerate(s):
            hashmap[c] = hashmap.get(c, 0)+1
            if c in hashmap0 and hashmap[c] == hashmap0[c]:
                count += 1
            while left <= i and hashmap[s[left]] > hashmap0.get(s[left], 0):
                hashmap[s[left]] -= 1
                left += 1
            if count == len(hashmap0):
                if minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
                if hashmap0.get(s[left], 0) == hashmap[s[left]]:
                    count -= 1
                hashmap[s[left]] -= 1
                left += 1
        return res
    
    def minWindow_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = {}
        for c in t:
            hashmap[c] = hashmap.get(c, 0)+1
        left = 0
        hashmapAll = {}
        hashset = set()
        res = ''
        minLen = float('inf')
        for i, c in enumerate(s):
            if c in hashmap and hashmapAll.get(c, 0)+1 >= hashmap[c]:
                hashset.add(c)
            hashmapAll[c] = hashmapAll.get(c, 0)+1
            while left < i and (s[left] not in hashmap or hashmapAll[s[left]] > hashmap[s[left]]):
                hashmapAll[s[left]] -= 1
                if hashmapAll[s[left]] < hashmap.get(s[left], 0):
                    hashset.discard(s[left])
                if hashmapAll[s[left]] == 0:
                    del hashmapAll[s[left]]
                left += 1
            if len(hashset) == len(hashmap):
                if minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
        return res
    
    def test(self):
        testCases = [
            ('ADOBECODEBANC', 'ABC'),
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        for s, t in testCases:
            print('s: %s' % (s))
            print('t: %s' % (t))
            result = self.minWindow(s, t)
            print('result: %s' % (result))
            print('-='*15 + '-')

Solution().test()
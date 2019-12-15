'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object):
    def longestSubstring_orig(self, s, k):
        if len(s) < k:
            return 0
        c = min([(s.count(c), c) for c in s])[1]
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring_orig(t, k) for t in s.split(c))
    
    def longestSubstring(self, s, k):
        if len(s) < k: return 0
        minChar, minCount = 0, float('inf')
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        for c in s:
            if hashmap[c] < minCount:
                minCount = hashmap[c]
                minChar = c
        if hashmap[minChar] >= k:
            return len(s)
        maxRes = float('-inf')
        for t in s.split(minChar):
            maxRes = max(maxRes, self.longestSubstring(t, k))
        return maxRes
    
    def longestSubstring_another(self, s, k):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        splitSet = set()
        for c, freq in hashmap.items():
            if freq < k:
                splitSet.add(c)
        if not splitSet: return len(s)
        print('splitSet: %s' % splitSet)
        maxLen = 0
        prev = 0
        for i in range(len(s)):
            if s[i] in splitSet:
                if prev < i:
                    maxLen = max(maxLen, self.longestSubstring_another(s[prev:i], k))
                prev = i+1
        if prev < len(s):
            maxLen = max(maxLen, self.longestSubstring_another(s[prev:], k))
        return maxLen
    
    def test(self):
        testCases = [
            ('aaabb', 3),
            ('ababbc', 2),
            ("weitong", 2),
            ("bbaaacbd", 3),
        ]
        for s, k in testCases:
            print('s: %s' % s)
            print('k: %s' % k)
            result = self.longestSubstring(s, k)
            print('result: %s' % result)
            result = self.longestSubstring_another(s, k)
            print('another result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

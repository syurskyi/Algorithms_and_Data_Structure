'''
Created on Mar 20, 2017

@author: MT
'''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k <= 0: return 0
        hashmap = {}
        maxLen = 0
        left = 0
        for i, c in enumerate(s):
            hashmap[c] = i
            while left <= i and len(hashmap) > k:
                if s[left] in hashmap and left == hashmap[s[left]]:
                    del hashmap[s[left]]
                left+=1
            maxLen = max(maxLen, i-left+1)
        return maxLen
    
    def test(self):
        testCases = [
            ('eceba', 2),
            ('abddebddesbaddes', 3),
        ]
        for s, k in testCases:
            print('s: %s, k: %s' % (s, k))
            result = self.lengthOfLongestSubstringKDistinct(s, k)
            print('result: %s' % (str(result)))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

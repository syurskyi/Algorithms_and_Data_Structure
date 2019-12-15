'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        l = 0
        res = 0
        for i, c in enumerate(s):
            hashmap[c] = hashmap.get(c, 0)+1
            while len(hashmap) > 2:
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0: del hashmap[s[l]]
                l += 1
            res = max(res, i-l+1)
        res = max(res, len(s)-l)
        return res
    
    def test(self):
        testCases = [
            'abccccbbb',
            'eceba',
            'abc',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.lengthOfLongestSubstringTwoDistinct(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

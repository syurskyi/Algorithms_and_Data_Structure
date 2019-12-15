'''
Created on May 5, 2017

@author: MT
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        hashset = set()
        maxLen = 0
        for i, c in enumerate(s):
            while left < i and c in hashset:
                hashset.discard(s[left])
                left += 1
            hashset.add(c)
            maxLen = max(maxLen, i-left+1)
        return maxLen
    
    def test(self):
        testCases = [
            'abc',
            'bbbb',
            'abcdba',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.lengthOfLongestSubstring(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

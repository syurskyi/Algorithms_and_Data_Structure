'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        for c in p:
            arr0[ord(c)-ord('a')] += 1
        left = 0
        res = []
        arr = [0]*26
        for i, c in enumerate(s):
            arr[ord(c)-ord('a')] += 1
            while left <= i and arr[ord(c)-ord('a')] > arr0[ord(c)-ord('a')]:
                arr[ord(s[left])-ord('a')] -= 1
                left += 1
            if i-left+1 == len(p):
                res.append(left)
        return res
    
    def findAnagrams_orig(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        count = len(p)
        for c in p:
            arr0[ord(c)-ord('a')] += 1
        left = 0
        arr1 = [0]*26
        result = []
        end = 0
        while end < len(s):
            numInd = ord(s[end]) - ord('a')
            if arr1[numInd] < arr0[numInd]:
                arr1[numInd] += 1
                count -= 1
                end += 1
                if count == 0:
                    result.append(left)
            else:
                arr1[ord(s[left]) - ord('a')] -= 1
                count += 1
                left += 1
        return result
    
    def test(self):
        testCases = [
            ('cbaebabacd', 'abc'),
            ('abab', 'ab'),
        ]
        for s, p in testCases:
            result = self.findAnagrams(s, p)
            print('result: %s' % result)
            result0 = self.findAnagrams_orig(s, p)
            print('result0: %s' % result0)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    def characterReplacement(self, s, k):
        arr = [0]*26
        maxCount = 0
        left = 0
        res = 0
        for i, c in enumerate(s):
            ind = ord(c)-ord('A')
            arr[ind] += 1
            maxCount = max(maxCount, arr[ind])
            if left <= i and maxCount+k<i-left+1:
                arr[ord(s[left])-ord('A')] -= 1
                left += 1
            res = max(res, i-left+1)
        return res
    
    def test(self):
        testCases = [
            ('ABAB', 2),
            ('AABABBA', 1),
        ]
        for s, k in testCases:
            print('s: %s' % s)
            print('k: %s' % k)
            result = self.characterReplacement(s, k)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

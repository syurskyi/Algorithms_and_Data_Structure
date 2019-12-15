'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ''
        count = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                res = S[i].upper() + res
                count += 1
                if count > 0 and count % K == 0:
                    res = '-' + res
        return res.lstrip('-')
    
    def test(self):
        testCases = [
            ('abc-abc', 3),
        ]
        for s, k in testCases:
            result = self.licenseKeyFormatting(s, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

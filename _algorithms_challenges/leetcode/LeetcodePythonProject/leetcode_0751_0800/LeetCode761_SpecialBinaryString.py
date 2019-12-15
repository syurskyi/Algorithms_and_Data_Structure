'''
Created on Mar 31, 2018

@author: tongq
'''
class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        i = 0
        res = []
        for j, c in enumerate(S):
            count = count+1 if c=='1' else count-1
            if count == 0:
                res.append('1'+self.makeLargestSpecial(S[i+1:j])+'0')
                i = j+1
        return ''.join(sorted(res, reverse=True))
    
    def test(self):
        testCases = [
            '11011000',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.makeLargestSpecial(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

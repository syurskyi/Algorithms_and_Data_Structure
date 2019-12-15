'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        s = s.strip()
        if not s or s == '+': return 0
        sig = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            sig = -1
        s = s.lstrip('0')
        res = 0
        for c in s:
            if not c.isdigit():
                break
            res = 10*res + ord(c) - ord('0') 
        if sig > 0:
            return min(2**32-1, res)
        else:
            return max(-2**31, sig*res)
    
    def test(self):
        testCases = [
            '    010',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.myAtoi(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

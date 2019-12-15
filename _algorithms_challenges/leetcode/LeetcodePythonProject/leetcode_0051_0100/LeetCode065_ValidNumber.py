'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        s = s.lstrip('-')
        s = s.lstrip('+')
        i = 0
        num, dot, exp = False, False, False
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = True
            elif c == '.':
                if exp or dot:
                    return False
                dot = True
            elif c == 'e':
                if exp or not num:
                    return False
                exp = True
                num = False
            elif c == '+' or c == '-':
                if s[i-1] != 'e':
                    return False
            else:
                return False
            i += 1
        return num
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
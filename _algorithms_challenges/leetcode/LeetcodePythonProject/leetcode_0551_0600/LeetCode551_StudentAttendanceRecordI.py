'''
Created on Aug 22, 2017

@author: MT
'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = False
        for i, c in enumerate(s):
            if c == 'A':
                if not absent:
                    absent = True
                else:
                    return False
            elif c == 'L':
                if i > 1 and s[i-1] == 'L' and s[i-2] == 'L':
                    return False
        return True
    
    def test(self):
        testCases = [
            'PPALLP',
            'PPALLL',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.checkRecord(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 5, 2017

@author: MT
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up, left = 0, 0
        for c in moves:
            if c == 'L':
                left += 1
            elif c == 'R':
                left -= 1
            elif c == 'U':
                up += 1
            else:
                up -= 1
        return up == 0 and left == 0
    
    def test(self):
        testCases = [
            'UD',
            'LL',
        ]
        for moves in testCases:
            print('moves: %s' % moves)
            result = self.judgeCircle(moves)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

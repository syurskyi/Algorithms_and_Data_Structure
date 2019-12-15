'''
Created on Jan 31, 2019

@author: tongq
'''
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        res = []
        self.helper(s, 0, res)
        return res if len(res) > 2 else []
    
    def helper(self, s, i, res):
        if i >= len(s) and len(res) > 2:
            return True
        for j in range(i+1, len(s)+1):
            s0 = s[i:j]
            num = int(s0)
            if num > 2**31-1 or (s0[0] == '0' and len(s0) > 1):
                break
            if len(res) < 2 or res[-2] + res[-1] == num:
                res.append(num)
                if self.helper(s, j, res):
                    return True
                res.pop()
        return False
    
    def test(self):
        testCases = [
            '123456579',
            '11235813',
            '112358130',
            '0123',
            '1101111',
            "1011",
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.splitIntoFibonacci(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

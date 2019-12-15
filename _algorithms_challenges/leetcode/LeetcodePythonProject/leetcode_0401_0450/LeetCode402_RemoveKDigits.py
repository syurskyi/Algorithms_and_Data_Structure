'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        longest = n-k
        if k >= n: return '0'
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        stack = stack[:longest]
        res = ''.join(stack)
        res = res.lstrip('0')
        return res if res else '0'
    
    def test(self):
        testCases = [
            ("1432219", 3),
            ("10200", 1),
            ("10", 2),
            ("112", 1),
            ("1234567890", 9),
            ("1173", 2),
        ]
        for num, k in testCases:
            print('num: %s' % num)
            print('k: %s' % k)
            result = self.removeKdigits(num, k)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

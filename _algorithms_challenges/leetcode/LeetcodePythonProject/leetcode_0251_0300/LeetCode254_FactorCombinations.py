'''
Created on Mar 1, 2017

@author: MT
'''

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, stack, x = [], [], 2
        while True:
            if x > n//x:
                if not stack:
                    return res
                res.append(stack+[n])
                x = stack.pop()
                n *= x
                x += 1
            elif n % x == 0:
                stack.append(x)
                n = n//x
            else:
                x += 1
    
    def getFactorsSlow(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(result, [], n, 2)
        return result
    
    def helper(self, result, item, n, start):
        if n <= 1:
            if len(item)>1:
                result.append(list(item))
            return
        
        for i in range(start, n+1):
            if n % i == 0:
                item.append(i)
                self.helper(result, item, int(n/i), i)
                item.pop()
    
    def test(self):
        testCases = [
            8,
            1,
            2,
            32,
            23848713,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.getFactors(n)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

    
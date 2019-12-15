'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
        sign = 1
        if (dividend > 0 and divisor < 0) or\
            (dividend < 0 and divisor > 0):
            sign = -1
        if dividend < 0: dividend = -dividend
        if divisor < 0: divisor = -divisor
        if divisor == 0: return 2**32-1
        if dividend == 0 or dividend < divisor:
            return 0
        res = self.ldivide(dividend, divisor)
        if res >= 2**31-1:
            res = 2**31-1 if sign == 1 else -2**31
        else:
            res = res if sign > 0 else -res
        return res
        
    def ldivide(self, dividend, divisor):
        if dividend < divisor: return 0
        sumVal = divisor
        multiple = 1
        while sumVal+sumVal <= dividend:
            sumVal += sumVal
            multiple += multiple
        return multiple + self.ldivide(dividend-sumVal, divisor)
    
    def test(self):
        testCases = [
            [1, 1],
            [5, 2],
            [-1, 1],
            [-2147483648, -1],
        ]
        for dividend, divisor in testCases:
            print('dividend: %s' % dividend)
            print('divisor: %s' % divisor)
            result = self.divide(dividend, divisor)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

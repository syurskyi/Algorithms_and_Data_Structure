'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10: return a
        res = []
        for i in range(9, 1, -1):
            while a%i == 0:
                res.append(i)
                a //= i
        if a >= 10 or not res: return 0
        result = ''
        for i in range(len(res)-1, -1, -1):
            result += str(res[i])
        result = int(result)
        return result if result < 2**31-1 else 0
    
    def test(self):
        testCases = [
            48,
            15,
            11,
            22,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.smallestFactorization(num)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

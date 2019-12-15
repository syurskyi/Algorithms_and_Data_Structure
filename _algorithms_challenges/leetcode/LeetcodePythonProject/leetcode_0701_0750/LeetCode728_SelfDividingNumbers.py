'''
Created on Mar 4, 2018

@author: tongq
'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            if self.isSelfDividing(num):
                res.append(num)
        return res
        
    def isSelfDividing(self, num):
        for digit in str(num):
            d = int(digit)
            if d == 0 or num%d != 0:
                return False
        return True
    
    def test(self):
        testCases = [
            [1, 22],
        ]
        for left, right in testCases:
            print('left: %s' % left)
            print('right: %s' % right)
            result = self.selfDividingNumbers(left, right)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

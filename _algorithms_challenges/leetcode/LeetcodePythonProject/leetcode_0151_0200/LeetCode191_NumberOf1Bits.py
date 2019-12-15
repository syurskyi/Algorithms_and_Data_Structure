'''
Created on Feb 16, 2017

@author: MT
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            if (n >> i)&1 == 1:
                count+=1
        return count
    
    def test(self):
        testCases = [
            int('00000000000000000000000000001011', 2),
        ]
        for n in testCases:
            print('n:      {0:032b}'.format(n))
            result = self.hammingWeight(n)
            print('result: {0:d}'.format(result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
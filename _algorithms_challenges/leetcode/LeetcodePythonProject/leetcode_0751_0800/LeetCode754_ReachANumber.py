'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sumVal = 0
        while sumVal < target:
            step += 1
            sumVal += step
        while (sumVal-target)%2 != 0:
            step += 1
            sumVal += step
        return step
    
    def test(self):
        testCases = [
            3,
            2,
        ]
        for target in testCases:
            print('target: %s' % target)
            result = self.reachNumber(target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

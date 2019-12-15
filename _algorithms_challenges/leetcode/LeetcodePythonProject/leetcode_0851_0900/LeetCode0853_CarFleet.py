'''
Created on Sep 10, 2019

@author: tongq
'''
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
    
    def test(self):
        testCases = [
            [
                12,
                [10, 8, 0, 5, 3],
                [2, 4, 1, 1, 3],
            ],
        ]
        for target, position, speed in testCases:
            res = self.carFleet(target, position, speed)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

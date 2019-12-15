'''
Created on Aug 24, 2017

@author: MT
'''

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        for vals in wall:
            sumVal = 0
            for val in vals:
                sumVal += val
                hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        minRes = len(wall)
        for val, count in hashmap.items():
            if 1 <= val < sum(wall[0]): # not the start and end
                minRes = min(minRes, len(wall)-count)
        return minRes
    
    def test(self):
        testCases = [
            [
                [1,2,2,1],
                [3,1,2],
                [1,3,2],
                [2,4],
                [3,1,2],
                [1,3,1,1],
            ],
        ]
        for wall in testCases:
            print('wall:')
            print('\n'.join([str(row) for row in wall]))
            result = self.leastBricks(wall)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

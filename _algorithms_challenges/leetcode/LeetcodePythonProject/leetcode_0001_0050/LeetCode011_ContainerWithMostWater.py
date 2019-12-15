'''
Created on Jan 9, 2017

@author: MT
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        i, j = 0, len(height)-1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area

    def test(self):
        testCases = [
            [1, 3, 9, 2],
        ]
        for height in testCases:
            print('height: %s' % (height))
            result = self.maxArea(height)
            print('result: %s' % (result))
            print('-='*15 + '-')

if __name__ == '__main__':
    Solution().test()
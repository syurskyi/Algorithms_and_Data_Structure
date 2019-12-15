'''
Created on Mar 11, 2017

@author: MT
'''

class Solution(object):
    def minArea(self, image, x, y):
        m, n = len(image), len(image[0])
        left = self.searchColumns(image, 0, y, 0, m, True)
        right = self.searchColumns(image, y+1, n, 0, m, False)
        top = self.searchRows(image, 0, x, left, right, True)
        bottom = self.searchRows(image, x+1, m, left, right, False)
        return (right-left)*(bottom-top)
    
    def searchColumns(self, image, i, j, top, bottom, opt):
        while i < j:
            k, mid = top, (i+j)//2
            while k < bottom and image[k][mid] == '0':
                k+=1
            if (k < bottom) == opt:
                j = mid
            else:
                i = mid+1
        return i
    
    def searchRows(self, image, i, j, left, right, opt):
        while i < j:
            k, mid = left, (i+j)//2
            while k < right and image[mid][k] == '0':
                k+=1
            if (k < right) == opt:
                j = mid
            else:
                i  = mid+1
        return i
    
    def test(self):
        testCases = [
            (
                [
                    '0010',
                    '0110',
                    '0100',
                ],
                0, 2
            ),
        ]
        for image, x, y in testCases:
            result = self.minArea(image, x, y)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

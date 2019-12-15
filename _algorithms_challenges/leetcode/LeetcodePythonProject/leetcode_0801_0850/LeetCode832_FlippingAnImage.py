'''
Created on Jun 9, 2018

@author: tongq
'''
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        image = A
        if not image or not image[0]: return
        m, n = len(image), len(image[0])
        for i in range(m):
            j, l = 0, n-1
            while j <= l:
                image[i][j], image[i][l] = image[i][l], image[i][j]
                image[i][j] = 1 if not image[i][j] else 0
                if j < l:
                    image[i][l] = 1 if not image[i][l] else 0
                j += 1
                l -= 1
        return image
    
    def test(self):
        testCases = [
            [[1,1,0],[1,0,1],[0,0,0]],
        ]
        for image in testCases:
            res = self.flipAndInvertImage(image)
            print('res: %s' % res)

if __name__ == '__main__':
    Solution().test()

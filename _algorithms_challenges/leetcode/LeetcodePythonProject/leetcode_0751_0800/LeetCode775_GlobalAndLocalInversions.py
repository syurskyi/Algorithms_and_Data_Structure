'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        cmax = 0
        for i in range(len(arr)-2):
            cmax = max(cmax, arr[i])
            if cmax > arr[i+2]:
                return False
        return True
    
    def test(self):
        testCases = [
            [1,0,2],
            [1,2,0],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.isIdealPermutation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

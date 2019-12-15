'''
Created on Apr 10, 2018

@author: tongq
'''
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # Use Java PriorityQueue comparator
        pass
    
    def test(self):
        testCases = [
            [ [1, 2, 3, 5], 3 ],
            [ [1, 7], 1 ],
        ]
        for arr, k in testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            result = self.kthSmallestPrimeFraction(arr, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

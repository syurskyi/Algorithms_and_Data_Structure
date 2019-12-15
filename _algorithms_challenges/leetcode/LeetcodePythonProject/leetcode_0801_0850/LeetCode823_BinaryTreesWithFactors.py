'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        MOD = 10**9+7
        res = 0
        arr.sort()
        hashmap = {}
        for i in range(len(arr)):
            hashmap[arr[i]] = 1
            for j in range(i):
                if arr[j] in hashmap and arr[i]%arr[j]==0 and\
                    arr[i]/arr[j] in hashmap:
                    hashmap[arr[i]] += hashmap[arr[j]]*hashmap[(arr[i]/arr[j])]
            res = (res+hashmap[arr[i]])%MOD
        return res
    
    def test(self):
        testCases = [
            [2, 4],
            [2, 4, 5, 10],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.numFactoredBinaryTrees(arr)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Apr 3, 2018

@author: tongq
'''
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        hashmap = {}
        idx = 0
        res = 0
        while idx < len(row):
            hashmap[row[idx]] = row[idx+1]
            hashmap[row[idx+1]] = row[idx]
            idx += 2
        idx = 0
        while idx < len(row):
            if hashmap[idx] != idx+1:
                nextVal = hashmap[idx+1]
                currVal = hashmap[idx]
                hashmap[currVal] = nextVal
                hashmap[nextVal] = currVal
                res += 1
            idx += 2
        return res
    
    def test(self):
        testCases = [
            [0, 2, 1, 3],
            [3, 2, 0, 1],
        ]
        for row in testCases:
            print('row: %s' % row)
            result = self.minSwapsCouples(row)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

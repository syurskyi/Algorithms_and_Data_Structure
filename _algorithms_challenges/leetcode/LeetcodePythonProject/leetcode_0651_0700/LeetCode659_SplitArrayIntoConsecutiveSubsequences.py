'''
Created on Oct 7, 2017

@author: MT
'''
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freqMap, appendFreqMap = {}, {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0)+1
        for num in nums:
            if freqMap[num] == 0:
                continue
            elif appendFreqMap.get(num, 0) > 0:
                appendFreqMap[num] -= 1
                appendFreqMap[num+1] = appendFreqMap.get(num+1, 0)+1
            elif freqMap.get(num+1, 0)>0 and freqMap.get(num+2, 0)>0:
                freqMap[num+1] -= 1
                freqMap[num+2] -= 1
                appendFreqMap[num+3] = appendFreqMap.get(num+3, 0)+1
            else:
                return False
            freqMap[num] -= 1
        return True
    
    def test(self):
        testCases = [
            [1, 2, 3, 3, 4, 5],
            [1, 2, 2, 3, 3, 3, 4, 4, 5],
            [1, 2, 3, 3, 4, 4, 5, 5],
            [1, 2, 3, 4, 4, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.isPossible(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

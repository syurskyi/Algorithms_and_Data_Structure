'''
Created on Aug 27, 2017

@author: MT
'''
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        arr = list(s)
        i = len(s)-1
        while i > 0 and arr[i-1] >= arr[i]:
            i -= 1
        if i == 0:
            return -1
        j = len(s)-1
        ind = i
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        j = ind
        while j < len(s) and arr[j] <= arr[ind-1]:
            j += 1
        arr[ind-1], arr[j] = arr[j], arr[ind-1]
        res = int(''.join(arr))
        if res >= 1 << 32-1:
            return -1
        return res
    
    def test(self):
        testCases = [
            21,
            123,
            4112,
            12000,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.nextGreaterElement(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

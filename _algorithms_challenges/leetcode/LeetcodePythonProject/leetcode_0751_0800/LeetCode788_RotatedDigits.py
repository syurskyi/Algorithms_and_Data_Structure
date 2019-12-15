'''
Created on Apr 12, 2018

@author: tongq
'''
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for num in range(1, N+1):
            if self.checkNum(num):
                cnt += 1
        return cnt
    
    def checkNum(self, num):
        arr = list(str(num))
        i, j = 0, len(arr)-1
        arr0 = ['']*len(arr)
        hashmap = {
            '1':'1',
            '2':'5',
            '5':'2',
            '6':'9',
            '8':'8',
            '9':'6',
            '0':'0',
        }
        while i <= j:
            if arr[i] in hashmap and arr[j] in hashmap:
                arr0[i], arr0[j] = hashmap[arr[i]], hashmap[arr[j]]
                i += 1
                j -= 1
            else:
                return False
        return arr0 != arr
    
    def test(self):
        testCases = [
            10,
            100,
            857,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.rotatedDigits(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

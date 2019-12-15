'''
Created on Oct 10, 2018

@author: tongq
'''
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        arr = list(dominoes)
        i = 0
        while i < n and arr[i] == '.':
            i += 1
        if i < n and arr[i] == 'L' and i > 0:
            arr[0] = 'L'
            self.setVals(arr, 0, i)
        while i < n:
            if arr[i] == 'L' or arr[i] == 'R':
                j = i+1
                while j < n and arr[j] == '.':
                    j += 1
                if j < n:
                    self.setVals(arr, i, j)
            i += 1
        i = n-1
        while i >= 0 and arr[i] == '.':
            i -= 1
        if i >= 0 and arr[i] == 'R' and i < n:
            arr[-1] = 'R'
            self.setVals(arr, i, n-1)
        return ''.join(arr)
    
    def setVals(self, arr, i, j):
        if arr[i] == arr[j]:
            for i0 in range(i+1, j):
                arr[i0] = arr[i]
        elif arr[i] == 'R' and arr[j] == 'L':
            i0, j0 = i, j
            while i < j:
                arr[i] = arr[i0]
                arr[j] = arr[j0]
                i += 1
                j -= 1
    
    def test(self):
        testCases = [
            '.',
            '.L.R...LR..L..',
            'RR.L',
            '.L.R.',
            'R..L..R..LR.R.R.....',
        ]
        for dominoes in testCases:
            print('origin: %s' % dominoes)
            result = self.pushDominoes(dominoes)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

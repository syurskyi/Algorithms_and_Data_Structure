'''
Created on Jun 6, 2019

@author: tongq
'''
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = S
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        return ''.join(chr((ord(c)-97+num) % 26 + 97) for c, num in zip(s, shifts))
    
    def test(self):
        testCases = [
            ['abc', [3, 5, 9]],
        ]
        for s, shifts in testCases:
            result = self.shiftingLetters(s, shifts)
            print('result: %s' % result)

if __name__ == '__main__':
    Solution().test()

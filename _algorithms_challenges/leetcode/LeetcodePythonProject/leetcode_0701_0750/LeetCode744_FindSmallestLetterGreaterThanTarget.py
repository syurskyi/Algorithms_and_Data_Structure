'''
Created on Mar 22, 2018

@author: tongq
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters)
        while l < r:
            mid = (l+r)//2
            if target >= letters[mid]:
                l = mid+1
            else:
                r = mid
        return letters[l] if l < len(letters) else letters[0]
    
    def test(self):
        testCases = [
            [
                ["c", "f", "j"],
                'a',
            ],
            [
                ["c", "f", "j"],
                "c",
            ],
            [
                ["c", "f", "j"],
                'd',
            ],
            [
                ["c", "f", "j"],
                'j',
            ],
        ]
        for letters, target in testCases:
            result = self.nextGreatestLetter(letters, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l, r = 0, len(people)-1
        res = 0
        while l <= r:
            w = people[r]
            if l < r and w + people[l] <= limit:
                l += 1
            res += 1
            r -= 1
        return res
    
    def test(self):
        testCases = [
            [
                [3,2,3,2,2],
                6,
            ],
            [
                [1,2], 3,
            ],
            [
                [3,2,2,1], 3,
            ],
            [
                [3,5,3,4], 5,
            ],
        ]
        for people, limit in testCases:
            res = self.numRescueBoats(people, limit)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

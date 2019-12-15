'''
Created on Apr 27, 2017

@author: MT
'''

class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        i = 0
        radius = 0
        for house in houses:
            while i+1 < len(heaters) and heaters[i+1] < house:
                i += 1
            if heaters[i] > house:
                tmp = heaters[i]-house
            else:
                tmp = house-heaters[i]
                if i+1 < len(heaters):
                    tmp = min(tmp, heaters[i+1]-house)
            radius = max(radius, tmp)
        return radius
    
    def test(self):
        testCases = [
            [
                [1, 2, 3],
                [2],
            ],
            [
                [1, 2, 3, 4],
                [1, 4],
            ],
        ]
        for houses, heaters in testCases:
            print('houses: %s' % houses)
            print('heaters: %s' % heaters)
            result = self.findRadius(houses, heaters)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

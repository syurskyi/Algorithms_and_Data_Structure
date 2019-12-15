'''
Created on Mar 7, 2018

@author: tongq
'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        while True:
            changed = False
            i = 0
            while i < len(asteroids):
                if i+1 <len(asteroids) and\
                    asteroids[i] > 0 and asteroids[i+1] < 0:
                    if asteroids[i] + asteroids[i+1] != 0:
                        val = asteroids[i] if asteroids[i]+asteroids[i+1] > 0\
                            else asteroids[i+1]
                        res.append(val) 
                    i += 1
                    changed = True
                else:
                    res.append(asteroids[i])
                i += 1
            if not changed:
                break
            asteroids = res
            res = []
        return res
    
    def test(self):
        testCases = [
            [5, 10, -5],
            [8, -8],
            [10, 2, -5],
            [-2, -1, 1, 2],
        ]
        for asteroids in testCases:
            print('asteroids: %s' % asteroids)
            result = self.asteroidCollision(asteroids)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

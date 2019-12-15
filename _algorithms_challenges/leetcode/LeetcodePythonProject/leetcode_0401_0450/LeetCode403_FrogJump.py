'''
Created on Apr 9, 2017

@author: MT
'''

class Solution(object):
    def canCross(self, stones):
        if not stones: return False
        hashmap = {}
        for stone in stones:
            hashmap[stone] = set()
        hashmap[0] = set([1])
        for stone in stones:
            for step in hashmap[stone]:
                reach = step+stone
                if reach == stones[-1]:
                    return True
                if reach in hashmap:
                    hashmap[reach].add(step)
                    if step > 1:
                        hashmap[reach].add(step-1)
                    hashmap[reach].add(step+1)
        return False
    
    def test(self):
        testCases = [
            [0,1,3,5,6,8,12,17], # True
            [0,1,2,3,4,8,9,11], # False
        ]
        for stones in testCases:
            print('stones: %s' % stones)
            result= self.canCross(stones)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Apr 14, 2018

@author: tongq
'''
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        maxVal = abs(target[0])+abs(target[1])
        for g in ghosts:
            d = abs(g[0]-target[0])+abs(g[1]-target[1])
            if d <= maxVal:
                return False
        return True
    
    def test(self):
        testCases = [
            
        ]
        for ghosts, target in testCases:
            result = self.escapeGhosts(ghosts, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        res = 0
        hashmap = {}
        for ans in answers:
            hashmap[ans] = hashmap.get(ans, 0)+1
        for n, count in hashmap.items():
            group = count//(n+1)
            if count%(n+1) != 0:
                res += (group+1)*(n+1)
            else:
                res += group*(n+1)
        return res
    
    def test(self):
        testCases = [
            [1, 1, 1, 1],
            [1, 1, 2],
            [10, 10, 10],
            [],
        ]
        for answers in testCases:
            print('answers: %s' % answers)
            result = self.numRabbits(answers)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

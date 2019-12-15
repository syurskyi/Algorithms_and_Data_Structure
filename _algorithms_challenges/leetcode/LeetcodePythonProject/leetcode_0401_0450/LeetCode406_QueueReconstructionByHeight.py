'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    def reconstructQueue(self, people):
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            res.insert(p[1], p)
        return res
        
    def test(self):
        testCases = [
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
        ]
        for people in testCases:
            print('people: %s' % people)
            result = self.reconstructQueue(people)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue1 = []
        queue2 = []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                queue1.append(i)
            else:
                queue2.append(i)
        while queue1 and queue2:
            r_index = queue1.pop(0)
            d_index = queue2.pop(0)
            if r_index < d_index:
                queue1.append(r_index+n)
            else:
                queue2.append(d_index+n)
        return 'Radiant' if len(queue1) > len(queue2) else 'Dire'
    
    def test(self):
        testCases = [
            'RD',
            'RDD',
            'DDRRR',
        ]
        for senate in testCases:
            print('senate: %s' % senate)
            result = self.predictPartyVictory(senate)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

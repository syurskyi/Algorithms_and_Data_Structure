'''
Created on Sep 5, 2017

@author: MT
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap1 = {}
        hashmap2 = {}
        for i, s in enumerate(list1):
            if s not in hashmap1:
                hashmap1[s] = i
        for i, s in enumerate(list2):
            if s not in hashmap2:
                hashmap2[s] = i
        minInd = float('inf')
        res = []
        for s, i in hashmap1.items():
            if s in hashmap2:
                ind = i+hashmap2[s]
                if ind == minInd:
                    res.append(s)
                elif ind < minInd:
                    minInd = ind
                    res = [s]
        return res
    
    def test(self):
        testCases = [
            [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
            ],
            [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            ],
        ]
        for list1, list2 in testCases:
            print('list1: %s' % list1)
            print('list2: %s' % list2)
            result = self.findRestaurant(list1, list2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

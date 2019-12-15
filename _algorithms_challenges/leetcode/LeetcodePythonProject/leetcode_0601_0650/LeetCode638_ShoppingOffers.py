'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.minPrice = sum([p*n for p, n in zip(price, needs)])
        self.helper(price, special, needs, 0)
        return self.minPrice
    
    def helper(self, price, special, needs, curPrice):
        n = len(price)
        added = False
        for arr in special:
            overflow = False
            for i in range(n):
                if needs[i] < arr[i]:
                    overflow = True
                needs[i] -= arr[i]
            if not overflow:
                added = True
                self.helper(price, special, needs, curPrice+arr[-1])
            for i in range(n):
                needs[i] += arr[i]
        if not added:
            for i in range(n):
                curPrice += needs[i]*price[i]
            self.minPrice = min(self.minPrice, curPrice)
    
    def test(self):
        testCases = [
            [
                [2,5],
                [[3,0,5],[1,2,10]],
                [3,2],
            ],
            [
                [2,3,4],
                [[1,1,0,4],[2,2,1,9]],
                [1,2,1],
            ],
            [
                [9,9],
                [[1,1,1]],
                [2,2],
            ],
            [
                [2,3],
                [[1,0,1],[0,1,2]],
                [1,1],
            ],
        ]
        for price, special, needs in testCases:
            print('price: %s' % price)
            print('special: %s' % special)
            print('needs: %s' % needs)
            result = self.shoppingOffers(price, special, needs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

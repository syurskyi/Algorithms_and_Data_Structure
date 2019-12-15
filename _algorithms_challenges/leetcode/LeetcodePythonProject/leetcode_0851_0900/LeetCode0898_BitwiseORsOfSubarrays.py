class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prevSet = set()
        uniqSet = set()
        for num in A:
            currSet = set()
            prevSet.add(0)
            for num1 in prevSet:
                currSet.add(num | num1)
                uniqSet.add(num | num1)
            prevSet = currSet
        return len(uniqSet)

    def test(self):
        testCases = [
            # [0],
            # [1, 1, 2],
            [1, 2, 4],
        ]
        for arr in testCases:
            res = self.subarrayBitwiseORs(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()

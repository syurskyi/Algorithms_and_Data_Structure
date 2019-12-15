class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left = 0
        res = 0
        hashmap = {}
        for i, num in enumerate(tree):
            hashmap[num] = hashmap.get(num, 0) + 1
            while len(hashmap) > 2:
                hashmap[tree[left]] -= 1
                if hashmap[tree[left]] == 0:
                    del hashmap[tree[left]]
                left += 1
            res = max(res, i-left+1)
        res = max(res, len(tree)-left)
        return res

    def test(self):
        testCases = [
            [0,1,2],
            [1,2,1],
            [0,1,2,2],
            [1,2,3,2,2],
            [3,3,3,1,2,1,1,2,3,3,4],
        ]
        for tree in testCases:
            res = self.totalFruit(tree)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()

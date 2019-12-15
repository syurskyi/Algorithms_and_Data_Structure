
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        nums = A
        n = len(nums)
        res = 0
        dp = [{} for _ in range(n)]
        for i in range(n):
            num1 = nums[i]
            for j in range(i):
                num2 = nums[j]
                diff = num2-num1
                c1 = dp[i].get(diff, 0)
                c2 = dp[j].get(diff, 0)
                res += c2
                dp[i][diff] = c1+c2+1
        return res
    
    def test(self):
        testCases = [
            [2, 4, 6, 8, 10],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

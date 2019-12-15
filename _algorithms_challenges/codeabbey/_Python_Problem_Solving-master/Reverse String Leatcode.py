class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        if x <= 0:
            ans = -1 * int(str(abs(x))[::-1])
        
        mini = -2**31
        maxi = 2**31 -1
        if ans not in range(mini,maxi):
            return 0
        else:
            return ans
        
        
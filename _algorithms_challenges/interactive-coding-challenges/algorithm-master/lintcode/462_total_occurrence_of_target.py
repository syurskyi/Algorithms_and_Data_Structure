class Solution:
    def totalOccurrence(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int

        given A == [a, b, b, b, c]
                       s     e

        using binary searching to find `s` and `e`
        ans is `e - s + 1`

        * s: start, e: end, l: left, r: right
             [a, b, b, b, c]
        r1    l  r,s
        r2           e,l  r
        """
        if not A:
            return 0

        n = len(A)

        left, mid, right = 0, 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        start = left if A[left] == target else right

        if A[start] != target:
            return 0

        left, mid, right = 0, 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        end = right if A[right] == target else left

        return end - start + 1

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        for i, num in enumerate(A):
            if i > 0:
                if num == A[i-1]:
                    continue
                if num > A[i-1]:
                    if increase is False:
                        return False
                    increase = True
                if num < A[i-1]:
                    if increase is True:
                        return False
                    increase = False
        return True

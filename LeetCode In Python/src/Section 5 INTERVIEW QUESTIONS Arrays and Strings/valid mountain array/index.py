from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A)<3):
            return False
        # initialize a loop index starting from 1
        i = 1
        # loop over array starting from loop index as long as it's increasing
        while(i<len(A) and A[i]>A[i-1]):
            i+=1
        # if loop index didn't move or reached array end, we return false
        if(i==1 or i==len(A)):
            return False

        # Loop over array starting from the loop index
        # as long as the array is decreasing
        while(i<len(A) and A[i]<A[i-1]):
            i+=1
        # if loop index is at end of the array, return true
        return i==len(A)

s = Solution()
answer = s.validMountainArray([1, 1, 2, 3, 1])
print(answer)
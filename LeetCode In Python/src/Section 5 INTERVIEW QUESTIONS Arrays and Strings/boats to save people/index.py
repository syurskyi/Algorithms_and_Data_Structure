from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people)-1

        boats_number = 0

        while(left<=right):
            if(left==right):
                boats_number+=1
                break
            if(people[left]+people[right]<=limit):
                left+=1

            right-=1
            boats_number+=1
        return boats_number


s = Solution()
# [2, 1, 3, 4], limit = 4
# [1, 2, 3, 4]

# [4]
# [1, 3]
# [2]
answer = s.numRescueBoats([2, 1, 3, 4], 4)
print(answer)
c_ Solution:
    ___ numRescueBoats people: List[int], limit: int) -> int:
        people.sort()

        left _ 0
        right _ len(people)-1

        boats_number _ 0

        _____(left<_right
            __(left==right
                boats_number+_1
                break
            __(people[left]+people[right]<_limit
                left+_1

            right-_1
            boats_number+_1
        r_ boats_number
c_ Solution:
    ___ getLeftPosition nums, target
        left _ 0
        right _ l..(nums)-1

        _____(left <_ right
            mid _ left+(right-left)//2
            __(nums[mid] __ target
                __(mid-1 >_ 0 and nums[mid-1] !_ target or mid __ 0
                    r_ mid
                right _ mid-1
            elif(nums[mid] > target
                right _ mid-1
            ____
                left _ mid+1

        r_ -1

    ___ getRightPosition nums, target
        left _ 0
        right _ l..(nums)-1

        _____(left <_ right
            mid _ left+(right-left)//2
            __(nums[mid] __ target
                __(mid+1 < l..(nums) and nums[mid+1] !_ target or mid __ l..(nums)-1
                    r_ mid
                left _ mid+1
            elif(nums[mid] > target
                right _ mid-1
            ____
                left _ mid+1

        r_ -1

    ___ searchRange nums: List[int], target: int) -> List[int]:
        left _ getLeftPosition(nums, target)
        right _ getRightPosition(nums, target)

        r_ [left, right]

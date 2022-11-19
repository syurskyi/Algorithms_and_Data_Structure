c_ Solution
    ___ getLeftPosition nums, target
        left _ 0
        right _ l..(nums)-1

        _____(left <_ right
            mid _ left+(right-left)//2
            __(nums[mid] __ target
                __(mid-1 >_ 0 ___ nums[mid-1] !_ target __ mid __ 0
                    r_ mid
                right _ mid-1
            ____(nums[mid] > target
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
                __(mid+1 < l..(nums) ___ nums[mid+1] !_ target __ mid __ l..(nums)-1
                    r_ mid
                left _ mid+1
            ____(nums[mid] > target
                right _ mid-1
            ____
                left _ mid+1

        r_ -1

    ___ searchRange nums: List[i..], target: i..) __ List[i..]:
        left _ getLeftPosition(nums, target)
        right _ getRightPosition(nums, target)

        r_ [left, right]

def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        # current element is 0
        if nums[j] < pivot:
            swap(nums, i, j)
            i = i + 1
            j = j + 1
        # current element is 2
        elif nums[j] > pivot:
            swap(nums, i, j)
            k = k - 1
        # current element is 1
        else:
            j = j + 1

    return nums


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]


if __name__ == '__main__':
    print(dutch_flag_problem([0, 1, 2, 2, 1, 0, 0, 2, 2, 1]))

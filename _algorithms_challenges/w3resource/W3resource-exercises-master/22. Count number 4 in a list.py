def count4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(count4([2, 3, 4, 2, 5, 4, 4, 4]))
print(count4([4, 4, 4, 4, 4, 2, 4, 2, 1]))
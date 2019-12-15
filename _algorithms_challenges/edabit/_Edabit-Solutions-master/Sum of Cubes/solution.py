def sum_of_cubes(nums):
    index = 0
    output = 0
    while index < len(nums):
      c = nums[index] ** 3
      output += c
      index += 1

    return output

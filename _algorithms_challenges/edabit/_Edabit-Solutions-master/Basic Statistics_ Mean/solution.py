def mean(nums):
    index = 1
    output = nums[0]
    while index < len(nums):
        output = output + nums[index]
        index += 1
    final_output = output / len(nums)
    return round(final_output,1)
    return final_output

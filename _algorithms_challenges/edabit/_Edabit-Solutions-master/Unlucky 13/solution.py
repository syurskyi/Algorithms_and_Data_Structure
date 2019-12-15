def unlucky_13(nums):
    output = []
    for i in nums:
        if i % 13 != 0:
            output.append(i)
    return output

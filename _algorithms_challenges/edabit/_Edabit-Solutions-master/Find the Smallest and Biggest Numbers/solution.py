def min_max(nums):
    nums.sort()
    return [nums[0],nums[-1]]


def test():
    print("test has started")
    a_list = [14, 35, 6, 1, 34, 54]
    if min_max(a_list) != [1,54]:
        print("error1")
    b_list = [1.346, 1.6532, 1.8734, 1.8723]
    if min_max(b_list) != [1.346, 1.8734]:
        print("error2")

# #
# # def findSmallestNum(lst):
# #     lst[sorted(lst)]
# # rrrr = [1, 3, 5, 1, 100, 14,]
# # sorted(rrrr)
# #
# # print(sorted(rrrr))
#
# def noOdds(lst):
#     lst1 = []
#     for number in lst:
#         if number % 2 == 0:
#             lst1.append(number)
#     return lst1
#
#
# def minMax(nums):
#     nums1 = sorted(nums)
#     nums2 = []
#     nums2.append(nums1[0])
#     nums2.append(nums1[len(nums1) - 1])
#     return nums2
#
#
# lst1 = [1, 4, 5, 10, 110, 15]
# # print(minMax(lst1))
# import calendar
#
#
# def month_name(num):
#     return calendar.month_name[num]
#
#
# print(month_name(3))
#
#
# def repeat(item, times):
#     lst = []
#     for i in range(times):
#         lst.append(item)
#     return lst
# print(repeat(2, 4))
# import math
#
#
# def my_pi(n):
#     return round(math.pi, 4)
#
#
# print(my_pi(3))

def MultiplyByLength(arr):
    mltp = len(arr)
    arr_mltp = []
    for i in arr:
        arr_mltp.append(i * mltp)
    return arr_mltp




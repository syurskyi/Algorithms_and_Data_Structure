# def check_ending(str1, str2):
#     symblols_to_check = len(str2)
#     if str1[-symblols_to_check:] == str2:
#         return True
#     else:
#         return False

#
# def findLargestNums(lst):
#     list_of_max = []
#     for i in lst:
#         sorted_lst = sorted(i)
#         list_of_max.append(sorted_lst[-1])
#     return list_of_max
#
#
# def reverse(txt):
#     if len(txt) == 2:
#         return txt[-1] + txt[0]
#
#     if len(txt) == 1:
#         return txt[0]
#
#     return txt[-1] + reverse(txt[1:len(txt) - 1]) + txt[0]
#
#
# print(reverse('aaafff'))

# def add_up(num):
#     summ_up = 0
#     for number in range(num + 1):
#         summ_up = summ_up + number
#     return summ_up
#
#
# print(add_up(600))

import math

#
# def get_abs_sum(lst):
#     summm = 0
#     for i in lst:
#         summm = summm + abs(i)
#     return summm
#
#
# print(get_abs_sum([-1, -3, -5, -4, -10, 0]))


# def calculate_exponent(num, exp):
#     return int(math.pow(num, exp))
# # print(calculate_exponent(3, 3))
# def XO(txt):
#     x_count = 0
#     o_count = 0
#     for letter in txt:
#         if letter.lower() == 'x':
#             x_count += 1
#         if letter.lower() == 'o':
#             o_count += 1
#     if x_count == o_count:
#         return True
#     else:
#         return False
#
# print(XO('ooxXm'))
#
# def double_char(txt):
# #     doubled_txt = ''
# #     for char in txt:
# #         doubled_txt += char
# #         doubled_txt += char
# #     return doubled_txt
# # print(double_char('string'))
# def count_vowels(txt):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowels_count = 0
#     for i in txt:
#         if i in str(vowels):
#             vowels_count = vowels_count + 1
#     return vowels_count
# print(count_vowels('Celebration'))

# print(ord('a'))

# def alphabet_soup(txt):
#     txt_ordered_list =  sorted(txt)
#     txt_ordered = ''
#     for letter in txt_ordered_list:
#         txt_ordered = txt_ordered + letter
#     return txt_ordered
#
#
# print(alphabet_soup('django'))


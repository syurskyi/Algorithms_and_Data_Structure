# def findLargestNum(nums):
#     largest_num = 0
#     for number in nums:
#         if largest_num < number:
#             largest_num = number
#     return largest_num
#
#
# # nums = [2, 15, 6]
# # print(findLargestNum(nums))
#
#
# def addition(num):
#     return num + 1
#
#
# def lessThanOrEqualToZero(num):
#     if num <= 0:
#         return True
#     else:
#         return False
#
#
# def comp(txt1, txt2):
#     if len(txt1) == len(txt2):
#         return True
#     else:
#         return False
#
#
# def num_to_dashes(num):
#     str = ''
#     i = 0
#     while True:
#         str = str + '-'
#         i = i + 1
#         if i == num:
#             break
#     return str
#
#
# print(num_to_dashes(5))
#
#
# def findSmallestNum(lst):
#     smallest = lst[0]
#     for i in lst:
#         if i <= smallest:
#             smallest = i
#     return smallest
#
# print(findSmallestNum([34, 15, 88, 2]))
#
#
# def isEvenOrOdd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
#
# print(isEvenOrOdd(14))
#
#
# def char_count(txt1, txt2):
#     ch_count = 0
#     for char in txt2:
#         if char == txt1:
#             ch_count = ch_count + 1
#     return ch_count
# print(char_count('a', 'dfgaadafagawrtagadfaaa'))


# def count_words(txt):
#     lst = txt.split(' ')
#     return len(lst)
#
#
# print(count_words("This is a test"))

#
# def find_index(lst, txt):
#     return lst.index(txt)
#
# print(len(["hi", "edabit", "fgh", "abc"]))

# def minMaxLengthAverage(lst):
#     answer = []
#     answer.append(max(lst))
#     answer.append(min(lst))
#     answer.append(len(lst))
#     answer.append(float(sum(lst) / len(lst)))
#     return answer
#
# #
# # print(minMaxLengthAverage([92, -2, 6, 21.833333333333332]))
#
# def mean(lst):
#     return round(sum(lst) / len(lst), 2)
#
# print(sorted([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3] ))


# def find_digit_amount(num):
# # # 	return len(str(num))
# # #
# # # print(find_digit_amount(3454524524))


# def is_valid_PIN(pin):
#     correct_length = bool
#     isdigit = bool
#     if len(pin) == 4 or len(pin) == 6:
#         correct_length = True
#         pass
#
#     else:
#         correct_length = False
#
#     for char in sorted(pin):
#         if str(char).isdigit():
#             isdigit = True
#         else:
#             isdigit = False
#             break
#     return correct_length and isdigit
#
#
# print(is_valid_PIN('12345'))
# print(is_valid_PIN('a2345'))
# print(is_valid_PIN('1234'))
# print(is_valid_PIN('@234'))

# def reverse(arg):
#     if not isinstance(arg, bool):
#         return 'boolean expected'
#     elif arg == False:
#         return True
#     elif arg == True:
#         return False
#
#
#
# print(reverse(1))
import numpy


def is_avg_whole(arr):
    if numpy.mean(arr).is_integer():
        return True
    else:
        return False


print(is_avg_whole([3, 5, 9]))
print(is_avg_whole([1, 1, 1, 1]))
print(is_avg_whole([4, 1, 7, 9, 2, 5, 7, 2, 4]))
print(is_avg_whole([1, 2, 3, 4, 5]))


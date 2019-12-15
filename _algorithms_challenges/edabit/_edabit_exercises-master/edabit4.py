# def unique_sort(lst):
#     return set(sorted(lst))
#
# print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
# print(unique_sort([1, 2, 3, 4, 5, 8, 10]))
# print(unique_sort([6, 7, 3, 2, 1]))

def is_isogram(txt):
    uniq_str = list(set(txt.lower()))
    if len(txt) == len(uniq_str):
        return True
    else:
        return False

    # listed_txt = list(txt)
    # for char in listed_txt:
    #     count = list(txt).count(char)
    #     if count > 1:
    #         is_isogram = False
    #         print('dfgdfgdfgdgf')
    #         break
    #     else:
    #         return True
    # return is_isogram

print(list(set('Consecutive')))
print(is_isogram('Consecutive'.lower()))

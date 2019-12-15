# def sharedLetters(a, b):
#     a_sorted = sorted(a)
#     b_sorted = sorted(b)
#     b_sorted_lower = []
#     for i in b_sorted:
#         b_sorted_lower.append(str(i).lower())
#     shared = ''
#     for letter in a_sorted:
#         if str(letter).lower() in b_sorted_lower and letter not in shared:
#             shared = shared + str(letter).lower()
#     return shared
#
#
# print(sharedLetters('Aa', 'aA'))
# print(sharedLetters('Javascript', 'Swift'))
# print(sharedLetters('house', 'home'))
# print(sharedLetters('Edabit', 'Matt'))
# print(sharedLetters('Micky', 'mouse'))

# def find_even_nums(num):
#     even_arr = []
#     for number in range(num + 1):
#         if number % 2 == 0 and number != 0:
#             even_arr.append(number)
#     return even_arr
#
#
# print(find_even_nums(8))
#
# def unique(lst):
#     for i in lst:
#         if lst.count(i) == 1:
#             return i
#         else:
#             continue
#
#
# print(unique([8, 8, 8, 8, 8, 8, 8, 0.5]))

# def all_about_strings(txt):
#     arr_answer = []
#     arr_answer.append(len(txt))
#     arr_answer.append(txt[0])
#     arr_answer.append(txt[-1])
#     if len(txt) % 2 != 0:
#         index_of_middle_element = int((len(txt) - 1) / 2)
#         arr_answer.append(txt[index_of_middle_element])
#     else:
#         index_of_middle_element = int(len(txt) / 2)
#         two_symbols_if_even = txt[index_of_middle_element - 1] + txt[index_of_middle_element]
#         arr_answer.append(two_symbols_if_even)
#     second_char = txt[1]
#     txt_list = list(txt)
#     del txt_list[1]
#     if txt.index(second_char):
#         try:
#             arr_answer.append('@ index ' + str(1 + txt_list.index(second_char)))
#         except ValueError:
#             arr_answer.append('not found')
#     return arr_answer
#
#
# print(all_about_strings('LASA'))
# print(all_about_strings('Computer'))
# # print(all_about_strings('Science'))
# def name_shuffle(txt):
#     txt_split =  txt.split(" ")
#     reversed_str = txt_split[1] + " " + txt_split[0]
#     return reversed_str
# print(name_shuffle("Donald Trump"))

# def sort_by_length(lst):
#     def sortByLength(inputStr):
#         return len(inputStr)
#
#     newList = sorted(lst, key=sortByLength)
#     return newList
#
#
# print(sort_by_length(["Google", "Apple", "Microsoft"]))

# def filter_list(lst):
#     lst_without_str = []
#     for i in lst:
#         if isinstance(i, int):
#             lst_without_str.append(i)
#     return lst_without_str
#
#
# print(filter_list([1, 2, "a", "b"]))

#
# def cap_me(lst):
#     cap_list = []
#     for word in lst:
#         cap_list.append(word[0].upper()+ word[1:].lower())
#     return cap_list
#
#
# print(cap_me(["mavis", "senaida", "letty"]))
# print(cap_me(["samuel", "MABELLE", "letitia", "meridith"]))



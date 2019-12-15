def is_anagram(s1, s2):
    result = set(s1.lower()) - set(s2.lower())
    if len(result) == 0 and len(s1) == len(s2):
        return True
    else:
        return False


# 3 решение, тоже не то
#     str1_list = list(s1)
#     str1_list.sort()
#     str2_list = list(s2)
#     str2_list.sort()
#ave Barry', 'Ray Adv
#     return str1_list == str2_list

##Тестовые строки
print(is_anagram('cristian', 'Cristina'))
print(is_anagram('Dave Barry', 'Ray Adverb'))
print(is_anagram('Nope', 'Note'))
print(is_anagram('Apple', 'Appeal'))
print("", is_anagram())

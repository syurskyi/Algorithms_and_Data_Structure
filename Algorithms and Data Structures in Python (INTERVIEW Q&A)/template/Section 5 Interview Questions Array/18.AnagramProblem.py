#
# ? ? is_anagram str1, str2
#
#     # if the length of the strings differ - they are not anagrams
#     __ l.. ? !_ l.. ?
#         r_ F..
#
#     # we have to sort the letters of the strings and then we haev to compare
#     # the letters with the same indexes
#     # this is the bottlenect because it has O(NlogN)
#     str1 _ s.. ?
#     str2 _ s.. ?
#
#     # after that we have to check the letters with the same indexes
#     # O(N) running time
#     ___ i __ r..(l.. ?
#         __ ? ? !_ ? ?
#             r_ F..
#
#     # overall running time is O(NlogN)+O(N)=O(NlogN)
#
#     r_ T..
#
#
# __ _____ __ ____
#
#     s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
#     s2 = ['r', 'e', 's', 't', 'f', 'e', 'l']
#
#     print(?(s1, s2))

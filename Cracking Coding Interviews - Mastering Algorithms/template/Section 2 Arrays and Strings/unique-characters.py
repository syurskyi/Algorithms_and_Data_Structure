# # Implement an algorithm to determine if a string has all unique characters.
#
# # "abc" -> True
# # "" -> True
# # "aabc" -> False
#
# # Brute Force - O(n^2)
# # Sorting - O(nlogn + n) -> O(nlogn)
# # Hashset - O(n)
#
# ___ unique_characters word
# 	visited_chars _ s..
#
# 	___ i __ r.. l.. ?
# 		letter _ ? ?
#
# 		__ ? __ ?
# 			r_ F..
#
# 		?.a.. ?
#
# 	r_ T..
#
# print(unique_characters("abc"))
# print(unique_characters(""))
# print(unique_characters("aabc"))

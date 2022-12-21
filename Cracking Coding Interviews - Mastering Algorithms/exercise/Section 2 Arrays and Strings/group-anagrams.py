# # Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# # Output:
# # [
# #   ["ate","eat","tea"],
# #   ["nat","tan"],
# #   ["bat"]
# # ]
#
# # O(n * mlogm)
#
# ___ group_anagrams strs
# 	dic _     # dict
#
# 	___ i __ r.. l.. ?
# 		sorted_anagram _ "".j.. s.. ? ?
# 		group_strs _ ?.g.. ?    # list)
# 		?.a.. ? ?
#
# 		? ? _ g..
#
# 	r_ l.. ?.v..
#
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
#
# # O(n*m)
# # Prime factorizations for each letter

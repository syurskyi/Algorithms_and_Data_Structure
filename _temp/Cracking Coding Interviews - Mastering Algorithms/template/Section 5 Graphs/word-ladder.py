# # Example 1:
#
# # Input:
# # beginWord = "hit",
# # endWord = "cog",
# # wordList = ["hot","dot","dog","lot","log","cog"]
#
# # Output: 5
#
# # Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# # return its length 5.
#
#
# # Example 2:
#
# # Input:
# # beginWord = "hit"
# # endWord = "cog"
# # wordList = ["hot","dot","dog","lot","log"]
#
# # Output: 0
#
# # Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
# ____ string ______ ascii_lowercase
# ______ copy
#
# c_ Node
# 	___ -  word, path
# 		? _ ?
# 		? _ ?
#
# ___ ladder begin, end, word_list
# 	queue _    # list
#
# 	words _ s.. ?
#
# 	?.a..(?(? b..
#
# 	_____ l.. ? > 0
# 		cur _ ?.p.. 0
#
# 		cur_word _ ?.w..
# 		path _ ?.p..
#
# 		__ ? __ end
# 			r_ ?
#
# 		___ i __ r..(l.. ?
# 			___ c __ a..
# 				potential_word _ ? |? + ? + c.. ?+1|
#
# 				__ ? __ w..
# 					copy_path _ c__.d.. ?
# 					?.a.. ?
# 					?.a.. ? ? ?
# 					w__.r.. ?
#
# 	r_    # list
#
# print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))


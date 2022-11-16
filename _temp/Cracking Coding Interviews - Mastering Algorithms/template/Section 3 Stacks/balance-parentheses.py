# # Given a string containing just the characters
# # '(', ')',
# # '{', '}',
# # '[' and ']',
# # determine if the input string is valid
#
# # Example 1:
# # Input: "()"
# # Output: true
#
# # Example 2:
# # Input: "()[]{}"
# # Output: true
#
# # Example 3:
# # Input: "(]"
# # Output: false
#
# # Example 4:
# # Input: "([)]"
# # Output: false
#
# # Example 5:
# # Input: "{[]}"
# # Output: true
#
# ___ balanced s
# 	stack _    # list
#
# 	___ i __ r.. l.. ?
# 		__ ? ? __ "(" __ ? ? __ "{" __ ? ? __ "[":
# 			?.a.. ? ?
# 		____ ? ? __ ")" ___ l..? __ 0 __ ?.p..  !_ "("
# 			r_ F..
# 		____ ? ? __ "]" ___ l..? __ 0 __ ?.p..  !_ "["
# 			r_ F..
# 		____ ? ? __ "}" ___ l..? __ 0 __ ?.p..  !_ "{"
# 			r_ F..
#
# 	r_ l..? __ 0
#
#
#
# print(balanced("()"))
# print(balanced("()[]{}"))
# print(balanced("(]"))
# print(balanced("([)]"))
# print(balanced("{[]}"))

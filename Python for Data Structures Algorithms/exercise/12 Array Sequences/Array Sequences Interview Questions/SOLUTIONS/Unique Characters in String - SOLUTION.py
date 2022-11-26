# # Unique Characters in String
# # Problem
# #
# # Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all
# # unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
# # Solution
# #
# # We'll show two possible solutions, one using a built-in data structure and a built in function, and another using
# # a built-in data structure but using a look-up method to check if the characters are unique
#
# ___ uni_char s
#     r_ l.. s.. ? __ l.. ?
#
# ___ uni_char2 s
#     chars _ s..
#     ___ let __ ?
#         # Check if in set
#         __ ? __ ?
#             r_ F..
#         ____
#             #Add it to the set
#             ?.a.. ?
#     r_ T..
#
# # Test Your Solution
# """
# RUN THIS CELL TO TEST YOUR CODE>
# """
# ____ n___.t.. ______ a..
#
#
# c_ TestUnique o..
#
#     ___ test sol
#         ? ? ''), T..)
#         ? ? 'goo'), F..)
#         ? ? 'abcdefg'), T..)
#         print('ALL TEST CASES PASSED')
#
#
# # Run Tests
# t _ TestUnique()
# t.test(uni_char)
#

# # Sentence Reversal
# # Problem
# # Given a string of words, reverse all the words. For example:
# # Given
# # 'This is the best'
# # Return:
# # 'best the is This'
# # As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# # '  space here'  and 'space here      '
# # both become:
# # 'here space'
# # Solution
# # We could take advantage of Python's abilities and solve the problem with the use of split() and some slicing or use
# # of reversed:
#
# ___ rev_word1 s
#     r_ " ".j.. r.. ?.s..
#
# #Or
#
# ___ rev_word2 s
#     r_ " ".j.. ?.s.. ||-1
#
# rev_word1('Hi John,   are you ready to go?')
# # 'go? to ready you are John, Hi'
#
# rev_word2('Hi John,   are you ready to go?')
# # 'go? to ready you are John, Hi'
#
# # While these are valid solutions, in an interview setting you'll have to work out the basic algorithm that is used.
# # In this case what we want to do is loop over the text and extract words form the string ourselves.
# # Then we can push the words to a "stack" and in the end opo them all to reverse. Let's see what this actually looks
# # like:
#
# ___ rev_word3 s
#     """
#     Manually doing the splits on the spaces.
#     """
#
#     words _    # list
#     length _ l.. ?
#     spaces _ [' ']
#
#     # Index Tracker
#     i _ 0
#
#     # While index is less than length of string
#     _____ ? < l..
#
#         # If element isn't a space
#         __ ? ? n.. __ s..
#
#             # The word starts at this index
#             word_start _ i
#
#             _____ ? < l.. ___ ? ? n.. __ s..
#                 # Get index where word ends
#                 ? +_ 1
#             # Append that word to the list
#             ?.a.. ?|??
#         # Add to index
#         ? +_ 1
#
#     # Join the reversed words
#     r_ " ".j.. r.. ?
#
# rev_word3('   Hello John    how are you   ')
# # 'you are how John Hello'
#
# rev_word3('    space before')
# # 'before space'
#
# # If you want you can further develop this solution so its all manual, you can create your own reversal function.
# # Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
#
# ____ n___.t.. ______ a..
#
#
# c_ ReversalTest o..
#
#     ___ test sol
#         ? ? '    space before'), 'before space')
#         ? ? 'space after     '), 'after space')
#         ? ? '   Hello John    how are you   '), 'you are how John Hello')
#         ? ? '1'), '1')
#         print("ALL TEST CASES PASSED")
#
#
# # Run and test
# t _ ReversalTest()
# t.test(rev_word3)
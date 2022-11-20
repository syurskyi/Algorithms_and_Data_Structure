# # %%
# '''
# # Anagram Solution
# ## Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact
# same letters (so you can just rearrange the letters to get a different phrase or word).
# For example:
#     "public relations" is an anagram of "crap built on lies."
#
#     "clint eastwood" is an anagram of "old west action"
# **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".*
# ## Solution
# There are two ways of thinking about this problem, if two strings have the same frequency of letters/element
# (meaning each letter shows up the same number of times in both strings) then they are anagrams of eachother.
# On a similar vien of logic, if two strings are equal to each other once they are sorted, then they are also anagrams
# of each other.
# You would be able to implement this second solution pretty easily in Python:
# '''
#
# # %%
# ___ anagram s1,s2
#
#     # Remove spaces and lowercase letters
#     s1 _ ?.r.. ' ','' .l..
#     s2 _ ?.r.. ' ','' .l..
#
#     # Return boolean for sorted match.
#     r_ s.. ? __ s.. ?
#
# # %%
# anagram('dog','god')
#
# # %%
# anagram('clint eastwood','old west action')
#
# # %%
# anagram('aa','bb')
#
# # %%
# '''
# Now the above sorting approach is simple, but is actually not optimal and in an interview setting you would probably
# be asked to implement a more manual solution involving just counting the number of letters in each string to test your
# ability to understand hash tables. Let's build out a fuller solution using counting and Python dictionaries:
# '''
#
# # %%
# ___ anagram2 s1,s2
#
#     # Remove spaces and lowercase letters
#     s1 _ ?.r.. ' ','' .l..
#     s2 _ ?.r.. ' ','' .l..
#
#     # Edge Case to check if same number of letters
#     __ l.. ? !_ l.. ?
#         r_ F..
#
#     # Create counting dictionary (Note could use DefaultDict from Collections module)
#     count _     # dict
#
#
#
#     # Fill dictionary for first string (add counts)
#     ___ letter __ ?
#         __ ? __ ?
#             ? ? +_ 1
#         ____
#             ? ? _ 1
#
#     # Fill dictionary for second string (subtract counts)
#     ___ l.. __ ?
#         __ ? __ ?
#             ? ? -_ 1
#         ____
#             ? ? _ 1
#
#     # Check that all counts are 0
#     ___ k __ c..
#         __ ? ? !_ 0
#             r_ F..
#
#     # Otherwise they're anagrams
#     r_ T..
#
# # %%
# anagram2('dog','god')
#
# # %%
# anagram2('clint eastwood','old west action')
#
# # %%
# anagram2('dd','aa')
#
# # %%
# '''
# A quick note on the second solution, the use of defaultdict form the collections module would clean up this code quite
# a bit, and the final for loop could be built into the second for loop, but in the above implementation every step is
# very clear.
# '''
#
# # %%
# '''
# # Test Your Solution
# Run the cell below to test your solution
# '''
#
# # %%
# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# ____ n___.t.. ______ a..
#
# c_ AnagramTest o..
#
#     ___ testsol
#         ? ? 'go go go','gggooo'),T..)
#         ? ? 'abc','cba'),T..)
#         ? ? 'hi man','hi     man'),T..)
#         ? ? 'aabbcc','aabbc'),F..)
#         ? ? '123','1 2'),F..)
#         print "ALL TEST CASES PASSED"
#
# # # Run Tests
# # t = AnagramTest()
# # t.test(anagram)
# #
# # # %%
# # t.test(anagram2)
# #
# # # %%
# # '''
# # # Good Job!
# # '''
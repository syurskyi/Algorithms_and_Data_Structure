# Recursion Homework Problems
# This assignment is a variety of small problems to begin you getting used to the idea of recursion.
# They are not full-blown interview questions, but do serve as a great start for getting your mind "in the zone"
# for recursion problems.
# Problem 1
# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
# For example, if n=4 , return 4+3+2+1+0, which is 10.
# This problem is very similar to the factorial problem presented during the introduction to recursion. Remember,
# always think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have
# also designed the cut off to be 1).
#
# In this case, we have: n + (n-1) + (n-2) + .... + 0

# Fill out a sample solution:

def rec_sum(n):

    pass

rec_sum(4)

# 10
#
# Problem 2
# Given an integer, create a function which returns the sum of all the individual digits in that integer.
# For example: if n = 4321, return 4+3+2+1
#
def sum_func(n):
    pass

sum_func(4321)
# 10
#
# Hints:
# # You'll neeed to use modulo
# 4321%10
# 1
# 4321 / 10
# 432
#
# We'll need to think of this function recursively by knowing that: 4502 % 10 + sum_func(4502/10)
# Problem 3
# Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and
# we're ignoring strict requirements here.
# Create a function called word_split() which takes in a string phrase and a set list_of_words.
# The function will then determine if it is possible to split the string in a way in which words can be made from
# the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely
# splittable.
#
# For example:
#
word_split('themanran',['the','ran','man'])
# ['the', 'man', 'ran']
#
word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
# ['i', 'love', 'dogs', 'John']
#
word_split('themanran',['clown','ran','man'])
# []
#
def word_split(phrase,list_of_words, output = None):
    pass

# Good Luck!
#
# Check out the Solutions Notebook once you're done!
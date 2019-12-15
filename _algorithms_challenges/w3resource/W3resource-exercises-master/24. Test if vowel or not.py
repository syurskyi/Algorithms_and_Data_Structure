"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

def is_vowel(char):
    all_vowels = "aeiouæøå"
    return char in all_vowels

print(is_vowel("c"))
print(is_vowel("a"))
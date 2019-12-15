""""
In this Bite we'd like you to loop over the characters in the large block of text (the most important text for any Python programmer: The Zen of Python!)

Within this loop you'll perform the following actions:

Replace all vowels (aeiou) with stars (*), do this case insensitively.
Count the number of replacements you do (= vowels in the text).
Return the new block of text post replacements and the count of vowels you replaced.
Hint: Try converting the block of text to a list first to make working with the characters simpler.

Tip: If you're struggling, work on one step at a time and expand on your code slowly. Don't try and tackle every requirement right away.

Bonus: if you already have some Python under your belt, try to use re and try to solve it without a for loop :)
"""

text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'

def strip_vowels(text=text):  
    number_of_replacement = 0
    for i in vowels:        
        number_of_replacement += int(text.count(i) + text.count(i.upper()))
        text = text.replace(i, "*", 1000)
        text = text.replace(i.upper(), "*", 1000)
    output = (str(text), number_of_replacement)
    return output
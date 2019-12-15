
"""
Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n) using split.

Loop through the lines and if the first character of each (stripped) line is lowercase, split the line into words and add the last word to the (given) results list, stripping the trailing dot (.) and exclamation mark (!) from the end of the word.

At the end of the function return the results list.
"""
text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text=text):
    results = []
    strip_text = text.strip("\n")
    split_strip = strip_text.split("\n")

    for i in split_strip:
        i = i.strip(" ")
        if i[0].islower():
            strip_i = i.strip('!.')
            split_i = strip_i.split(" ")
            results.append(split_i[-1])
    return results
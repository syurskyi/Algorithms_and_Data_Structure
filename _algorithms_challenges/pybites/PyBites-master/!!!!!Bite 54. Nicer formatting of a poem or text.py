from textwrap import *
import string
poem = """            Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand"""


INDENTS = 4


def print_hanging_indents(poem=poem):
    poem = poem.strip()
    wrapper = TextWrapper(subsequent_indent=' '*INDENTS)
    return wrapper.wrap(poem)


print_hanging_indents()



print('#'*155)

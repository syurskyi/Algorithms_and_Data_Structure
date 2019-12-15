from slicing import text, slice_and_dice

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def test_slice_and_dice_default_text():
    expected = ['objects', 'y', 'too', ':)', 'bites']
    assert slice_and_dice(text) == expected


def test_slice_and_dice_other_text():
    expected = ['word', 'list', 'list']
    assert slice_and_dice(another_text) == expected
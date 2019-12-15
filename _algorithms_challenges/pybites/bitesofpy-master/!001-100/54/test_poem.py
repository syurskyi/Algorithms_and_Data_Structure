from Previous.poem import print_hanging_indents

# part of William Shakespeare's play Hamlet
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""

# part of Remember, by Christina Rosetti
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""


def test_shakespeare_text(capfd):
    print_hanging_indents(shakespeare_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == shakespeare_formatted.strip()


def test_rosetti_poem(capfd):
    print_hanging_indents(rosetti_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == rosetti_formatted.strip()
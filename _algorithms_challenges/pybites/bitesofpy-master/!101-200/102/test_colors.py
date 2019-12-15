from unittest.mock import patch

from colors import print_colors

NOT_VALID = 'Not a valid color'


def call_print_colors():
    # some people prefer sys.exit instead of break
    try:
        print_colors()
    except SystemExit:
        pass


@patch("builtins.input", side_effect=['quit'])
def test_straight_quit(input_mock, capsys):
    # user only enter quit, program prints bye and breaks loop
    call_print_colors()
    actual = capsys.readouterr()[0].strip()
    expected = 'bye'
    assert actual == expected


@patch("builtins.input", side_effect=['blue', 'quit'])
def test_one_valid_color_then_quit(input_mock, capsys):
    # user enters blue = valid color so print it
    # then user enters quit so break out of loop = end program
    call_print_colors()
    actual = capsys.readouterr()[0].strip()
    expected = 'blue\nbye'
    assert actual == expected


@patch("builtins.input", side_effect=['green', 'quit'])
def test_one_invalid_color_then_quit(input_mock, capsys):
    # user enters green which is not in VALID_COLORS so continue the loop,
    # user then enters quit so loop breaks (end function / program)
    call_print_colors()
    actual = capsys.readouterr()[0].strip()
    expected = f'{NOT_VALID}\nbye'
    assert actual == expected


@patch("builtins.input", side_effect=['white', 'red', 'quit'])
def test_invalid_then_valid_color_then_quit(nput_mock, capsys):
    # white is not a valid color so continue the loop,
    # then user enters red which is valid so print it, then quit
    call_print_colors()
    actual = capsys.readouterr()[0].strip()
    expected = f'{NOT_VALID}\nred\nbye'
    assert actual == expected


@patch("builtins.input", side_effect=['yellow', 'orange', 'quit'])
def test_valid_then_invalid_color_then_quit(input_mock, capsys):
    # yellow is a valid color so print it, user then enters orange
    # which is not a valid color so continue loop, lastly user
    # enters quit so exit loop = reaching end function / program
    call_print_colors()
    actual = capsys.readouterr()[0].strip()
    expected = f'yellow\n{NOT_VALID}\nbye'
    assert actual == expected
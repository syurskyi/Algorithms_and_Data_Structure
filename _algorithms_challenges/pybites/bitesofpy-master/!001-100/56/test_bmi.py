import pytest

from Previous.bmi import create_parser, handle_args


@pytest.fixture
def parser():
    return create_parser()


def test_no_args_exits(parser):
    # parser.parse_args should raise the exception but in case
    # you raised it explicitly further down the stack let's check
    # if handle_args raises it (same applies to next test)
    with pytest.raises(SystemExit):
        handle_args()


def test_help_flag_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-h'])
        handle_args(args)


def test_only_width_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-w', '80'])
        handle_args(args)


def test_only_length_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-l', '187'])
        handle_args(args)


def test_two_arg(parser, capfd):
    args = parser.parse_args(['-w', '80', '-l', '187'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_two_arg_reversed_order(parser, capfd):
    args = parser.parse_args(['-l', '187', '-w', '80'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_different_args(parser, capfd):
    args = parser.parse_args(['-l', '200', '-w', '100'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 25.0" in output
import pytest

from calculator import create_parser, call_calculator


@pytest.fixture
def parser():
    return create_parser()


def test_one_arg_no_numbers_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--add'])
        call_calculator(args=args)


def test_call_with_wrong_operation(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--sum', '10'])
        call_calculator(args=args)


def test_help_text_hints(parser, capfd):
    with pytest.raises(SystemExit):
        parser.parse_args(['-h'])

    output = capfd.readouterr()[0].lower()
    assert 'usage' in output
    assert 'a simple calculator' in output
    for op in 'add sub mul div'.split():
        assert op in output


@pytest.mark.parametrize("args, expected", [
    (['1'], 1),
    (['1', '2'], 3),
    (['1', '2', '3'], 6),
    (['1', '2', '3', '4.5'], 10.5),
])
def test_add_operations(parser, args, expected):
    args = parser.parse_args(['--add'] + args)
    assert call_calculator(args) == expected


@pytest.mark.parametrize("args, expected", [
    (['1'], 1),
    (['1', '2'], -1),
    (['10', '7', '0.5'], 2.5),
    (['11', '9', '2.2', '1.8'], -2),
])
def test_sub_operations(parser, args, expected):
    args = parser.parse_args(['--sub'] + args)
    assert call_calculator(args) == expected


@pytest.mark.parametrize("args, expected", [
    (['1'], 1),
    (['1', '2'], 2),
    (['3.5', '2', '4.2'], 29.4),
    (['3.5', '2', '4.2', '-1'], -29.4),
])
def test_mul_operations(parser, args, expected):
    args = parser.parse_args(['--mul'] + args)
    assert call_calculator(args) == expected


@pytest.mark.parametrize("args, expected", [
    (['2'], 2),
    (['1', '0'], 0),
    (['2.2', '7', '1.1'], 0.29),
    (['3', '2', '3', '5'], 0.1),
])
def test_div_operations(parser, args, expected):
    args = parser.parse_args(['--div'] + args)
    assert call_calculator(args) == expected
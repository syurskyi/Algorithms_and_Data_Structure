import pytest

from tables import MultiplicationTable


@pytest.fixture
def t10():
    return MultiplicationTable(10)


@pytest.fixture
def t3():
    return MultiplicationTable(3)


@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (5, 25),
    (10, 100),
    (100, 10000),

])
def test_table_len(arg, ret):
    assert len(MultiplicationTable(arg)) == ret


@pytest.mark.parametrize("arg, ret", [
    ((6, 6), 36),
    ((4, 2), 8),
    ((7, 6), 42),
    ((8, 8), 64),
    ((10, 10), 100),
])
def test_calc(t10, arg, ret):
    assert t10.calc_cell(*arg) == ret


def test_calc_exception(t3, capfd):
    with pytest.raises(IndexError):
        t3.calc_cell(3, 4)
    with pytest.raises(IndexError):
        t3.calc_cell(4, 3)


def test_table_str(t3):
    output = str(t3)
    assert '1 | 2 | 3' in output
    assert '2 | 4 | 6' in output
    assert '3 | 6 | 9' in output
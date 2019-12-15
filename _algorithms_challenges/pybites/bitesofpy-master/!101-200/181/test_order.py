import inspect

import pytest

from order import OrderedList


@pytest.fixture(scope='module')
def order():
    return OrderedList()


@pytest.mark.parametrize("num, expected", [
    (10, '10'),
    (9, '9, 10'),
    (16, '9, 10, 16'),
    (2, '2, 9, 10, 16'),
    (7, '2, 7, 9, 10, 16'),
    (1, '1, 2, 7, 9, 10, 16'),
    (5, '1, 2, 5, 7, 9, 10, 16'),
])
def test_order(order, num, expected):
    order.add(num)
    assert str(order) == expected


def test_does_not_use_manual_sort():
    assert '.sorted' not in inspect.getsource(OrderedList)
    assert '.sort(' not in inspect.getsource(OrderedList)
from decimal import Decimal

import pytest

from intlist import IntList


@pytest.fixture()
def list1():
    return IntList([1, 3, 5])


@pytest.fixture()
def list2():
    return IntList([2, 3, 4, 5, 7])


def test_mean_median_start_first_instance(list1):
    assert list1.mean == 3
    assert list1.median == 3


def test_append_and_new_stats_first_instance(list1):
    list1.append(7)
    assert list1.mean == 4
    assert list1.median == 4


def test_mean_median_start_second_instance(list2):
    assert list2.mean == 4.2
    assert list2.median == 4


def test_append_and_new_stats_second_instance(list2):
    list2.append(9.0)  # float ok too
    list2.append(Decimal(11))  # decimal ok too
    assert round(list2.mean, 2) == 5.86
    assert list2.median == 5


@pytest.mark.parametrize("arg", ['a', ['a'], {'a': 1}])
def test_cannot_append_non_int_values(list1, list2, arg):
    for instance in (list1, list2):
        with pytest.raises(TypeError):
            instance.append(arg)


def test_cannot_append_non_int_values_via_overloading(list1):
    with pytest.raises(TypeError):
        list1 + ['a']


def test_cannot_append_non_int_values_via_inplace_overloading(list2):
    with pytest.raises(TypeError):
        list2 += ['a']


def test_can_append_list_of_ints(list1):
    try:
        list1 += [1, 2, 3]
    except Exception as exc:
        pytest.fail(exc)
    assert list1 == [1, 3, 5, 1, 2, 3]
from dataclasses import astuple, replace

import pytest

from dc import Bite


@pytest.fixture()
def bites():
    b1 = Bite(number=1, title="sum of numbers")
    b2 = Bite(number=2, title="a second bite", level="Intermediate")
    b3 = Bite(number=3, title="a hard bite", level="Advanced")
    bites = [b1, b2, b3]
    return bites


def test_type_annotations():
    assert Bite.__annotations__ == {'number': int, 'title': str, 'level': str}


def test_getting_str_for_free(bites):
    expected = Bite(number=1, title='Sum of numbers', level='Beginner')
    assert bites[0] == expected


def test_default_level_arg_first_bite(bites):
    assert bites[0].level == 'Beginner'


def test_attribute_access_second_bite(bites):
    assert bites[1].number == 2
    # title should get capitalized (use the __post_init__ method)
    assert bites[1].title == 'A second bite'
    assert bites[1].level == 'Intermediate'


def test_my_data_class_is_mutable(bites):
    b3 = bites[-1]
    assert b3.level == 'Advanced'
    # named tuples are immutable so would not allow this:
    b3 = replace(b3, level='super hard')
    assert b3.level == 'super hard'


def test_can_order_bites(bites):
    # not out of the box, need to set something on the data class ...
    sorted_bites = sorted(bites, reverse=True)
    assert sorted_bites[0].number == 3
    assert sorted_bites[-1].number == 1


def test_data_class_are_not_hashable(bites):
    # this would work if namedtuples, but Bites are data classes here
    with pytest.raises(TypeError):
        set(bites)


def test_data_class_can_only_be_unpacked_when_casted_to_tuple(bites):
    with pytest.raises(TypeError):
        number, title, level = bites[0]
    # but this works:
    number, title, level = astuple(bites[0])
    assert number == 1
    assert level == 'Beginner'
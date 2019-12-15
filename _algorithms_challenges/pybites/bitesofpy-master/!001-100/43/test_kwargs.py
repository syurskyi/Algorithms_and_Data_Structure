import pytest

from Previous.kwargs import get_profile


def test_no_arguments():
    assert get_profile() == 'julian is a programmer'


def test_one_positional_arg():
    with pytest.raises(TypeError):
        get_profile('julian')


def test_wrong_single_kw():
    with pytest.raises(TypeError):
        get_profile(test=True)


def test_wrong_additional_kw():
    with pytest.raises(TypeError):
        get_profile(name='bob', profession='software developer',
                    another_flag=False)


def test_correct_kw_second_default():
    assert get_profile(name='bob') == 'bob is a programmer'


def test_two_correct_kws():
    ret = get_profile(name='bob', profession='software developer')
    assert ret == 'bob is a software developer'
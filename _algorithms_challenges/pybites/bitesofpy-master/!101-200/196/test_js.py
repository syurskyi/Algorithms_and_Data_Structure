import pytest

from js import JsObject as JS


@pytest.fixture
def D():
    """Create a JsObject object"""
    return JS(a=1, b=2, c=3)


def test_object_type(D):
    assert type(D) == JS


def test_assert_regular_dict_behavior(D):
    assert D['a'] == 1
    assert D['b'] == 2
    assert D['c'] == 3
    D['d'] = 4
    assert len(D) == 4
    del D['b']
    assert 'b' not in D
    assert len(D) == 3
    assert list(D.keys()) == ['a', 'c', 'd']
    assert list(D.values()) == [1, 3, 4]


def test_assert_js_behavior(D):
    assert D.a == 1
    assert D.b == 2
    assert D.c == 3
    D.d = 4
    assert len(D) == 4
    del D.b
    D.update(dict(e=5))
    assert D.e == 5


def test_supports_nesting(D):
    D.d = JS(e=5)
    assert D.d.e == 5
    D.d.e = JS(f=6)
    assert D.d.e.f == 6
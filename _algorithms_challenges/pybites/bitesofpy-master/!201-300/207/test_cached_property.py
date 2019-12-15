from time import perf_counter
import pytest

from Previous.cached_property import Planet


@pytest.fixture(scope="module")
def blue():
    return Planet('blue')


def test_property_is_cached_timing(blue):
    start_time = perf_counter()
    for _ in range(5):
        blue.mass
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    assert elapsed_time < .5


def test_property_is_cached_value(blue):
    masses = [blue.mass for _ in range(10)]
    initial_mass = masses[0]
    assert all(m == initial_mass for m in masses)


def test_property_is_immutable(blue):
    with pytest.raises(AttributeError):
        blue.mass = 11
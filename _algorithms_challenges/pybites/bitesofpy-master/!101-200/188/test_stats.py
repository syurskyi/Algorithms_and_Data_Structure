import pytest

from stats import get_all_line_counts, create_stats_report

EXPECTED_OUTPUT = """
Basic statistics:
- count     :     186
- min       :       6
- max       :     337
- mean      :   43.74

Population variance:
- pstdev    :   43.04
- pvariance : 1852.39

Estimated variance for sample:
- count     :   93.00
- stdev     :   30.24
- variance  :  914.36
"""


@pytest.fixture
def report():
    return create_stats_report()


def test_get_all_line_counts():
    counts = list(get_all_line_counts())
    # total number of test files / bites
    assert len(counts) == 186
    # all elements should be ints
    assert all(isinstance(c, int) for c in counts)
    # total lines of test code written
    assert sum(counts) == 8135


@pytest.mark.parametrize("line", EXPECTED_OUTPUT.strip().splitlines())
def test_create_stats_report(report, line):
    assert line in report
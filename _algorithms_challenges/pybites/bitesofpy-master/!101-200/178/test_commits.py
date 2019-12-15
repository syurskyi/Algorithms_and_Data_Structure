import pytest

from Previous.commits import get_min_max_amount_of_commits


@pytest.mark.parametrize('year, expected', [
    (None, ('2018-02', '2017-01')),  # parse the whole file
    (2017, ('2017-11', '2017-01')),
    (2018, ('2018-02', '2018-10')),
    (2019, ('2019-01', '2019-03')),
])
def test_get_min_max_amount_of_commits(year, expected):
    actual = get_min_max_amount_of_commits(year=year)
    assert actual == expected
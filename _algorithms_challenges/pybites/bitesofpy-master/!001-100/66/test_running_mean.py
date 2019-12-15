import pytest

from Previous.running_mean import running_mean


@pytest.mark.parametrize("input_argument, expected_return", [
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 6, 10, 8, 11, 10],
     [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]),
    ([3, 4, 6, 2, 1, 9, 0, 7, 5, 8],
     [3.0, 3.5, 4.33, 3.75, 3.2, 4.17, 3.57, 4.0, 4.11, 4.5]),
    ([], []),
])
def test_running_mean(input_argument, expected_return):
    ret = list(running_mean(input_argument))
    assert ret == expected_return
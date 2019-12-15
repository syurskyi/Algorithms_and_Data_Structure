import pytest

from validate import (get_secret_token, SECRET,
                      UserDoesNotExist, UserAccessExpired, UserNoPermission)


def test_get_secret_token():
    assert issubclass(UserDoesNotExist, Exception)
    assert issubclass(UserAccessExpired, Exception)
    assert issubclass(UserNoPermission, Exception)

    with pytest.raises(UserDoesNotExist):
        get_secret_token('Tim')
    with pytest.raises(UserAccessExpired):
        get_secret_token('Bob')
    with pytest.raises(UserNoPermission):
        get_secret_token('Julian')

    assert get_secret_token('PyBites') == SECRET
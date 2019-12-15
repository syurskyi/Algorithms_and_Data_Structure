from Previous.login import welcome


def test_no_account():
    """User is not on the system"""
    assert welcome('anonymous') == 'please create an account'


def test_not_loggedin():
    """User is on the system but not logged in"""
    assert welcome('julian') == 'please login'


def test_loggedin():
    """User is on the system and logged in"""
    assert welcome('sue') == 'welcome back sue'


def test_docstring():
    """Decorator should not lose function's docstring"""
    assert welcome.__doc__ == 'Return a welcome message if logged in'
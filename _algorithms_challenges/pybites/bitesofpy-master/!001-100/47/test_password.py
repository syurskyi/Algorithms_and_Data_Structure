from password import validate_password, used_passwords


def test_password_len():
    assert not validate_password('short')
    assert not validate_password('waytoolongpassword')


def test_password_missing_chars():
    assert not validate_password('UPPERCASE')
    assert not validate_password('lowercase')
    assert not validate_password('PW_no_digits')
    assert not validate_password('Pw9NoPunc')
    assert not validate_password('_password_')
    assert not validate_password('@#$$)==1')


def test_password_only_one_letter():
    assert not validate_password('@#$$)==1a')


def test_validate_password_good_pws():
    assert validate_password('passWord9_')
    assert validate_password('another>4Y')
    assert validate_password('PyBites@1912')
    assert validate_password('We<3Python')


def test_password_not_used_before():
    assert not validate_password('PassWord@1')
    assert not validate_password('PyBit$s9')


def test_password_cache_cannot_reuse():
    num_passwords_use = len(used_passwords)
    assert validate_password('go1@PW')
    assert len(used_passwords) == num_passwords_use + 1
    assert not validate_password('go1@PW')
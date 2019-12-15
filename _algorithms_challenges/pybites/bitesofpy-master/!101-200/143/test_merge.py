from merge import get_person_age, NOT_FOUND


def test_regular_name():
    assert get_person_age('tim') == 30
    assert get_person_age('helen') == 26
    assert get_person_age('otto') == 44


def test_case_insensitive_lookup():
    assert get_person_age('Tim') == 30
    assert get_person_age('BOB') == 17
    assert get_person_age('BrEnDa') == 17


def test_name_not_found():
    assert get_person_age('timothy') == NOT_FOUND
    assert get_person_age(None) == NOT_FOUND
    assert get_person_age(False) == NOT_FOUND
    assert get_person_age(-1) == NOT_FOUND


def test_duplicate_name():
    assert get_person_age('thomas') == 46
    assert get_person_age('ana') == 26
import pytest
from bt import check_bt, Bloodtype


def test_universal_donor():
    donor = Bloodtype.ZERO_NEG
    for i in range(8):
        recipient = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_universal_recipient():
    recipient = Bloodtype.AB_POS
    for i in range(8):
        donor = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_AB_POS_can_donate_to_own_group_only_numeric_input():
    donor = 7
    for i in range(7):
        recipient = i
        assert check_bt(donor, recipient) is False


def test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input():
    recipient = 0
    for i in range(1, 8):
        donor = i
        assert check_bt(donor, recipient) is False


def test_red_blood_cell_compatibility():
    assert check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    assert check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    assert check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


def test_red_blood_cell_incompatibility():
    assert check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) is False
    assert check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) is False


def test_red_blood_cell_compatibility_text_input():
    assert check_bt("0+", "A+")
    assert check_bt("0+", "B+")
    assert check_bt("B-", "B+")
    assert check_bt("A-", "AB-")


def test_red_blood_cell_incompatibility_text_input():
    assert check_bt("0+", "A-") is False
    assert check_bt("0+", "B-") is False
    assert check_bt("B-", "0-") is False
    assert check_bt("AB-", "A+") is False


def test_invalid_value_text_input():
    with pytest.raises(ValueError):
        check_bt("X-", "Y+")
    with pytest.raises(ValueError):
        check_bt("0", "A+")


def test_invalid_value_numeric_input():
    with pytest.raises(ValueError):
        check_bt(8, 1)
    with pytest.raises(ValueError):
        check_bt(3, -1)


def test_invalid_type():
    with pytest.raises(TypeError):
        check_bt(1.0, 1)
    with pytest.raises(TypeError):
        check_bt(3, ["AB", "Rh+"])
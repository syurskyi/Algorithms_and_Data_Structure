from user import User


def test_bob_lowercase():
    bob = User('bob', 'belderbos')
    assert bob.get_full_name == 'Bob Belderbos'
    assert bob.username == 'bbelderb'  # lowercase!
    assert str(bob) == 'Bob Belderbos (bbelderb)'
    assert repr(bob) == 'User("bob", "belderbos")'


def test_julian_mixed_case():
    bob = User('julian', 'Sequeira')
    assert bob.get_full_name == 'Julian Sequeira'
    assert bob.username == 'jsequeir'  # lowercase!
    assert str(bob) == 'Julian Sequeira (jsequeir)'
    assert repr(bob) == 'User("julian", "Sequeira")'


def test_tania_title_name():
    bob = User('Tania', 'Courageous')
    assert bob.get_full_name == 'Tania Courageous'  # aka PyBites Ninja
    assert bob.username == 'tcourage'  # lowercase!
    assert str(bob) == 'Tania Courageous (tcourage)'
    assert repr(bob) == 'User("Tania", "Courageous")'


def test_noah_use_dunder_in_repr():
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    class SpecialUser(User):
        pass

    noah = SpecialUser('Noah', 'Kagan')
    assert noah.get_full_name == 'Noah Kagan'
    assert noah.username == 'nkagan'  # lowercase!
    assert str(noah) == 'Noah Kagan (nkagan)'

    # it should show the subclass!
    assert repr(noah) == 'SpecialUser("Noah", "Kagan")'
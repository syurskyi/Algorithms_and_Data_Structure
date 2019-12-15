import pytest

from rankings import Ninja, Rankings, bites, names

more_names = [
    ("rey", 287),
    ("bob", 293),
    ("dan", 296),
    ("darren", 298),
    ("david", 313),
    ("sebastian", 323),
    ("ed", 368),
    ("veronica", 410),
    ("valentine", 441),
    ("tyler", 450),
    ("steve", 468),
    ("doug", 469),
    ("noah", 470),
]
FIRST_NINJAS = [Ninja(*ninja) for ninja in zip(names, bites)]
SECOND_NINJAS = [Ninja(*ninja) for ninja in more_names]


def _create_ranks(ninjas=None):
    ranking = Rankings()
    if ninjas is None:
        return ranking

    for ninja in ninjas:
        ranking.add(ninja)
    return ranking


@pytest.fixture
def first_ninjas():
    return FIRST_NINJAS


@pytest.fixture
def second_ninjas():
    return SECOND_NINJAS


@pytest.fixture(scope="module")
def ninja_ranks():
    ranking = Rankings()
    for ninja in FIRST_NINJAS:
        ranking.add(ninja)
    return ranking


def test_ninja_class_empty_init_raises_exception():
    with pytest.raises(TypeError):
        Ninja()


# required class behavior


def test_ninja_class_and_membership(first_ninjas):
    ninja1 = Ninja("snow", 283)
    ninja2 = Ninja("natalia", 282)
    ninja3 = Ninja("okken", 70)
    assert ninja1 in first_ninjas
    assert ninja2 in first_ninjas
    assert ninja3 not in first_ninjas


def test_ninja_str_output(first_ninjas, capfd):
    print(first_ninjas[1])
    output = capfd.readouterr()[0].strip()
    assert output == "[282] natalia"
    print(first_ninjas[3])
    output = capfd.readouterr()[0].strip()
    assert output == "[263] maquina"


# starting len of ninja rankings


def test_first_ninja_ranks_in_object(ninja_ranks):
    assert len(ninja_ranks) == 11


def test_dumping_lowest_ranking_fist_ninjas(ninja_ranks):
    actual = ninja_ranks.dump()
    expected = Ninja(name="sam", bites=195)
    assert actual == expected
    assert len(ninja_ranks) == 10


# highest / lowest ninjas in rankings


def test_highest_ranking_no_arg(ninja_ranks):
    actual = ninja_ranks.highest()
    expected = [Ninja(name="snow", bites=283)]
    assert actual == expected


def test_lowest_ranking_no_arg(ninja_ranks):
    actual = ninja_ranks.lowest()
    expected = [Ninja(name="sara", bites=196)]
    assert actual == expected


def test_lowest_ranking_with_arg(ninja_ranks):
    actual = ninja_ranks.lowest(3)
    expected = [
        Ninja(name="sara", bites=196),
        Ninja(name="james", bites=197),
        Ninja(name="fred", bites=204),
    ]
    assert actual == expected


def test_adding_a_ninja(ninja_ranks):
    ninja_ranks.add(Ninja(name="sam", bites=195))
    assert len(ninja_ranks) == 11


def test_lowest_ranking_after_adding_more_ninjas(ninja_ranks):
    actual = ninja_ranks.lowest(3)
    expected = [
        Ninja(name="sam", bites=195),
        Ninja(name="sara", bites=196),
        Ninja(name="james", bites=197),
    ]
    assert actual == expected

    # now add the ninjas of first_ninja_ranks
    for ninja in SECOND_NINJAS:
        ninja_ranks.add(ninja)

    # check lowest again, it should have changed
    actual = ninja_ranks.highest(3)
    expected = [
        Ninja(name="noah", bites=470),
        Ninja(name="doug", bites=469),
        Ninja(name="steve", bites=468),
    ]
    assert actual == expected


# pairing of ninjas


def test_pairing_with_no_arg(ninja_ranks):
    actual = ninja_ranks.pair_up()
    assert len(actual) == 3

    expected = (Ninja(name="doug", bites=469), Ninja(name="sara", bites=196))
    assert actual[1] == expected


def test_pairing_with_count_arg(ninja_ranks):
    actual = ninja_ranks.pair_up(5)
    assert len(actual) == 5

    expected = (Ninja(name="noah", bites=470),
                Ninja(name="sam", bites=195))
    assert actual[0] == expected

    expected = (Ninja(name="valentine", bites=441),
                Ninja(name="kenneth", bites=216))
    assert actual[-1] == expected
from collections import defaultdict

import pytest

from Previous.names import group_names_by_country, data

# another output to test with
data2 = """last_name,first_name,country_code
Poxton,Sydney,CZ
Kynman,Bryant,NL
Mockler,Leese,AF
Gillicuddy,Raffaello,IR
Renyard,Carlo,CO
Beadham,Evonne,CZ
Tunstall,Allissa,IR
Kamenar,Augy,IR
Insko,Ave,NL
Pigney,Gavrielle,ID"""


@pytest.fixture
def grouping1():
    return group_names_by_country(data)


@pytest.fixture
def grouping2():
    return group_names_by_country(data2)


def test_return_type(grouping1, grouping2):
    assert type(grouping1) == defaultdict
    assert type(grouping2) == defaultdict


def test_return_dict_len(grouping1, grouping2):
    assert len(grouping1) == 7
    assert len(grouping2) == 6


@pytest.mark.parametrize('key, expected', [
    ('BR', ['Alphonso Harrold']),
    ('CN', ['Davie Halbard', 'Ines Parrett', 'Margo Apdell']),
    ('ID', ['Husain Watsham', 'Sula Wasielewski']),
    ('PL', ['Kermit Braunle']),
    ('RU', ['Deerdre Tomblings']),
    ('SE', ['Luke Brenston']),
    ('TD', ['Rudolph Jeffry']),
])
def test_grouping1_return(grouping1, key, expected):
    assert sorted(grouping1[key]) == expected


@pytest.mark.parametrize('key, expected', [
    ('AF', ['Leese Mockler']),
    ('CO', ['Carlo Renyard']),
    ('CZ', ['Evonne Beadham', 'Sydney Poxton']),
    ('ID', ['Gavrielle Pigney']),
    ('IR', ['Allissa Tunstall', 'Augy Kamenar', 'Raffaello Gillicuddy']),
    ('NL', ['Ave Insko', 'Bryant Kynman']),
])
def test_grouping2_return(grouping2, key, expected):
    assert sorted(grouping2[key]) == expected
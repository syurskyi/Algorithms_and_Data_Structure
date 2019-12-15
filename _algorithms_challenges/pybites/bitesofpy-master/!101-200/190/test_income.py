import pytest

from Previous.income import get_income_distribution

EXPECTED = {'High income': ['Aruba',
                            'Argentina',
                            'Antigua and Barbuda',
                            'Bahamas, The',
                            'Barbados',
                            'Chile',
                            'Curacao',
                            'Cayman Islands',
                            'St. Kitts and Nevis',
                            'St. Martin (French part)',
                            'Panama',
                            'Puerto Rico',
                            'Sint Maarten (Dutch part)',
                            'Turks and Caicos Islands',
                            'Trinidad and Tobago',
                            'Uruguay',
                            'British Virgin Islands',
                            'Virgin Islands (U.S.)'],
            'Low income': ['Haiti'],
            'Lower middle income': ['Bolivia',
                                    'Honduras',
                                    'Nicaragua',
                                    'El Salvador'],
            'Upper middle income': ['Belize',
                                    'Brazil',
                                    'Colombia',
                                    'Costa Rica',
                                    'Cuba',
                                    'Dominica',
                                    'Dominican Republic',
                                    'Ecuador',
                                    'Grenada',
                                    'Guatemala',
                                    'Guyana',
                                    'Jamaica',
                                    'St. Lucia',
                                    'Mexico',
                                    'Peru',
                                    'Paraguay',
                                    'Suriname',
                                    'St. Vincent and the Grenadines',
                                    'Venezuela, RB']}


@pytest.fixture(scope="module")
def actual():
    return get_income_distribution()


@pytest.mark.parametrize("income, countries", EXPECTED.items())
def test_return_function(actual, income, countries):
    assert income in actual
    assert sorted(actual[income]) == sorted(countries)
from cal import get_weekdays

april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    January 1956
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""


def test_april_1981():
    weekdays = get_weekdays(april_1981)
    assert len(weekdays) == 30
    assert weekdays[25] == 'Sa'
    assert weekdays[22] == 'We'


def test_jan_1986():
    weekdays = get_weekdays(jan_1986)
    assert len(weekdays) == 31
    assert weekdays[20] == 'Mo'
    assert weekdays[16] == 'Th'


def test_jan_1956():
    weekdays = get_weekdays(jan_1956)
    assert len(weekdays) == 31
    assert weekdays[13] == 'Fr'
    assert weekdays[31] == 'Tu'
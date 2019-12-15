from grid import print_sequence_route

small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""


def test_print_sequence_route_small_grid(capfd):
    expected = """1 2 ⇓
    3 ⇐
    4 5 ⇑
    6 7 ⇒
    8 9 10 ⇓
    11 12 13 ⇐
    14 15 16 17 ⇑
    18 19 20 21 ⇒
    22 23 24 25""".splitlines()

    print_sequence_route(small_grid)
    output = capfd.readouterr()[0].splitlines()

    for i, j in zip(expected, output):
        assert i.strip() == j.strip()


intermediate_grid = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""


def test_print_sequence_route_intermediate_grid(capfd):
    expected = """1 2 ⇓
    3 ⇐
    4 5 ⇑
    6 7 ⇒
    8 9 10 ⇓
    11 12 13 ⇐
    14 15 16 17 ⇑
    18 19 20 21 ⇒
    22 23 24 25 26 ⇓
    27 28 29 30 31 ⇐
    32 33 34 35 36 37 ⇑
    38 39 40 41 42 43 ⇒
    44 45 46 47 48 49""".splitlines()

    print_sequence_route(intermediate_grid)
    output = capfd.readouterr()[0].splitlines()

    for i, j in zip(expected, output):
        assert i.strip() == j.strip()


big_grid = """
73 - 74 - 75 - 76 - 77 - 78 - 79 - 80 - 81
 |
72   43 - 44 - 45 - 46 - 47 - 48 - 49 - 50
 |    |                                  |
71   42   21 - 22 - 23 - 24 - 25 - 26   51
 |    |    |                        |    |
70   41   20    7 -  8 -  9 - 10   27   52
 |    |    |    |              |    |    |
69   40   19    6    1 -  2   11   28   53
 |    |    |    |         |    |    |    |
68   39   18    5 -  4 -  3   12   29   54
 |    |    |                   |    |    |
67   38   17 - 16 - 15 - 14 - 13   30   55
 |    |                             |    |
66   37 - 36 - 35 - 34 - 33 - 32 - 31   56
 |                                       |
65 - 64 - 63 - 62 - 61 - 60 - 59 - 58 - 57
"""


def test_print_sequence_route_big_grid(capfd):
    expected = """1 2 ⇓
    3 ⇐
    4 5 ⇑
    6 7 ⇒
    8 9 10 ⇓
    11 12 13 ⇐
    14 15 16 17 ⇑
    18 19 20 21 ⇒
    22 23 24 25 26 ⇓
    27 28 29 30 31 ⇐
    32 33 34 35 36 37 ⇑
    38 39 40 41 42 43 ⇒
    44 45 46 47 48 49 50 ⇓
    51 52 53 54 55 56 57 ⇐
    58 59 60 61 62 63 64 65 ⇑
    66 67 68 69 70 71 72 73 ⇒
    74 75 76 77 78 79 80 81 """.splitlines()

    print_sequence_route(big_grid)
    output = capfd.readouterr()[0].splitlines()

    for i, j in zip(expected, output):
        assert i.strip() == j.strip()